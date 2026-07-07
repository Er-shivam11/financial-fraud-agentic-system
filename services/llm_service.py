# services/llm_service.py

import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables
load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0,
    max_output_tokens=512,
)


def clean_sql(sql: str) -> str:
    """
    Remove markdown formatting if the LLM accidentally returns it.
    """

    sql = sql.strip()

    if sql.startswith("```sql"):
        sql = sql.replace("```sql", "")

    sql = sql.replace("```", "")

    return sql.strip()


def is_valid_sql(sql: str) -> bool:
    """
    Basic SQL validation before executing against Snowflake.
    """

    sql = sql.strip().upper()

    valid_starts = (
        "SELECT",
        "WITH",
        "INSERT",
        "UPDATE",
        "DELETE",
        "CREATE",
    )

    return (
        sql.startswith(valid_starts)
        and sql.endswith(";")
    )


def generate_sql(question: str, history=None):
    """
    Generate Snowflake SQL using Gemini.
    Automatically retries once if SQL is invalid.
    """

    history_context = ""

    if history:
        last = history[-1]

        history_context = f"""
Previous Interaction

Question:
{last["question"]}

SQL:
{last["sql"]}

Result:
{last["result"]}
"""

    prompt = f"""
You are an expert Snowflake SQL Developer.

Database Schema

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

Rules

- Return ONLY executable Snowflake SQL.
- Do NOT explain anything.
- Do NOT use markdown.
- Do NOT use ```sql.
- Do NOT use backticks.
- Do NOT add comments.
- Output must start with SELECT, WITH, INSERT, UPDATE, DELETE or CREATE.
- Return exactly one SQL statement.
- End the SQL with a semicolon.

{history_context}

Current Question

{question}
"""

    # ---------- First Attempt ----------

    sql = llm.invoke(prompt).content
    sql = clean_sql(sql)

    if is_valid_sql(sql):
        return sql

    # ---------- Retry Once ----------

    retry_prompt = f"""
Your previous SQL was incomplete or invalid.

Generate ONE complete executable Snowflake SQL statement.

Rules

- Return ONLY SQL.
- No explanation.
- No markdown.
- End with semicolon.

Question:

{question}
"""

    sql = llm.invoke(retry_prompt).content
    sql = clean_sql(sql)

    return sql

def rag_answer(question: str, context: str) -> str:
    """
    Generate an answer using retrieved context.
    """

    prompt = f"""
You are a banking assistant.

Answer ONLY from the provided context.

If the answer is not available in the context,
reply:

"I don't have enough information."

Context:
{context}

Question:
{question}

Answer:
"""

    return llm.invoke(prompt).content.strip()