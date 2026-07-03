import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load .env
load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0,
    max_output_tokens=512,
)

def generate_sql(question: str, history=None):

    history_context = ""

    if history:
        last = history[-1]

        history_context = f"""
Previous Interaction

Question:
{last['question']}

SQL:
{last['sql']}

Result:
{last['result']}
"""

    prompt = f"""
You are an expert Snowflake SQL developer.

Database:

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

Rules

- Return ONLY executable Snowflake SQL.
- Do NOT explain anything.
- Do NOT use markdown.
- Do NOT use ```sql.
- Do NOT use backticks.
- Do NOT add comments.
- Output must start with SELECT, WITH, INSERT, UPDATE, DELETE or CREATE.
- Return exactly one SQL statement.

{history_context}

Current Question

{question}
"""

    return llm.invoke(prompt).content.strip()

def explain(question: str, rows) -> str:

    prompt = f"""
You are a banking data analyst.

User Question:
{question}

SQL Result:
{rows}

Explain the result in simple English.
Keep the answer under 25 words.
"""

    return llm.invoke(prompt).content.strip()