import snowflake.connector
import glob
import os
from dotenv import load_dotenv

load_dotenv()

USER = os.getenv("SNOWFLAKE_USER")
PWD = os.getenv("SNOWFLAKE_PASSWORD")
ACC = os.getenv("SNOWFLAKE_ACCOUNT")
WH = os.getenv("SNOWFLAKE_WAREHOUSE")
DB = os.getenv("SNOWFLAKE_DATABASE")
ROLE = os.getenv("SNOWFLAKE_ROLE")

TARGET_SCHEMA = "SILVER"

print("🔍 Connecting to Snowflake...")

conn = snowflake.connector.connect(
    user=USER,
    password=PWD,
    account=ACC,
    warehouse=WH,
    database=DB,
    role=ROLE
)

cursor = conn.cursor()
print("✅ Connected successfully!")
print("--------------------------------------------------")

cursor.execute(f"USE SCHEMA {DB}.{TARGET_SCHEMA};")

print("📌 CURRENT DB & SCHEMA:", cursor.execute("SELECT CURRENT_DATABASE(), CURRENT_SCHEMA()").fetchall())
print("--------------------------------------------------")

sql_files = sorted(glob.glob("./silver/*.sql"))
print(f"📄 Found {len(sql_files)} SQL files:")

if not sql_files:
    print("❌ No SQL files found!")
else:
    for sql_file in sql_files:
        print(f"📄 Running: {sql_file}")

        try:
            # 🔹 FIX 1: Force UTF-8 encoding
            with open(sql_file, "r", encoding="utf-8") as f:
                query = f.read()

            # 🔹 FIX 2: Prevent multiple statements error
            for stmt in query.split(";"):
                stmt = stmt.strip()
                if stmt:
                    cursor.execute(stmt)

            print(f"   ✔ Success: {sql_file}\n")

        except Exception as e:
            print(f"   ❌ Error in {sql_file}: {e}\n")

conn.commit()
print("🎉 Silver layer built successfully!")

cursor.close()
conn.close()
print("🔒 Connection closed.")
