# backend/app.py  (FULL FILE – SAFE FOR DEPLOYMENT)

import json
import re
import numpy as np
from pathlib import Path
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from rank_bm25 import BM25Okapi

# --------------------
# App setup
# --------------------
BASE = Path(__file__).parent
ROOT = BASE.parent

INDEX_PATH = BASE / "index.json"
FRONTEND_DIR = ROOT / "frontend"

app = Flask(__name__, static_folder=str(FRONTEND_DIR), static_url_path="/")
CORS(app)

# --------------------
# Load indexed docs
# --------------------
if not INDEX_PATH.exists():
    raise SystemExit(f"index.json not found at {INDEX_PATH}. Run ingest_and_index.py first.")

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    docs = json.load(f)

# --------------------
# Tokenization helpers (NO NLTK)
# --------------------
def tokenize(text: str):
    return text.lower().split()

def split_sentences(text: str):
    return [s.strip() for s in re.split(r'(?<=[.!?])\s+', text) if s.strip()]

# --------------------
# Build BM25 index
# --------------------
tokenized_corpus = [tokenize(d["text"]) for d in docs]
bm25 = BM25Okapi(tokenized_corpus)

# --------------------
# Routes
# --------------------
@app.route("/")
def index_page():
    return send_from_directory(app.static_folder, "index.html")

# --------------------
# Search-only API
# --------------------
@app.route("/api/query", methods=["POST"])
def query_api():
    data = request.get_json(force=True)
    user_text = data.get("message", "").strip()
    if not user_text:
        return jsonify({"error": "Message cannot be empty"}), 400

    top_k = int(data.get("top_k", 5))
    tokens = tokenize(user_text)

    scores = bm25.get_scores(tokens)
    ranked_idx = np.argsort(scores)[::-1][:top_k]

    results = []
    for idx in ranked_idx:
        d = docs[int(idx)]
        results.append({
            "id": d.get("id"),
            "title_meta": d.get("title_meta"),
            "text": d.get("text"),
            "source_file": d.get("source_file"),
            "source_url": d.get("source_url"),
            "last_updated": d.get("last_updated"),
            "score": float(scores[int(idx)])
        })

    return jsonify({"query": user_text, "results": results})

# --------------------
# Extractive summary
# --------------------
def extractive_summary(user_text, top_k=5, summary_sentences=3):
    q_tokens = tokenize(user_text)

    corpus_scores = bm25.get_scores(q_tokens)
    ranked_idx = np.argsort(corpus_scores)[::-1][:top_k]
    top_chunks = [docs[int(i)] for i in ranked_idx]

    sentences = []
    sent_meta = []

    for ci, c in enumerate(top_chunks):
        for s in split_sentences(c.get("text", "")):
            sentences.append(s)
            sent_meta.append({
                "title_meta": (c.get("title_meta") or "").lower(),
                "source_url": c.get("source_url")
            })

    if not sentences:
        return {"summary": "", "sources": [], "used_snippets": []}

    sent_tokens = [tokenize(s) for s in sentences]
    sent_bm25 = BM25Okapi(sent_tokens)
    sent_scores = sent_bm25.get_scores(q_tokens)

    q_set = set(q_tokens)
    final_scores = []

    for i, s in enumerate(sentences):
        overlap = len(q_set.intersection(sent_tokens[i]))
        overlap_norm = overlap / (len(q_set) or 1)

        title_boost = 1.0 if any(q in sent_meta[i]["title_meta"] for q in q_set) else 0.0

        score = float(sent_scores[i]) + 0.75 * overlap_norm + 0.35 * title_boost
        if len(s) > 300:
            score *= 0.9

        final_scores.append(score)

    top_idxs = sorted(range(len(sentences)), key=lambda i: -final_scores[i])[:summary_sentences]
    top_idxs = sorted(top_idxs)

    summary = " ".join(sentences[i] for i in top_idxs)

    sources = []
    for c in top_chunks:
        if c.get("source_url") and c["source_url"] not in sources:
            sources.append(c["source_url"])

    return {
        "summary": summary,
        "sources": sources,
        "used_snippets": [
            {
                "id": c.get("id"),
                "title_meta": c.get("title_meta"),
                "source_url": c.get("source_url")
            } for c in top_chunks
        ]
    }

# --------------------
# Answer API
# --------------------
@app.route("/api/answer", methods=["POST"])
def answer_api():
    data = request.get_json(force=True)
    user_text = data.get("message", "").strip()
    if not user_text:
        return jsonify({"error": "Message cannot be empty"}), 400

    top_k = int(data.get("top_k", 5))
    summary_sentences = int(data.get("summary_sentences", 3))

    tokens = tokenize(user_text)
    scores = bm25.get_scores(tokens)
    ranked_idx = np.argsort(scores)[::-1][:top_k]

    results = []
    for idx in ranked_idx:
        d = docs[int(idx)]
        results.append({
            "id": d.get("id"),
            "title_meta": d.get("title_meta"),
            "text": d.get("text"),
            "source_file": d.get("source_file"),
            "source_url": d.get("source_url"),
            "last_updated": d.get("last_updated"),
            "score": float(scores[int(idx)])
        })

    summary_data = extractive_summary(
        user_text,
        top_k=top_k,
        summary_sentences=summary_sentences
    )

    return jsonify({
        "query": user_text,
        "summary": summary_data["summary"],
        "sources": summary_data["sources"],
        "used_snippets": summary_data["used_snippets"],
        "results": results
    })

# --------------------
# Local run
# --------------------
if __name__ == "__main__":
    app.run(debug=True, port=5000)
