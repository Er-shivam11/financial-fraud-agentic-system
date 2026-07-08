from agents.manager_agent import route_question
from agents.sql_agent import sql_agent
from agents.rag_agent import rag_agent


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

    history = []

    while True:

        question = input("Ask (type 'exit' to quit): ")

        if question.lower() == "exit":
            print("\nGoodbye!")
            break

        route = route_question(question)

        print("\nManager Decision\n")
        print(route.upper())

        if route == "sql":

            result = sql_agent(
                question,
                history=history
            )

            print("\nGenerated SQL\n")
            print(result["sql"])

            print("\nResult\n")
            print(result["result"])

            history.append(
                {
                    "question": question,
                    "sql": result["sql"],
                    "result": result["result"]
                }
            )

            history = history[-5:]

        else:

            result = rag_agent(question)

            print("\nRetrieved Context\n")
            print(result["context"])

            print("\nAI Answer\n")
            print(result["answer"])

        print("\n" + "-" * 60 + "\n")


if __name__ == "__main__":
    main()