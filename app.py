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
            print("\nGenerating Sample Embedding...\n")

            sample = "Fraud is an unauthorized transaction."

            vector = generate_embedding(sample)

            print(f"Text : {sample}")

            print(f"\nEmbedding Dimension : {len(vector)}")

            print("\nFirst 10 Values")

            for value in vector[:10]:
                print(value)
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

        print("\nAI Answer\n")
        print(result["answer"])

        print("\n" + "-" * 60 + "\n")


if __name__ == "__main__":
    main()