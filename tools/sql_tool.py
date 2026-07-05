# tools/sql_tool.py
from langchain.tools import tool
from database.snowflake import run_sql


@tool
def sql_tool(query: str):
    """
    Executes Snowflake SQL queries and returns results as a DataFrame.
    Use this tool ONLY for structured database queries.
    """

    try:
        df = run_sql(query)
        return df

    except Exception as e:
        return f"SQL Execution Error: {str(e)}"