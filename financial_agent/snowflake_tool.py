# financial_agent/snowflake_tool.py

from google.adk.tools import FunctionTool
from snowflake.snowpark import Session
from dotenv import load_dotenv
import os

load_dotenv()

def get_session():
    conn = {
        "account": os.getenv("SNOWFLAKE_ACCOUNT"),
        "user": os.getenv("SNOWFLAKE_USER"),
        "password": os.getenv("SNOWFLAKE_PASSWORD"),
        "warehouse": os.getenv("SNOWFLAKE_WAREHOUSE"),
        "role": os.getenv("SNOWFLAKE_ROLE"),
        "database": os.getenv("SNOWFLAKE_DATABASE"),
        "schema": os.getenv("SNOWFLAKE_SCHEMA"),
    }
    return Session.builder.configs(conn).create()

def run_query(query: str):
    session = get_session()
    try:
        df = session.sql(query).to_pandas()
        return df.to_dict(orient="records")
    finally:
        session.close()

snowflake_tool = FunctionTool(
    func=run_query,
    require_confirmation=False
)
# -------------------------------
# Dummy Dataset (replace with Snowflake if needed)
# -------------------------------

dim_account = {
    "A1001": {"CUSTOMER_ID": "C001", "ACCOUNT_TYPE": "SAVINGS", "BALANCE": 45000},
    "A1002": {"CUSTOMER_ID": "C002", "ACCOUNT_TYPE": "CURRENT", "BALANCE": 78000},
    "A1003": {"CUSTOMER_ID": "C003", "ACCOUNT_TYPE": "SAVINGS", "BALANCE": 52000},
    "A1004": {"CUSTOMER_ID": "C004", "ACCOUNT_TYPE": "CURRENT", "BALANCE": 0},
    "A1005": {"CUSTOMER_ID": "C005", "ACCOUNT_TYPE": "SAVINGS", "BALANCE": 31000},
}

dim_customer = {
    "C001": {"FIRST_NAME": "Arjun", "LAST_NAME": "Mehta", "AGE": 29, "COUNTRY": "India"},
    "C002": {"FIRST_NAME": "Neha", "LAST_NAME": "Sharma", "AGE": 33, "COUNTRY": "India"},
    "C003": {"FIRST_NAME": "Rahul", "LAST_NAME": "Kumar", "AGE": None, "COUNTRY": "India"},
    "C004": {"FIRST_NAME": "Anita", "LAST_NAME": "Gupta", "AGE": 41, "COUNTRY": "Unknown"},
}

dim_merchant = {
    "M001": {"MERCHANT_NAME": "Flipkart", "CATEGORY": "E-Commerce", "RISK_SCORE": 30},
    "M002": {"MERCHANT_NAME": "Amazon", "CATEGORY": "E-Commerce", "RISK_SCORE": 25},
    "M003": {"MERCHANT_NAME": "Walmart", "CATEGORY": "Retail", "RISK_SCORE": 40},
}

fact_transactions = {
    "T1001": {"CUSTOMER_ID": "C001", "ACCOUNT_ID": "A1001", "MERCHANT_ID": "M001", "AMOUNT": 5000, "IS_FRAUD": 0},
    "T1002": {"CUSTOMER_ID": "C002", "ACCOUNT_ID": "A1002", "MERCHANT_ID": "M002", "AMOUNT": 7000, "IS_FRAUD": 1},
}

# -------------------------------
# Tool Functions
# -------------------------------

def get_account_balance(account_id: str):
    return dim_account.get(account_id, None)

def get_customer_info(customer_id: str):
    return dim_customer.get(customer_id, None)

def get_transaction_info(txn_id: str):
    return fact_transactions.get(txn_id, None)

def get_merchant_risk(merchant_id: str):
    return dim_merchant.get(merchant_id, None)
