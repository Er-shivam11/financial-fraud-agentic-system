# test_chroma.py
from chroma.vector_store import (
    load_documents,
    retrieve_context,
)

load_documents()

query = "How can a bank detect money laundering?"

print("\nQuestion:\n")
print(query)

print("\nRetrieved Context:\n")

context = retrieve_context(query)

print(context)