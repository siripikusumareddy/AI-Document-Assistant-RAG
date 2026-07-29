import chromadb
from config import CHROMA_DB_PATH

client = chromadb.PersistentClient(path=CHROMA_DB_PATH)

collection = client.get_or_create_collection(
    name="documents"
)


def store_chunks(chunks, embeddings, metadatas):
    try:
        client.delete_collection("documents")
    except:
        pass

    global collection
    collection = client.get_or_create_collection(
        name="documents"
    )

    ids = [str(i) for i in range(len(chunks))]

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings,
        metadatas=metadatas
    )


def search(query_embedding):
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    return results