# chroma/vector_store.py
import chromadb

from embeddings.embedding_service import generate_embedding

# Persistent Chroma database
client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="banking_knowledge"
)


def load_documents():
    """
    Insert knowledge documents once.
    """

    documents = [
        {
            "id": "doc1",
            "text": "High risk merchants are monitored for unusual transaction activity."
        },
        {
            "id": "doc2",
            "text": "KYC verification is mandatory before opening a bank account."
        },
        {
            "id": "doc3",
            "text": "Transactions above 10000 dollars require AML review."
        },
        {
            "id": "doc4",
            "text": "Multiple failed login attempts may indicate account compromise."
        },
        {
            "id": "doc5",
            "text": "Rapid transfers between multiple accounts can indicate money laundering."
        }
    ]

    existing = set(collection.get()["ids"])

    for doc in documents:

        if doc["id"] in existing:
            continue

        embedding = generate_embedding(doc["text"])

        collection.add(
            ids=[doc["id"]],
            documents=[doc["text"]],
            embeddings=[embedding]
        )

    print("Knowledge Base Ready.")


def search_documents(query: str, top_k: int = 3):
    """
    Returns raw Chroma result.
    """

    embedding = generate_embedding(query)

    return collection.query(
        query_embeddings=[embedding],
        n_results=top_k
    )


def retrieve_context(query: str, top_k: int = 3) -> str:
    """
    Returns formatted text that will be given to the LLM.
    """

    results = search_documents(query, top_k)

    docs = results["documents"][0]

    if not docs:
        return ""

    return "\n".join(docs)