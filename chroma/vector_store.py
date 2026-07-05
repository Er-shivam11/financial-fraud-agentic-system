from pathlib import Path

import chromadb

from embeddings.embedding_service import generate_embedding

# Persistent database
client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="banking_knowledge"
)

knowledge_folder = Path("chroma/knowledge")


def load_documents():

    for file in knowledge_folder.glob("*.txt"):

        text = file.read_text(encoding="utf-8")

        embedding = generate_embedding(text)

        collection.upsert(
            ids=[file.stem],
            documents=[text],
            embeddings=[embedding],
        )

    print("Knowledge Base Loaded")


def search_documents(question: str, k: int = 2):

    embedding = generate_embedding(question)

    result = collection.query(
        query_embeddings=[embedding],
        n_results=k,
    )

    return result