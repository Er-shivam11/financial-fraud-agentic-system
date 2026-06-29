from services.llm_service import generate_sql, explain
from tools.sql_tool import sql_tool


def sql_generator_node(state):

    sql = generate_sql(state["question"])

    return {
        **state,
        "sql": sql,
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
        state["result"],
    )

    return {
        **state,
        "answer": answer,
    }