import os
from dotenv import load_dotenv
from snowflake.snowpark import Session

# Load environment variables
load_dotenv()


def get_session():
    """Create and return a Snowflake Snowpark session."""
    conn = {
        "account": os.getenv("SNOWFLAKE_ACCOUNT"),
        "user": os.getenv("SNOWFLAKE_USER"),
        "password": os.getenv("SNOWFLAKE_PASSWORD"),
        "warehouse": os.getenv("SNOWFLAKE_WAREHOUSE"),
        "role": os.getenv("SNOWFLAKE_ROLE"),
        "database": os.getenv("SNOWFLAKE_DATABASE"),
        "schema": os.getenv("SNOWFLAKE_SCHEMA"),
    }

    missing = [key for key, value in conn.items() if not value]
    if missing:
        raise ValueError(f"Missing environment variables: {missing}")

    return Session.builder.configs(conn).create()


def main():
    session = get_session()
    print("Connected to Snowflake successfully!")

    try:
        # Read tables from Snowflake
        dim_customer = session.table("DIM_CUSTOMER")
        dim_account = session.table("DIM_ACCOUNT")
        dim_merchant = session.table("DIM_MERCHANT")
        fact_transactions = session.table("FACT_TRANSACTIONS")

        print("\n=== DIM_CUSTOMER ===")
        dim_customer.show()

        print("\n=== DIM_ACCOUNT ===")
        dim_account.show()

        print("\n=== DIM_MERCHANT ===")
        dim_merchant.show()

        print("\n=== FACT_TRANSACTIONS ===")
        fact_transactions.show()

    finally:
        session.close()
        print("\nSnowflake session closed.")


if __name__ == "__main__":
    main()