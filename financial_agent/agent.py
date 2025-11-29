import os
from google.adk.agents import LlmAgent
from google.adk.agents.remote_a2a_agent import RemoteA2aAgent, AGENT_CARD_WELL_KNOWN_PATH
from google.adk.a2a.utils.agent_to_a2a import to_a2a
from google.adk.models.google_llm import Gemini
from google.genai import types
from .fraud_agent import fraud_app, remote_fraud_agent
from .snowflake_tool import (
    get_account_balance,
    get_customer_info,
    get_transaction_info,
    get_merchant_risk
)

# Retry configuration
retry_config = types.HttpRetryOptions(
    attempts=5, exp_base=7, initial_delay=1,
    http_status_codes=[429, 500, 503, 504]
)

# Financial Operations Agent
financial_agent = LlmAgent(
    model=Gemini(model="gemini-2.5-flash-lite", retry_options=retry_config),
    name="FinancialOpsAgent",
    description="Handles account lookup, balances, customer info, and transaction details.",
    instruction="""
    You are a financial operations analyst. 
    Use the provided tools to answer questions about accounts, balances, and transactions.
    If data is missing, say 'Unknown'.
    """,
    tools=[get_account_balance, get_customer_info, get_transaction_info],
)

financial_app = to_a2a(financial_agent, port=9001)

# Remote sub-agent
remote_financial_agent = RemoteA2aAgent(
    name="FinancialOpsAgent",
    description="Remote financial operations agent.",
    agent_card=f"http://localhost:9001{AGENT_CARD_WELL_KNOWN_PATH}",
)

# Unified Support Agent
root_agent = LlmAgent(
    model=Gemini(model="gemini-2.5-flash-lite", retry_options=retry_config),
    name="UnifiedSupportAgent",
    description="Unified agent that uses both Financial & Fraud agents.",
    instruction="""
    You handle customer queries that require both financial operations and fraud detection.
    Use sub-agents for factual lookup before answering.
    """,
    sub_agents=[remote_financial_agent, remote_fraud_agent],
)
