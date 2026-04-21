import chromadb

client = chromadb.Client()
collection = client.get_or_create_collection(name="docs")

def store_embeddings(chunks, embeddings):
    for i, (chunk, emb) in enumerate(zip(chunks, embeddings)):
        collection.add(
            documents=[chunk],
            embeddings=[emb],
            ids=[str(i)]
        )
