# **AI Multi-Agent Financial Fraud & Compliance Automation System**

*A Production-Ready Multi-Agent System for Financial Insights, Fraud Detection & Explainable Compliance Analysis*

---

## 🚀 **Overview**

Financial institutions generate massive amounts of customer, account, and transaction data. Yet, analysts still rely on manual lookups or static dashboards to answer basic operational queries.

This project solves that problem.

**AI Multi-Agent Financial Fraud & Compliance Automation System** is a fully functional, production-style multi-agent architecture built using:

* **Google ADK (Agent Developer Kit)**
* **Gemini 2.5 Flash Lite**
* **Streamlit Dashboard**
* **Tool-Augmented Reasoning**
* **Real-time Structured Data Retrieval**

It allows users to ask natural language questions such as:

* *“Show me the balance for Account A1001”*
* *“Find suspicious merchants for Indian customers”*
* *“Summarize fraud alerts for this month”*

…and get structured tables + clean explanations instantly.

---

## 🎯 **Key Features**

### **AI Multi-Agent Architecture**

✔ **FinancialOpsAgent**
Retrieves customer details, account balances, and transaction history.

✔ **FraudRiskAgent**
Identifies suspicious merchants and explains fraud risks.

✔ **UnifiedSupportAgent (Orchestrator)**
Routes queries, combines outputs, and returns final explanations.

---

### **Real-Time Structured Financial Insights**

* Natural language → **tool calls**
* Simulated Snowflake-like data lookup
* Schema-aware structured responses
* Works with customer, account, merchant & transaction metadata

---

### **Fraud Detection**

* Merchant risk evaluation
* Suspicious transaction lookup
* Clear human-readable fraud summaries

---

### **Explainable AI**

* Transparent reasoning
* Clear steps
* Tool-call traces via ADK runner
* Narrative summaries + DataFrames

---

### **Fully Interactive Streamlit UI**

✔ Input queries
✔ View structured tables
✔ Read agent summary
✔ View history of previous queries
✔ ADK event-based debugging

---

## 📦 **Project Structure**

```
financial-fraud-agentic-system/
│
├── main.py
├── README.md
├── requirements.txt
│
├── streamlit_app/
│   ├── app.py
│
├── financial_agent/
│   ├── __init__.py
│   ├── agent.py
│   ├── fraud_agent.py
│   ├── snowflake_tool.py
│   ├── .env
│
└── .venv/
```

---

## 🧠 **System Architecture**

### **1. Data Layer (Simulated Snowflake)**

Tools for data retrieval:

* `get_customer_info`
* `get_account_balance`
* `get_transaction_info`
* `get_merchant_risk`

These mock Snowflake queries while keeping the project lightweight.

---

### **2. Multi-Agent Layer**

#### **FinancialOpsAgent**

* Customer lookup
* Account balances
* Transaction data

#### **FraudRiskAgent**

* Merchant risk scores
* Suspicious transaction detection
* Fraud explanation generation

#### **UnifiedSupportAgent**

* Orchestrates both agents
* Handles complex cross-domain queries
* Generates combined summaries

---

### **3. Frontend Layer (Streamlit UI)**

* Natural language query input
* Table rendering
* Narrative summary
* Async execution
* History tracking

---

## 🛠️ **Tech Stack**

| Component       | Technology            |
| --------------- | --------------------- |
| AI Models       | Gemini 2.5 Flash Lite |
| Agent Framework | Google ADK            |
| UI              | Streamlit             |
| Dataframes      | Pandas                |
| Environment     | Python + dotenv       |

---

## ▶️ **How to Run Locally**

### **1. Create Environment**

```bash
pip install -r requirements.txt
```

### **2. Start ADK Agent Backend**

```bash
adk web --port 9001
```

### **3. Start Streamlit App**

```bash
streamlit run streamlit_app/app.py
```

---

## 🧪 **Test Queries (main.py)**

```python
tests = [
    "find fraud alerts for indian customers",
    "show total balance by account type",
    "which merchants are most risky",
    "generate summary report for all customers"
]
```

Run with:

```bash
python main.py
```

---

## 📈 **Example Use Cases**

* Fraud Operations
* Compliance Monitoring
* Customer Support Automation
* Merchant Risk Screening
* Analyst Data Lookup

---

## 🔍 **Sample Query Flow**

**User:**
“Find fraud alerts for Indian customers”

**UnifiedSupportAgent:**
→ FinancialOpsAgent → fetch customer + transactions
→ FraudRiskAgent → evaluate merchant risk
→ Combine + summarize

**Output:**

* Structured Pandas table
* Fraud explanation
* Merchant risk breakdown

---

## 🧬 **Retry Logic, Robustness & Observability**

* Exponential backoff
* 5 retry attempts
* HTTP failure resistance
* Tool-call traceability
* ADK event-level debugging

---

## 📌 **Future Enhancements**

* Real Snowflake integration
* Advanced graph-based fraud detection
* Real-time streaming alerts
* Multi-language customer query support
* Role-based access (RBAC)

---

## 🏁 **Conclusion**

This system demonstrates:

* How AI agents can automate financial operations
* How multi-agent routing reduces manual workload
* How LLMs + structured tools generate **reliable, explainable results**
* How a complete agent ecosystem can be built using Google ADK

It is a **practical, extensible prototype** suitable for banking, fintech, fraud analytics, and compliance teams.