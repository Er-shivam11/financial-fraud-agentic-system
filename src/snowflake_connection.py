from snowflake.snowpark import Session
import os
from dotenv import load_dotenv

print("🔍 Loading .env...")
load_dotenv()
print("✔ Loaded")

def get_snowpark_session():
    try:
        print("🔍 Fetching environment variables...")
        conn_params = {
            "account": os.getenv("SNOWFLAKE_ACCOUNT"),
            "user": os.getenv("SNOWFLAKE_USER"),
            "password": os.getenv("SNOWFLAKE_PASSWORD"),
            "warehouse": os.getenv("SNOWFLAKE_WAREHOUSE"),
            "role": os.getenv("SNOWFLAKE_ROLE"),
            "database": os.getenv("SNOWFLAKE_DATABASE"),
            "schema": os.getenv("SNOWFLAKE_SCHEMA"),
        }

        print("🔧 Connection parameters:", conn_params)

        session = Session.builder.configs(conn_params).create()
        print("✅ Snowpark Session created successfully!")
        return session

    except Exception as e:
        print("❌ Failed to create Snowpark session:", e)
        raise e


# 🔥 CALL THE FUNCTION
# get_snowpark_session()
