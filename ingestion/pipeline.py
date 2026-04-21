from ingestion.loader import load_pdf
from ingestion.chunker import chunk_text
from core.embeddings import embed_texts
from core.vector_store import store_embeddings

def ingest_pdf(path):
    text = load_pdf(path)
    chunks = chunk_text(text)
    embeddings = embed_texts(chunks)
    store_embeddings(chunks, embeddings)
