![AI](future/main.png)
# Production AI Banking Assistant (LangGraph + Snowflake)

Act as a Senior AI Engineer, Python Architect, and LangGraph expert.

Build a production-quality AI Banking Assistant using Python, LangGraph, Snowflake, Chroma, and OpenAI. The goal is educational: I want to learn every major AI Engineering concept by building one realistic project incrementally.

## Requirements

* Use clean architecture and production folder structure.
* Keep every phase beginner-friendly with minimal code.
* Explain every file before writing code.
* Follow SOLID principles and separation of concerns.
* Do not over-engineer or introduce unnecessary abstractions.
* Reuse existing code whenever possible.
* Add one AI concept per phase.

## Technologies

* Python
* LangGraph
* LangChain
* Snowflake Snowpark
* Chroma Vector Database
* OpenAI LLM
* OpenAI Embeddings
* python-dotenv
* Pandas

## Existing Database

Database: AI_BANKING

Schema: CORE

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

DIM_CUSTOMER.CUSTOMER_ID
→ DIM_ACCOUNT.CUSTOMER_ID
→ FACT_TRANSACTIONS.CUSTOMER_ID

DIM_ACCOUNT.ACCOUNT_ID
→ FACT_TRANSACTIONS.ACCOUNT_ID

DIM_MERCHANT.MERCHANT_ID
→ FACT_TRANSACTIONS.MERCHANT_ID

## Final Architecture

User

↓

Manager Agent

↓

Routes requests to:

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

1. SQL Tool

* Execute SQL on Snowflake.
* Return structured results.

2. RAG Tool

* Search embedded documents from Chroma.
* Return relevant context.

3. Calculator Tool

* Perform arithmetic and statistics.
* Used instead of LLM calculations.

## Agents

### Manager Agent

* Understand user intent.
* Select the correct tool or agent.
* Combine outputs.

### Fraud Analyst Agent

* Interpret transaction, customer, and merchant data.
* Explain fraud risk in natural language.
* Never execute SQL directly.

## Memory

Use LangGraph MemorySaver.

The assistant should remember previous conversation context.

Example:

User: Show customer C001.

Later:

User: What is his balance?

The assistant should remember that "his" refers to customer C001.

## RAG

Use Chroma for vector storage.

Later I will add PDFs such as:

* Fraud Policy
* KYC Policy
* AML Guidelines
* Banking SOP

Only these documents should be embedded. Structured Snowflake tables should continue to be queried through SQL rather than RAG.

## Development Strategy

Build the project incrementally.

For each phase:

1. Explain the concept.
2. Explain which files are added or modified.
3. Generate only the code needed for that phase.
4. Ensure the project runs before moving to the next phase.
5. Keep code concise, readable, and production-ready.

The learning roadmap is:

Phase 1 – Snowflake Connection & LLM

Phase 2 – SQL Tool

Phase 3 – LangGraph Workflow

Phase 4 – Conversation Memory

Phase 5 – Embeddings

Phase 6 – Chroma Vector Database

Phase 7 – RAG

Phase 8 – Manager Agent

Phase 9 – Fraud Analyst Agent

Phase 10 – Complete Multi-Agent AI Banking Assistant

still in progress...stay tuned.


