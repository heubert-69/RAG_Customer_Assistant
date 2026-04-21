from core.vector_store import collection

def retrieve(query_embedding, k=3):
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=k
    )
    docs = results["documents"][0]
    scores = results["distances"][0]
    return docs, scores
