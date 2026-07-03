from services.llm_service import generate_sql, explain
from tools.sql_tool import sql_tool


def sql_generator_node(state):

    sql = generate_sql(
        state["question"],
        state.get("history", [])
    )

    return {
        "sql": sql
    }


def execute_sql_node(state):

    df = sql_tool.invoke(state["sql"])

    return {
        **state,
        "result": df,
    }


def explain_node(state):

    answer = explain(
        state["question"],
        state["result"]
    )

    history = state.get("history", [])

    history.append(
        {
            "question": state["question"],
            "sql": state["sql"],
            "result": state["result"],
            "answer": answer,
        }
    )

    # Keep only the latest interaction
    history = history[-1:]

    return {
        "answer": answer,
        "history": history,
    }