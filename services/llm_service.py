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

def generate_sql(question: str) -> str:
    prompt = f"""
You are an expert Snowflake SQL developer.

Database Schema:

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

Relationships:
- DIM_CUSTOMER.CUSTOMER_ID = DIM_ACCOUNT.CUSTOMER_ID
- DIM_CUSTOMER.CUSTOMER_ID = FACT_TRANSACTIONS.CUSTOMER_ID
- DIM_ACCOUNT.ACCOUNT_ID = FACT_TRANSACTIONS.ACCOUNT_ID
- DIM_MERCHANT.MERCHANT_ID = FACT_TRANSACTIONS.MERCHANT_ID

Rules:
- Return ONLY valid Snowflake SQL.
- No explanation.
- No markdown.
- No ```sql``` block.
- Use JOINs whenever required.

Question:
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
Keep the answer under 100 words.
"""

    return llm.invoke(prompt).content.strip()