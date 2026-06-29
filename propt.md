# Production AI Banking Assistant (LangGraph + Snowflake + Gemini)

Act as a Senior AI Engineer, Python Architect, and LangGraph expert.

Build a production-quality AI Banking Assistant using Python, LangGraph, Snowflake, Chroma, and **Google Gemini**. The goal is educational: I want to learn every major AI Engineering concept by building one realistic project incrementally.

## Requirements

* Use clean architecture and production folder structure.
* Keep every phase beginner-friendly with minimal code.
* Explain every file before writing code.
* Follow SOLID principles and separation of concerns.
* Do not over-engineer or introduce unnecessary abstractions.
* Reuse existing code whenever possible.
* Add only one new AI Engineering concept per phase.
* Use the latest stable LangChain APIs.
* Use **Gemini 2.5 Flash** via `langchain-google-genai`, not OpenAI.

## Technologies

* Python
* LangGraph
* LangChain
* Google Gemini 2.5 Flash
* langchain-google-genai
* Snowflake Snowpark
* Chroma Vector Database
* Google Embeddings (later phase)
* python-dotenv
* Pandas

## Existing Database

Database: **AI_BANKING**

Schema: **CORE**

### DIM_CUSTOMER

* CUSTOMER_ID (PK)
* FIRST_NAME
* LAST_NAME
* AGE
* COUNTRY

### DIM_ACCOUNT

* ACCOUNT_ID (PK)
* CUSTOMER_ID (FK)
* ACCOUNT_TYPE
* BALANCE

### DIM_MERCHANT

* MERCHANT_ID (PK)
* MERCHANT_NAME
* CATEGORY
* RISK_SCORE

### FACT_TRANSACTIONS

* TRANSACTION_ID (PK)
* CUSTOMER_ID (FK)
* ACCOUNT_ID (FK)
* MERCHANT_ID (FK)
* AMOUNT
* IS_FRAUD

## Relationships

* DIM_CUSTOMER.CUSTOMER_ID → DIM_ACCOUNT.CUSTOMER_ID
* DIM_CUSTOMER.CUSTOMER_ID → FACT_TRANSACTIONS.CUSTOMER_ID
* DIM_ACCOUNT.ACCOUNT_ID → FACT_TRANSACTIONS.ACCOUNT_ID
* DIM_MERCHANT.MERCHANT_ID → FACT_TRANSACTIONS.MERCHANT_ID

## Final Architecture

User

↓

Manager Agent

↓

Routes to:

* SQL Tool (Snowflake)
* RAG Tool (Chroma + Embeddings)
* Calculator Tool (Python)

↓

Fraud Analyst Agent

↓

Conversation Memory (LangGraph MemorySaver)

↓

Final Response

## Tools

### SQL Tool

* Execute Snowflake SQL.
* Return structured results.

### RAG Tool

* Search Chroma Vector Database.
* Return relevant document chunks.

### Calculator Tool

* Perform mathematical operations instead of using the LLM.

## Agents

### Manager Agent

* Understand user intent.
* Decide which tool or agent to use.
* Combine responses.

### Fraud Analyst Agent

* Analyze customer, merchant and transaction data.
* Explain fraud risk in natural language.
* Never execute SQL directly.

## Memory

Use LangGraph MemorySaver.

Example:

User:
Show customer C001.

Later:

What is his balance?

The assistant should remember that "his" refers to customer C001.

## RAG

Use Chroma.

Later I will add documents such as:

* Fraud Policy
* KYC Policy
* AML Guidelines
* Banking SOP

Only these documents should be embedded.

Structured Snowflake tables must always be queried using SQL, not RAG.

## Development Strategy

Build the project incrementally.

For every phase:

1. Explain the concept.
2. Explain every new file.
3. Generate only the code required for that phase.
4. Ensure the project runs before moving to the next phase.
5. Keep the code production-ready, simple, and beginner-friendly.

## Learning Roadmap

Phase 1 — Snowflake + Gemini LLM

Phase 2 — SQL Tool

Phase 3 — LangGraph Workflow

Phase 4 — Conversation Memory

Phase 5 — Embeddings

Phase 6 — Chroma Vector Database

Phase 7 — RAG

Phase 8 — Manager Agent

Phase 9 — Fraud Analyst Agent

Phase 10 — Complete Multi-Agent AI Banking Assistant

Do not generate the entire project at once. Build one phase at a time with complete explanations. Use Gemini 2.5 Flash throughout the project and optimize prompts to minimize token usage while maintaining code quality.
