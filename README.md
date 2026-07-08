# Production AI Banking Assistant (LangGraph + Gemini + Snowflake)

![AI](future/main.png)

A production-inspired AI Banking Assistant built to learn modern AI Engineering concepts by implementing them incrementally using LangGraph, Google Gemini, Snowflake, ChromaDB, and Retrieval-Augmented Generation (RAG).

This project focuses on understanding how enterprise AI assistants are designed — from SQL agents and conversation memory to vector databases, multi-agent workflows, fraud analysis, and production-ready architecture.

---

## Project Status

✅ Phase 10 Completed

Current version includes:

* SQL Agent
* RAG Agent
* Fraud Agent
* Manager Agent
* Conversation Memory
* Vector Database
* LLM Intent Routing

---

## Project Goals

The objective of this project is to gain hands-on experience with production AI Engineering concepts by building one real-world application step by step.

Each phase introduces a single concept while keeping the implementation clean, modular, and easy to understand.

Topics covered include:

* AI Agent Architecture
* LangGraph Workflows
* Tool Calling
* Conversation Memory
* Retrieval-Augmented Generation (RAG)
* Vector Databases
* Multi-Agent Systems
* Production Project Structure
* Snowflake Integration
* LLM Application Development
* Fraud Analytics
* Intent Classification

---

## Tech Stack

### AI Frameworks

* Python
* LangChain
* LangGraph

### LLM

* Google Gemini 2.5 Flash
* Gemini Embeddings

### Data Layer

* Snowflake Snowpark
* ChromaDB

### Utilities

* Pandas
* python-dotenv

---

## Banking Dataset

The project uses a simplified banking data warehouse stored in Snowflake.

### DIM_CUSTOMER

| Column      | Type   |
| ----------- | ------ |
| CUSTOMER_ID | TEXT   |
| FIRST_NAME  | TEXT   |
| LAST_NAME   | TEXT   |
| AGE         | NUMBER |
| COUNTRY     | TEXT   |

### DIM_ACCOUNT

| Column       | Type   |
| ------------ | ------ |
| ACCOUNT_ID   | TEXT   |
| CUSTOMER_ID  | TEXT   |
| ACCOUNT_TYPE | TEXT   |
| BALANCE      | NUMBER |

### DIM_MERCHANT

| Column        | Type   |
| ------------- | ------ |
| MERCHANT_ID   | TEXT   |
| MERCHANT_NAME | TEXT   |
| CATEGORY      | TEXT   |
| RISK_SCORE    | NUMBER |

### FACT_TRANSACTIONS

| Column         | Type   |
| -------------- | ------ |
| TRANSACTION_ID | TEXT   |
| CUSTOMER_ID    | TEXT   |
| ACCOUNT_ID     | TEXT   |
| MERCHANT_ID    | TEXT   |
| AMOUNT         | NUMBER |
| IS_FRAUD       | NUMBER |

---

## Current Features

### SQL Analytics

Example queries:

* Top customer
* Top merchant
* Customer with highest balance
* Merchant turnover
* Largest transactions

---

### Fraud Analysis

Example queries:

* Show high risk merchants
* Show suspicious transactions
* Show fraudulent transactions
* Show money laundering transactions

---

### Banking Knowledge Assistant

Example queries:

* What is money laundering?
* Explain AML.
* Define KYC.
* What is a high-risk merchant?

---

### Conversation Memory

Example:

User:

```text
top merchant
```

Assistant:

```text
Amazon
```

User:

```text
and its turnover
```

Assistant understands that:

```text
its = Amazon
```

without repeating context.

---

## System Architecture

```text
User
 │
 ▼
Manager Agent
 │
 ├──────────────┬──────────────┐
 │              │              │
 ▼              ▼              ▼
SQL Agent     RAG Agent     Fraud Agent
 │              │              │
 ▼              ▼              ▼
Snowflake     ChromaDB      Snowflake
 │              │              │
 └───────┬──────┴──────┬───────┘
         ▼
Conversation Memory
         ▼
    Final Response
```

---

## Project Structure

```text
banking-ai-assistant/
│
├── app.py
├── config.py
├── requirements.txt
├── .env
│
├── database/
│   └── snowflake.py
│
├── services/
│   └── llm_service.py
│
├── agents/
│   ├── manager_agent.py
│   ├── sql_agent.py
│   ├── rag_agent.py
│   └── fraud_agent.py
│
├── prompts/
│   ├── sql_prompt.txt
│   └── fraud_prompt.txt
│
├── embeddings/
│   └── embedding_service.py
│
├── chroma/
│   └── vector_store.py
│
├── graph/
│   ├── state.py
│   ├── nodes.py
│   └── workflow.py
│
└── future/
```

---

## Learning Roadmap

| Phase    | Status    | Concept                        |
| -------- | --------- | ------------------------------ |
| Phase 1  | Completed | Snowflake + Gemini Setup       |
| Phase 2  | Completed | SQL Generation                 |
| Phase 3  | Completed | SQL Execution                  |
| Phase 4  | Completed | Conversation Memory            |
| Phase 5  | Completed | Embeddings                     |
| Phase 6  | Completed | Chroma Vector Database         |
| Phase 7  | Completed | Retrieval-Augmented Generation |
| Phase 8  | Completed | Multi-Agent Architecture       |
| Phase 9  | Completed | Fraud Analysis Agent           |
| Phase 10 | Completed | LLM Intent Routing             |
| Phase 11 | Next      | Persistent Memory              |
| Phase 12 | Planned   | Hybrid Search                  |
| Phase 13 | Planned   | Tool Calling Agents            |
| Phase 14 | Planned   | Streamlit Dashboard            |
| Phase 15 | Planned   | Production Deployment          |

---

## Example Queries

### SQL

```text
top customer
top merchant
customer with highest balance
show all merchants
```

### Fraud

```text
show high risk merchants
show suspicious transactions
show money laundering transactions
show fraudulent transactions
```

### RAG

```text
what is money laundering
explain aml
define kyc
what is account compromise
```

---

## Future Enhancements

* Persistent vector memory
* Hybrid search (SQL + Vector Search)
* Tool Calling
* Human-in-the-loop workflows
* Multi-LLM support
* LangSmith Observability
* Authentication & RBAC
* REST API
* Streamlit Dashboard
* Docker Deployment
* CI/CD Pipeline
* Monitoring & Logging

---

## Learning Philosophy

This project follows a simple principle:

> Learn one production concept at a time and implement it immediately.

Every phase introduces exactly one new AI Engineering concept while preserving a runnable, production-style architecture.

---

## Repository Status

This project is actively under development and continuously evolving as new AI Engineering concepts are explored.
