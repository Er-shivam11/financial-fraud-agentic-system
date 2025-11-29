# financial_agent/fraud_agent.py

from google.adk.agents import LlmAgent
from google.adk.a2a.utils.agent_to_a2a import to_a2a
from google.adk.models.google_llm import Gemini
from google.genai import types
from .snowflake_tool import get_transaction_info, get_customer_info, get_merchant_risk

# Retry configuration
retry_config = types.HttpRetryOptions(
    attempts=5, exp_base=7, initial_delay=1,
    http_status_codes=[429, 500, 503, 504]
)

# Fraud Risk Agent
fraud_agent = LlmAgent(
    model=Gemini(model="gemini-2.5-flash-lite", retry_options=retry_config),
    name="FraudRiskAgent",
    description="Analyzes fraud transactions and risk score using merchant and customer metadata.",
    instruction="""
    You are a fraud detection specialist. 
    Always use tools to lookup transaction, merchant, and customer data. 
    Return a clear fraud risk explanation.
    """,
    tools=[get_transaction_info, get_customer_info, get_merchant_risk],
)

fraud_app = to_a2a(fraud_agent, port=9002)

# Remote Fraud Agent
remote_fraud_agent = fraud_agent  # Will be used in agent.py as sub-agent






