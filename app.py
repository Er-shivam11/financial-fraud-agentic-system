# app.py
from random import sample

from embeddings.embedding_service import generate_embedding
from graph.workflow import graph


def main():

    print("=" * 60)
    print("      AI Banking Assistant")
    print("=" * 60)

    thread_id = input(
        "Conversation ID (Press Enter for default): "
    ).strip()

    if not thread_id:
        thread_id = "banking-session"

    print()

    while True:

        question = input("Ask (type 'exit' to quit): ")

        if question.lower() == "exit":
            print("\nGoodbye!")
            break

        state = {
            "question": question,
            "sql": None,
            "result": None,
            "answer": None,
        }

        result = graph.invoke(
            state,
            config={
                "configurable": {
                    "thread_id": thread_id
                }
            },
        )

        print("\nGenerated SQL\n")
        print(result["sql"])

        print("\nResult\n")
        print(result["result"])

        print("\nExecution Status\n")
        print(result["answer"])

        print("\n" + "-" * 60 + "\n")


if __name__ == "__main__":
    main()