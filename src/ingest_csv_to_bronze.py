# src/ingest_csv_to_bronze.py
import os
import csv
from snowflake.snowpark import Session
from dotenv import load_dotenv

load_dotenv()

# ----------------------------------------------------------------------
# 1. CREATE SNOWFLAKE SESSION
# ----------------------------------------------------------------------
def create_snowflake_session():
    connection_params = {
        "account": os.getenv("SNOWFLAKE_ACCOUNT"),
        "user": os.getenv("SNOWFLAKE_USER"),
        "password": os.getenv("SNOWFLAKE_PASSWORD"),
        "warehouse": os.getenv("SNOWFLAKE_WAREHOUSE"),
        "database": os.getenv("SNOWFLAKE_DATABASE"),
        "schema": "BRONZE"
    }

    session = Session.builder.configs(connection_params).create()
    print("✅ Snowpark Session created\n")
    return session


# ----------------------------------------------------------------------
# 2. READ HEADER FROM LOCAL CSV
# ----------------------------------------------------------------------
def extract_header(local_path):
    with open(local_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)  # First row → column names
    return header


# ----------------------------------------------------------------------
# 3. INGEST CSV → STAGE → READ → APPLY HEADER → SAVE TO BRONZE
# ----------------------------------------------------------------------
def load_csv_to_bronze(session, local_path, table_name, stage_name="BRONZE_STAGE"):
    if not os.path.exists(local_path):
        print(f"❌ Local file not found: {local_path}")
        return False

    print(f"\n📌 Ingesting {local_path} → BRONZE.{table_name}")

    # read header locally
    try:
        header = extract_header(local_path)
    except Exception as e:
        print("❌ Failed to read header locally:", e)
        return False

    expected_cols = len(header)
    print(f"🧠 Detected columns: {header}")

    # upload file to stage
    try:
        print(f"📤 Uploading {local_path} to @{stage_name} (overwrite=True)")
        session.file.put(local_path, f"@{stage_name}", auto_compress=False, overwrite=True)
        print("✅ Upload complete")
    except Exception as e:
        print("❌ Error uploading file to stage:", e)
        return False

    # debug: list stage contents (helps ensure right file present)
    try:
        print(f"📋 Listing files in @{stage_name}:")
        res = session.sql(f"LIST @{stage_name}").collect()
        for r in res:
            # r[0] is file name, printing concise info
            print("  -", r[0])
    except Exception as e:
        print("⚠️ Could not list stage contents:", e)

    # read only the uploaded file (use base name)
    staged_file = f"@{stage_name}/{os.path.basename(local_path)}"
    print(f"📖 Reading staged file: {staged_file}")

    try:
        df = session.read.option("skip_header", 1).csv(staged_file)
        print("✅ Read CSV from stage")
    except Exception as e:
        print("❌ Error reading CSV from stage:", e)
        return False

    # fix column mismatch if needed
    actual_cols = len(df.schema.fields)
    if actual_cols > expected_cols:
        print(f"⚠️ Extra columns detected (inferred {actual_cols} > expected {expected_cols}) — trimming")
        df = df.select(df.columns[:expected_cols])
    elif actual_cols < expected_cols:
        print(f"❌ Column count mismatch: CSV header {expected_cols} vs inferred {actual_cols}")
        return False

    # apply header names
    try:
        df = df.to_df(*header)
        print("🔧 Applied correct column names")
    except Exception as e:
        print("❌ Error applying column names:", e)
        return False

    # drop table if exists (safe)
    try:
        session.sql(f"DROP TABLE IF EXISTS BRONZE.{table_name}").collect()
        print(f"🗑️ Dropped existing table if it existed: BRONZE.{table_name}")
    except Exception as e:
        print("⚠️ Could not drop table (continuing):", e)

    # save as table
    try:
        df.write.mode("overwrite").save_as_table(f"BRONZE.{table_name}")
        print(f"🧱 Saved to BRONZE.{table_name}")
        return True
    except Exception as e:
        print("❌ Error writing to table:", e)
        return False


# ----------------------------------------------------------------------
# 4. MAIN
# ----------------------------------------------------------------------
def main():
    session = None
    try:
        session = create_snowflake_session()
    except Exception as e:
        print("❌ Failed to create session, aborting:", e)
        return

    files = {
        "CUSTOMERS": "data/customers.csv",
        "ACCOUNTS": "data/accounts.csv",
        "TRANSACTIONS": "data/transactions.csv",
        "ALERTS_HISTORY": "data/alerts_history.csv",
        "MERCHANT_INFO": "data/merchant_info.csv",
        "FRAUD_LABELS": "data/fraud_labels.csv",
    }

    success = {}
    for table, path in files.items():
        ok = load_csv_to_bronze(session, path, table)
        success[table] = ok

    print("\n📊 Ingestion summary:")
    for t, s in success.items():
        print(f" - {t}: {'OK' if s else 'FAILED'}")

    # close session
    try:
        session.close()
    except Exception:
        pass


if __name__ == "__main__":
    main()
