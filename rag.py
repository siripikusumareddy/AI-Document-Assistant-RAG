from ollama import chat
from embeddings import model
from vector_db import search

def ask_rag(question):
    query_embedding = model.encode(question).tolist()
    results = search(query_embedding)
    print("\n========== SEARCH RESULTS ==========")
    print(results)
    context = "\n\n".join(results["documents"][0])
    print("\n========== CONTEXT ==========")
    print(context)
    prompt = f"""
You are a helpful AI assistant.

Answer ONLY using the context below.

If the answer is not present, say:
"I couldn't find that information in the document."
Context:
{context}
Question:
{question}
"""
    response = chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return (
    response["message"]["content"],
    results["documents"][0],
    results["metadatas"][0]
)