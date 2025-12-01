# streamlit_app/app.py
import streamlit as st
import sys
import os
import asyncio
import pandas as pd

# Add project root to sys.path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from financial_agent.agent import root_agent
from google.adk.runners import InMemoryRunner

runner = InMemoryRunner(agent=root_agent)

st.set_page_config(page_title="Financial & Fraud Agent", layout="wide")
st.title("💰 Financial & Fraud Agent")

# Initialize session state
if "query" not in st.session_state:
    st.session_state.query = ""
if "responses" not in st.session_state:
    st.session_state.responses = []

# User input
st.session_state.query = st.text_input(
    "Enter your query for the agent:", st.session_state.query
)

async def run_agent_query(q):
    """Run the financial agent asynchronously and return events."""
    events = await runner.run_debug(q)
    return events

import asyncio

def handle_query():
    query = st.session_state.query.strip()
    if not query:
        st.warning("Please enter a query!")
        return

    with st.spinner("Running your query..."):
        try:
            loop = asyncio.get_event_loop()
        except RuntimeError:  # no loop in current thread
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)

        try:
            response = loop.run_until_complete(run_agent_query(query))
        except Exception as e:
            st.error(f"Error running agent: {e}")
            return

    # Save response to session state
    st.session_state.responses.append((query, response))
    st.session_state.query = ""  # Clear input


st.button("Run Query", on_click=handle_query)

# Display previous queries and responses
if st.session_state.responses:
    for idx, (query, response) in enumerate(st.session_state.responses[::-1], 1):
        st.markdown(f"### Query {len(st.session_state.responses)-idx+1}: `{query}`")

        results_list = []
        final_text = ""

        # Parse structured events returned by ADK
        if isinstance(response, list):
            for event in response:
                if hasattr(event, "content") and event.content:
                    for part in event.content.parts:
                        func_resp = getattr(part, "function_response", None)
                        if func_resp and hasattr(func_resp, "response"):
                            res = func_resp.response.get("result", [])
                            if isinstance(res, list):
                                results_list.extend(res)
                        text = getattr(part, "text", None)
                        if isinstance(text, str) and text.strip():
                            final_text += text.strip()
        elif isinstance(response, dict):
            results_list = response.get("result", [])
            final_text = response.get("summary", "")
        else:
            final_text = str(response)

        # Display results in a DataFrame if available
        if results_list:
            df = pd.DataFrame(results_list)
            st.write("**Query Results:**")
            st.dataframe(df)

        if final_text:
            st.write("**Agent Summary:**")
            st.write(final_text)
