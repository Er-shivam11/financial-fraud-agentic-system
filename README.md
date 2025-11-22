# 📦 Financial Fraud Agentic System

End-to-end data engineering pipeline for ingesting raw CSV data into Snowflake using **stages**, **Snowpark**, and a **Bronze layer**.
This repository currently implements the **Bronze Ingestion Layer** with automatic schema detection and table creation.

---

## 🚀 **Project Overview**

This project aims to build a modular, scalable data pipeline for financial-fraud analytics and AI agentic workflows.

### **Current Milestone Completed**

✔ Snowflake project setup
✔ Local `.env` integration
✔ Internal stage creation
✔ CSV upload to Snowflake stage
✔ Automatic schema inference from CSV
✔ Automatic Bronze table creation
✔ Data loading into Bronze tables
✔ Modular folder structure

---

# 📁 **Folder Structure (Current Version)**

```
financial-fraud-agentic-system/
│
├── config/
│   └── config.py                # Loads Snowflake credentials from .env
│
├── ingestion/
│   └── ingest_csv_to_bronze.py  # Full working ingestion script
│
├── data/
│   └── raw/                     # Local CSV files before ingestion
│
├── .env                         # Snowflake credentials (not committed)
├── .gitignore                   # Python + env + cache ignores
├── README.md                    # Project documentation
└── requirements.txt             # Dependencies
```

---

# 🔧 **Bronze Ingestion Script**

### **Script:**

`ingestion/ingest_csv_to_bronze.py`

### **What it does:**

1. Reads Snowflake credentials from `.env`
2. Connects to Snowflake using **SnowparkSession**
3. Uploads CSV to stage (e.g., `@raw_stage`)
4. Infers schema from CSV header
5. Creates Bronze table automatically (if not exists)
6. Loads data into:

```
bronze.<auto_table_name_from_csv>
```

### **Command to Run**

From project root (`financial-fraud-agentic-system/`):

```
python ingestion/ingest_csv_to_bronze.py
```

---

# 🔐 Environment Variables

Create a file named **.env** in the root:

```
SNOWFLAKE_USER=your_user
SNOWFLAKE_PASSWORD=your_password
SNOWFLAKE_ACCOUNT=your_account
SNOWFLAKE_ROLE=your_role
SNOWFLAKE_WAREHOUSE=your_wh
SNOWFLAKE_DATABASE=your_db
SNOWFLAKE_SCHEMA=bronze
SNOWFLAKE_STAGE=raw_stage
```

> `.env` is already ignored by `.gitignore`.

---

# 📦 Installation

### 1️⃣ Create virtual environment

```
python -m venv .venv
```

### 2️⃣ Activate it

PowerShell:

```
.venv\Scripts\activate
```

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

# 📌 Features Completed (Bronze Layer)

| Feature                      | Status |
| ---------------------------- | ------ |
| Snowpark session setup       | ✅ Done |
| CSV → Snowflake stage upload | ✅ Done |
| Auto schema inference        | ✅ Done |
| Auto table creation          | ✅ Done |
| Load CSV → Bronze table      | ✅ Done |
| Config modularization        | ✅ Done |

---

# 🛠 Upcoming (Future Roadmap)

✔ Silver layer transformation scripts
✔ Gold layer transformation scripts
✔ CI/CD (GitHub Actions)
✔ Streamlit dashboard
✔ Agentic Fraud Detection models
✔ Orchestration (Airflow / Prefect)

---

# 🤝 Contributing

Feel free to open issues or submit pull requests as the project grows.

---

# 📜 License

MIT License.

