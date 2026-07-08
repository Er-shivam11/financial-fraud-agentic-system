from services.llm_service import (
    llm,
    clean_sql,
    is_valid_sql
)

from database.snowflake import run_sql


def fraud_agent(question: str, history=None):

    with open(
        "prompts/fraud_prompt.txt",
        "r",
        encoding="utf-8"
    ) as file:
        fraud_prompt = file.read()

    schema = """
DIM_CUSTOMER(
CUSTOMER_ID,
FIRST_NAME,
LAST_NAME,
AGE,
COUNTRY
)

DIM_ACCOUNT(
ACCOUNT_ID,
CUSTOMER_ID,
ACCOUNT_TYPE,
BALANCE
)

DIM_MERCHANT(
MERCHANT_ID,
MERCHANT_NAME,
CATEGORY,
RISK_SCORE
)

FACT_TRANSACTIONS(
TRANSACTION_ID,
CUSTOMER_ID,
ACCOUNT_ID,
MERCHANT_ID,
AMOUNT,
IS_FRAUD
)
"""

    prompt = f"""
{fraud_prompt}

Database Schema:

{schema}

Question:

{question}
"""

    # ---------- First Attempt ----------

    sql = llm.invoke(prompt).content
    sql = clean_sql(sql)

    # ---------- Retry if invalid ----------

    if not is_valid_sql(sql):

        retry_prompt = f"""
Your previous SQL was incomplete or invalid.

Generate exactly one executable Snowflake SQL statement.

Database Schema:

{schema}

Question:
{question}

Rules:

- Return ONLY SQL.
- No explanation.
- No markdown.
- End with semicolon.
- Use only tables from schema.
"""

        sql = llm.invoke(retry_prompt).content
        sql = clean_sql(sql)

    result = run_sql(sql)

    return {
        "type": "fraud",
        "sql": sql,
        "result": result,
    }