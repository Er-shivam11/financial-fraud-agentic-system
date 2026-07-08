from services.llm_service import generate_sql
from database.snowflake import run_sql


def sql_agent(question, history=None):

    sql = generate_sql(question, history)

    result = run_sql(sql)

    return {
        "type": "sql",
        "sql": sql,
        "result": result
    }