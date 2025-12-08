# backend/ingest_and_index.py
import os, json, re
from pathlib import Path
import nltk
from nltk.tokenize import sent_tokenize

# Ensure punkt is available
nltk.download('punkt', quiet=True)

ROOT = Path(__file__).parent.parent
DATA_DIR = ROOT / "law_data"
OUT_INDEX = Path(__file__).parent / "index.json"

CHUNK_SENTENCE_SIZE = 6  # adjust if you want larger/smaller chunks

SOURCE_RE = re.compile(r"source\s*:\s*(https?://\S+)", re.IGNORECASE)
UPDATED_RE = re.compile(r"last[_\s]?updated\s*:\s*(\S+)", re.IGNORECASE)

def chunk_text(text, sentences_per_chunk=CHUNK_SENTENCE_SIZE):
    sents = sent_tokenize(text)
    chunks = []
    for i in range(0, len(sents), sentences_per_chunk):
        chunk = " ".join(sents[i:i+sentences_per_chunk]).strip()
        if chunk:
            chunks.append(chunk)
    return chunks

def parse_first_line(first_line):
    """
    Try to extract a source URL and last_updated date from the first line.
    Returns (title_meta, source_url, last_updated)
    """
    title_meta = first_line.strip()
    source_url = None
    last_updated = None

    m = SOURCE_RE.search(first_line)
    if m:
        source_url = m.group(1).rstrip('.,;')

    m2 = UPDATED_RE.search(first_line)
    if m2:
        last_updated = m2.group(1).rstrip('.,;')

    # if there's a '|' separator, take part before it as clean title
    if '|' in title_meta:
        title_meta = title_meta.split('|')[0].strip()
    return title_meta, source_url, last_updated

def ingest():
    docs = []
    for filepath in sorted(DATA_DIR.glob("*.txt")):
        raw = filepath.read_text(encoding='utf-8').strip()
        if not raw:
            continue
        lines = raw.splitlines()
        first_line = lines[0].strip() if lines else filepath.stem
        title_meta, source_url, last_updated = parse_first_line(first_line)
        body = "\n".join(lines[1:]).strip() if len(lines) > 1 else title_meta

        chunks = chunk_text(body)
        if not chunks:
            chunks = [body]

        for i, c in enumerate(chunks):
            docs.append({
                "id": f"{filepath.stem}__{i}",
                "title_meta": title_meta,
                "text": c,
                "source_file": filepath.name,
                "source_url": source_url,
                "last_updated": last_updated
            })

    OUT_INDEX.write_text(json.dumps(docs, indent=2, ensure_ascii=False), encoding='utf-8')
    print(f"Ingested {len(docs)} chunks into {OUT_INDEX}")

if __name__ == "__main__":
    ingest()
