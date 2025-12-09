# backend/app.py  (FULL file — replace your current app.py with this)
import os, json
from flask import Flask, request, jsonify, send_from_directory
from pathlib import Path
from rank_bm25 import BM25Okapi
from flask_cors import CORS
from nltk.tokenize import word_tokenize, sent_tokenize
import nltk
nltk.download('punkt', quiet=True)

BASE = Path(__file__).parent
ROOT = BASE.parent

INDEX_PATH = BASE / "index.json"
FRONTEND_DIR = ROOT / "frontend"

# load index
if not INDEX_PATH.exists():
    raise SystemExit(f"index.json not found at {INDEX_PATH}. Run ingest_and_index.py first.")

with open(INDEX_PATH, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# BM25 index on chunks
tokenized_corpus = [word_tokenize(d['text'].lower()) for d in docs]
bm25 = BM25Okapi(tokenized_corpus)

app = Flask(__name__, static_folder=str(FRONTEND_DIR), static_url_path="/")

@app.route('/')
def index_page():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/query', methods=['POST'])
def query_api():
    """Existing search-only endpoint (returns raw snippets)."""
    data = request.get_json(force=True)
    user_text = data.get('message', '').strip()
    if not user_text:
        return jsonify({"error": "Message cannot be empty"}), 400
    top_k = int(data.get('top_k', 5))

    tokens = word_tokenize(user_text.lower())
    scores = bm25.get_scores(tokens)

    import numpy as np
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

    return jsonify({
        "query": user_text,
        "results": results
    })

def extractive_summary(user_text, top_k=5, summary_sentences=3):
    """
    Improved extractive summary:
    - Retrieves top_k chunks
    - Splits into sentences
    - Scores every sentence by:
        sent_bm25_score + 0.75 * keyword_overlap + 0.35 * title_match_boost
    - Returns top summary_sentences in original order
    """
    from nltk.tokenize import word_tokenize, sent_tokenize
    from rank_bm25 import BM25Okapi
    import numpy as np
    import math

    if not user_text:
        return {"summary": "", "sources": [], "used_snippets": []}

    # prepare query tokens
    q_tokens = word_tokenize(user_text.lower())

    # get top_k chunk indices by corpus BM25 (as before)
    corpus_scores = bm25.get_scores(q_tokens)
    ranked_idx = np.argsort(corpus_scores)[::-1][:top_k]
    top_chunks = [docs[int(i)] for i in ranked_idx]

    # collect all sentences and map to their chunk meta
    sentences = []
    sent_meta = []  # store (chunk_index, title_meta, source_url)
    for ci, c in enumerate(top_chunks):
        txt = c.get("text", "") or ""
        sents = sent_tokenize(txt)
        for s in sents:
            s_strip = s.strip()
            if s_strip:
                sentences.append(s_strip)
                sent_meta.append({
                    "chunk_idx": ci,
                    "title_meta": (c.get("title_meta") or "").lower(),
                    "source_url": c.get("source_url")
                })

    if not sentences:
        return {"summary": "", "sources": [], "used_snippets": []}

    # BM25 over sentences
    sent_tokens = [word_tokenize(s.lower()) for s in sentences]
    sent_bm25 = BM25Okapi(sent_tokens)
    sent_scores = sent_bm25.get_scores(q_tokens)

    # compute keyword overlap and title boosts
    q_set = set([t for t in q_tokens if len(t) > 1])
    scores = []
    for i, s in enumerate(sentences):
        s_low = s.lower()
        s_tokens = set(sent_tokens[i])

        # overlap = count of query tokens present in sentence
        overlap = len(q_set.intersection(s_tokens))

        # normalized overlap (0..1)
        overlap_norm = overlap / (len(q_set) if len(q_set) > 0 else 1)

        # title match boost: if any query token appears in the title_meta of that chunk
        title = sent_meta[i]["title_meta"] or ""
        title_boost = 0.0
        if any(qt in title for qt in q_set):
            title_boost = 1.0

        # final score: weighted sum (tunable)
        final = float(sent_scores[i]) + 0.75 * overlap_norm + 0.35 * title_boost

        # length penalty: prefer sentences that are not excessively long
        length_penalty = 1.0
        if len(s) > 300:
            length_penalty = 0.9
        final = final * length_penalty

        scores.append(final)

    # pick top N sentence indices
    idxs = list(range(len(sentences)))
    top_sent_idxs = sorted(idxs, key=lambda i: -scores[i])[:summary_sentences]

    # preserve original order in the combined text
    top_sent_idxs_sorted = sorted(top_sent_idxs)

    summary = " ".join([sentences[i] for i in top_sent_idxs_sorted])

    # collect unique sources from the chunks used
    sources = []
    used_snips = []
    for ci in ranked_idx:
        c = docs[int(ci)]
        if c.get("source_url") and c.get("source_url") not in sources:
            sources.append(c.get("source_url"))
        used_snips.append({
            "id": c.get("id"),
            "title_meta": c.get("title_meta"),
            "source_url": c.get("source_url")
        })

    return {
        "summary": summary,
        "sources": sources,
        "used_snippets": used_snips
    }

@app.route('/api/answer', methods=['POST'])
def answer_api():
    """Higher-level endpoint: returns short answer (extractive summary) + supporting snippets."""
    data = request.get_json(force=True)
    user_text = data.get('message', '').strip()
    if not user_text:
        return jsonify({"error": "Message cannot be empty"}), 400

    top_k = int(data.get('top_k', 5))
    summary_sentences = int(data.get('summary_sentences', 3))

    # get snippets (reuse query_api logic)
    tokens = word_tokenize(user_text.lower())
    scores = bm25.get_scores(tokens)
    import numpy as np
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

    # build extractive summary from top chunks
    summ = extractive_summary(user_text, top_k=top_k, summary_sentences=summary_sentences)

    return jsonify({
        "query": user_text,
        "summary": summ["summary"],
        "sources": summ["sources"],
        "used_snippets": summ["used_snippets"],
        "results": results
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)
