from chroma.vector_store import load_documents, search_documents

load_documents()

result = search_documents(
    "How do banks detect fraud?"
)

print(result)