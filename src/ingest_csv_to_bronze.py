import os
from snowflake.snowpark import Session
from dotenv import load_dotenv

load_dotenv()

# ------------------------------------------------------------------------------
# 1. SNOWFLAKE CONNECTION
# ------------------------------------------------------------------------------
def create_snowflake_session():
    try:
        connection_params = {
            "account": os.getenv("SNOWFLAKE_ACCOUNT"),
            "user": os.getenv("SNOWFLAKE_USER"),
            "password": os.getenv("SNOWFLAKE_PASSWORD"),
            "warehouse": os.getenv("SNOWFLAKE_WAREHOUSE"),
            "database": os.getenv("SNOWFLAKE_DATABASE"),
            "schema": "BRONZE"
        }

        session = Session.builder.configs(connection_params).create()
        print("✅ Snowpark Session created successfully\n")
        return session

    except Exception as e:
        print("❌ Error creating Snowflake session:", e)
        raise


# ------------------------------------------------------------------------------
# 2. INGEST FUNCTION: LOCAL CSV → STAGE → BRONZE TABLE
# ------------------------------------------------------------------------------
def load_csv_to_bronze(session, local_path, table_name):
    stage_name = "BRONZE_STAGE"

    # Validate local file
    if not os.path.exists(local_path):
        print(f"❌ Local file not found: {local_path}")
        return

    print(f"📌 Ingesting {local_path} → BRONZE.{table_name}")

    # 1. Upload to stage --------------------------------------------------------
    try:
        session.file.put(
            local_path,
            f"@{stage_name}",
            auto_compress=False,
            overwrite=True
        )
        print(f"📤 Uploaded to @{stage_name}")
    except Exception as e:
        print("❌ Error uploading file:", e)
        return

    # 2. Read from stage --------------------------------------------------------
    try:
        df = session.read.option("skip_header", 1).csv(f"@{stage_name}")
        print("📖 CSV read from stage")
    except Exception as e:
        print("❌ Error reading CSV from stage:", e)
        return

    # 3. Write to Bronze table --------------------------------------------------
    try:
        df.write.mode("overwrite").save_as_table(f"BRONZE.{table_name}")
        print(f"🧱 Saved to BRONZE.{table_name}\n")
    except Exception as e:
        print("❌ Error writing to table:", e)
        return


# ------------------------------------------------------------------------------
# 3. MAIN EXECUTOR
# ------------------------------------------------------------------------------
def main():
    session = create_snowflake_session()

    data_files = {
        "CUSTOMERS": "data/customers.csv",
        "ACCOUNTS": "data/accounts.csv",
        "TRANSACTIONS": "data/transactions.csv",
        "ALERTS_HISTORY": "data/alerts_history.csv",
        "MERCHANT_INFO": "data/merchant_info.csv",
        "FRAUD_LABELS": "data/fraud_labels.csv"
    }

    for table, path in data_files.items():
        load_csv_to_bronze(session, path, table)


if __name__ == "__main__":
    main()
