import os
import subprocess
from pathlib import Path
from dotenv import load_dotenv
import snowflake.connector
import pandas as pd
import asyncio

from google.adk.agents import Agent
from google.adk.runners import InMemoryRunner
from google.adk.tools import google_search

# -------------------------------------------------
# Load Gemini API key from .env
# -------------------------------------------------
def load_api_key():
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        raise ValueError("❌ GOOGLE_API_KEY missing in .env file")

    os.environ["GOOGLE_API_KEY"] = api_key
    os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "FALSE"

    print("✅ Gemini API key loaded from .env")
    return api_key

# -------------------------------------------------
# Connect to Snowflake and load tables
# -------------------------------------------------
def load_snowflake_data():
    conn = snowflake.connector.connect(
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
        database=os.getenv("SNOWFLAKE_DATABASE"),
        schema=os.getenv("SNOWFLAKE_SCHEMA"),
    )

    df_customer = pd.read_sql("SELECT * FROM dim_customer", conn)
    df_account = pd.read_sql("SELECT * FROM dim_account", conn)
    df_merchants = pd.read_sql("SELECT * FROM dim_merchant", conn)
    df_transactions = pd.read_sql("SELECT * FROM fact_transactions", conn)

    print("✅ Data loaded from Snowflake")
    return df_customer, df_account, df_merchants, df_transactions

# -------------------------------------------------
# Precompute high-risk / high-value summaries
# -------------------------------------------------
def preprocess_data(df_customer, df_account, df_merchants, df_transactions):
    high_risk_merchants = df_merchants[df_merchants['RISK_SCORE'] >= 40]['MERCHANT_ID'].tolist()
    high_value_txns = df_transactions[df_transactions['AMOUNT'] >= 5000]
    high_risk_customers = high_value_txns[high_value_txns['MERCHANT_ID'].isin(high_risk_merchants)]['CUSTOMER_ID'].unique().tolist()

    print(f"✅ High-risk merchants: {high_risk_merchants}")
    print(f"✅ High-risk customers: {high_risk_customers}")

    return high_risk_merchants, high_risk_customers

# -------------------------------------------------
# Create agents folder if needed
# -------------------------------------------------
def ensure_agents_folder():
    agents_dir = Path(__file__).parent / "agents"
    agents_dir.mkdir(exist_ok=True)
    
    init_file = agents_dir / "__init__.py"
    if not init_file.exists():
        init_file.touch()
    
    print(f"✅ Agents folder ready: {agents_dir}")
    return agents_dir

# -------------------------------------------------
# Create & run the financial profiler agent
# -------------------------------------------------
async def run_agent_examples(df_customer, df_account, df_merchants, df_transactions, high_risk_merchants, high_risk_customers):
    financial_agent = Agent(
        name="financial_profiler",
        model="gemini-2.5-flash-lite",
        description="Agent that profiles financial transactions, accounts, and fraud risk.",
        instruction=f"""
            You are a financial profiler agent.
            Analyze customer, account, merchant, and transaction data.

            Definitions:
            - High-risk merchant: any merchant with MERCHANT_RISK_SCORE >= 40
            - High-value transaction: any transaction with AMOUNT >= 5000
            - High-risk merchants: {high_risk_merchants}
            - High-risk customers: {high_risk_customers}

            Use the provided Snowflake dataframes (df_customer, df_account, df_merchants, df_transactions)
            to answer queries about customers, accounts, and fraud risks.
        """,
        tools=[google_search],
    )

    runner = InMemoryRunner(agent=financial_agent, app_name="financial_profiler_app")

    print("\n▶ Running financial profiling queries…\n")

    sample_queries = [
        "Profile customer C001: account balance, transaction risk, merchant exposure.",
        "List customers with high-risk merchants and high-value transactions.",
        "Which accounts have suspicious patterns in transactions?"
    ]

    for q in sample_queries:
        responses = await runner.run_debug(q)
        for i, resp in enumerate(responses, 1):
            print(f"\nAnswer {i}:", getattr(resp, 'final_output', resp))

# -------------------------------------------------
# Run CLI commands (optional)
# -------------------------------------------------
def create_sample_agent(api_key, agents_dir):
    sample_agent_path = agents_dir / "financial_profiler"
    subprocess.run(
        ["adk", "create", str(sample_agent_path), "--model", "gemini-2.5-flash-lite", "--api_key", api_key],
        check=True,
    )

def start_adk_web():
    subprocess.run(["adk", "web"], check=True)

# -------------------------------------------------
# MAIN
# -------------------------------------------------
if __name__ == "__main__":
    api_key = load_api_key()
    agents_dir = ensure_agents_folder()
    
    # Load Snowflake data
    df_customer, df_account, df_merchants, df_transactions = load_snowflake_data()

    # Preprocess for high-risk/high-value
    high_risk_merchants, high_risk_customers = preprocess_data(df_customer, df_account, df_merchants, df_transactions)

    # Run agent examples
    asyncio.run(run_agent_examples(df_customer, df_account, df_merchants, df_transactions, high_risk_merchants, high_risk_customers))

    # Optional CLI commands
    create_sample_agent(api_key, agents_dir)
    start_adk_web()

    print("\n🎉 Setup complete. ADK Web UI is now running at:")
    print("👉 http://localhost:8000")
