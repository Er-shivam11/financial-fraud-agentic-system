# 🚀 Financial Fraud Agentic System

A full-stack **agentic, multi-service** pipeline for Fraud Detection, AML/KYC Compliance, Transaction Risk Scoring, and automated ML.
This system integrates **Snowflake**, **Python**, **Streamlit**, **FastAPI**, **Agents**, **ML**, and **Docker** into one production-ready architecture.

---

# 📁 Project Structure

```
financial-fraud-agentic-system/
│
├── data/                       # Raw CSV datasets
│   ├── customers.csv
│   ├── accounts.csv
│   ├── merchant_info.csv
│   ├── transactions.csv
│   ├── fraud_labels.csv
│   └── alerts_history.csv
│
├── src/
│   │   ├── ingest_csv_to_bronze.py
│       ├── snowflake_connection.py
│       ├── run_silver_pipeline.py
│       ├── run_gold_pipeline.py
│   
├── silver/
│     ├── customers.sql
│     ├── accounts.sql
│     ├── merchant_info.sql
│     ├── transactions.sql
│     ├── fraud_labels.sql
│     └── alerts_history.sql
│   
│
├── models/
│     ├── dim_customers.sql
│     ├── dim_accounts.sql
│     ├── dim_merchant_info.sql
│     ├── fact_transactions.sql
│
├── agents/                     # AI Agents (future modules)
│   ├── profiler_agent.py
│   ├── automl_agent.py
│   ├── fraud_agent.py
│   ├── risk_agent.py
│   └── aml_agent.py
│
├── ml/
│   ├── train_model.py
│   ├── feature_store.py
│   └── model_registry/
│
├── api/
│   ├── fastapi_app.py
│   └── endpoints/
│
├── streamlit/
│   ├── dashboard.py
│   └── insights/
│
├── docker/
│   ├── Dockerfile.api
│   ├── Dockerfile.streamlit
│   └── docker-compose.yml
│
├── .env│
├── README.md
├── .gitignore
└── requirements.txt
```

---

# 🎯 Project Goals

This system enables:

### ✅ Automated ingestion → transformation → feature engineering → ML → agents

### ✅ Real-time fraud detection

### ✅ AML/KYC compliance checks

### ✅ Risk scoring + alert explanations

### ✅ Streamlit insights + API services

### ✅ Docker microservices for deployment

---

# 🏗 Current Progress (Completed)

### ✔ **1. Data Preparation**

* All raw datasets ready in `/data`.

### ✔ **2. Snowflake Connectivity**

`src/utils/snowflake_connection.py` manages:

* Session creation
* Automatic environment loading
* Safe connection handling

### ✔ **3. Bronze Ingestion Layer**

`src/ingest/ingest_csv_to_bronze.py` supports:

* Upload CSV → Snowflake Stage
* Auto schema detection
* Auto Bronze table creation
* Load data into `BRONZE` schema

---

# 🚧 Upcoming Development (next phases)

### 🔜 **SILVER Layer**

* Data cleaning
* Normalization
* Deduplication
* Data validation rules

### 🔜 **GOLD Layer**

* Feature engineering
* Aggregates
* Customer risk profiles
* Fraud score features

### 🔜 **Agentic AI Layer**

* Profiler Agent → identifies fraud type
* AutoML Agent → trains & selects best model
* Fraud Agent → real-time predictions
* AML Agent → compliance rule checks
* Risk Agent → scoring & explanations

### 🔜 **ML Layer**

* Feature store
* Model registry
* Incremental training

### 🔜 **API Layer**

* FastAPI service
* Endpoints for predictions & alerts

### 🔜 **Streamlit Dashboard**

* Fraud alerts
* Visualization
* Agent chat panel

### 🔜 **Docker Deployment**

* Streamlit container
* API container
* Orchestration using docker-compose

---

# 🔧 Installation

### **1️⃣ Create virtual environment**

```
python -m venv .venv
```

### **2️⃣ Activate**

PowerShell:

```
.venv\Scripts\activate
```

### **3️⃣ Install dependencies**

```
pip install -r requirements.txt
```

---

# 🔐 Environment Setup

Create your own `.env` (not committed):

```
SNOWFLAKE_USER=
SNOWFLAKE_PASSWORD=
SNOWFLAKE_ACCOUNT=
SNOWFLAKE_ROLE=
SNOWFLAKE_WAREHOUSE=
SNOWFLAKE_DATABASE=
SNOWFLAKE_SCHEMA=
SNOWFLAKE_STAGE=
```

---

# ▶ Running Bronze Ingestion

From project root:

```
python src/ingest/ingest_csv_to_bronze.py
```

---

# 🤝 Contributing

Open issues or PRs anytime.

---

# 📜 License

MIT License.

