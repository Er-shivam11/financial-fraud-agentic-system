from chroma.vector_store import retrieve_context
from services.llm_service import rag_answer


def rag_agent(question):

    context = retrieve_context(question)

    answer = rag_answer(question, context)

    return {
        "type": "rag",
        "context": context,
        "answer": answer
    }