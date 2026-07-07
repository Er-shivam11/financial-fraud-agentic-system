from chroma.vector_store import (
    load_documents,
    retrieve_context,
)

from services.llm_service import rag_answer


load_documents()

question = "How can a bank detect money laundering?"

context = retrieve_context(question)

print("\nRetrieved Context\n")
print(context)

print("\nAI Answer\n")

print(rag_answer(question, context))