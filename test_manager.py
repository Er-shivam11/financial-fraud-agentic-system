from agents.manager_agent import route_question
from agents.sql_agent import sql_agent
from agents.rag_agent import rag_agent

question = input("Ask: ")

route = route_question(question)

print("\nManager Decision:")
print(route)

if route == "sql":
    result = sql_agent(question)

    print("\nGenerated SQL\n")
    print(result["sql"])

    print("\nResult\n")
    print(result["result"])

else:
    result = rag_agent(question)

    print("\nRetrieved Context\n")
    print(result["context"])

    print("\nAI Answer\n")
    print(result["answer"])