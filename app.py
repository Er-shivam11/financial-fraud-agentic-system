from agents.manager_agent import route_question
from agents.sql_agent import sql_agent
from agents.rag_agent import rag_agent
from agents.fraud_agent import fraud_agent


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

        # ==========================
        # SQL AGENT
        # ==========================
        if route == "sql":

            result = sql_agent(
                question,
                history=history
            )

            print("\nGenerated SQL\n")
            print(result["sql"])

            print("\nResult\n")
            print(result["result"])

        # ==========================
        # FRAUD AGENT
        # ==========================
        elif route == "fraud":

            result = fraud_agent(
                question,
                history=history
            )

            print("\nGenerated Fraud SQL\n")
            print(result["sql"])

            print("\nFraud Analysis Result\n")
            print(result["result"])

        # ==========================
        # RAG AGENT
        # ==========================
        else:

            result = rag_agent(question)

            print("\nRetrieved Context\n")
            print(result["context"])

            print("\nAI Answer\n")
            print(result["answer"])

        # ==========================
        # SHARED MEMORY
        # ==========================
        history.append(
            {
                "route": route,
                "question": question,
                "response": result
            }
        )

        # Keep only last 5 interactions
        history = history[-5:]

        print("\n" + "-" * 60 + "\n")


if __name__ == "__main__":
    main()