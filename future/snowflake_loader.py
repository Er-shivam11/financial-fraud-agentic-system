# import os
# import pandas as pd
# from snowflake.snowpark import Session
# from dotenv import load_dotenv

# load_dotenv() 
# # 1. Establish the session using your structure
# def get_session():
#     conn = {
#         "account": os.getenv("SNOWFLAKE_ACCOUNT"),
#         "user": os.getenv("SNOWFLAKE_USER"),
#         "password": os.getenv("SNOWFLAKE_PASSWORD"),
#         "warehouse": os.getenv("SNOWFLAKE_WAREHOUSE"),
#         "role": os.getenv("SNOWFLAKE_ROLE"),
#         "database": os.getenv("SNOWFLAKE_DATABASE"),
#         "schema": os.getenv("SNOWFLAKE_SCHEMA"),
#     }
#     print(conn)
#     return Session.builder.configs(conn).create()

# # 2. Raw data structures mapping keys to column rows
# data_dict = {
#     "DIM_ACCOUNT": ("ACCOUNT_ID", {
#         "A1001": {"CUSTOMER_ID": "C001", "ACCOUNT_TYPE": "SAVINGS", "BALANCE": 45000},
#         "A1002": {"CUSTOMER_ID": "C002", "ACCOUNT_TYPE": "CURRENT", "BALANCE": 78000},
#         "A1003": {"CUSTOMER_ID": "C003", "ACCOUNT_TYPE": "SAVINGS", "BALANCE": 52000},
#         "A1004": {"CUSTOMER_ID": "C004", "ACCOUNT_TYPE": "CURRENT", "BALANCE": 0},
#         "A1005": {"CUSTOMER_ID": "C005", "ACCOUNT_TYPE": "SAVINGS", "BALANCE": 31000},
#     }),
#     "DIM_CUSTOMER": ("CUSTOMER_ID", {
#         "C001": {"FIRST_NAME": "Arjun", "LAST_NAME": "Mehta", "AGE": 29, "COUNTRY": "India"},
#         "C002": {"FIRST_NAME": "Neha", "LAST_NAME": "Sharma", "AGE": 33, "COUNTRY": "India"},
#         "C003": {"FIRST_NAME": "Rahul", "LAST_NAME": "Kumar", "AGE": None, "COUNTRY": "India"},
#         "C004": {"FIRST_NAME": "Anita", "LAST_NAME": "Gupta", "AGE": 41, "COUNTRY": "Unknown"},
#     }),
#     "DIM_MERCHANT": ("MERCHANT_ID", {
#         "M001": {"MERCHANT_NAME": "Flipkart", "CATEGORY": "E-Commerce", "RISK_SCORE": 30},
#         "M002": {"MERCHANT_NAME": "Amazon", "CATEGORY": "E-Commerce", "RISK_SCORE": 25},
#         "M003": {"MERCHANT_NAME": "Walmart", "CATEGORY": "Retail", "RISK_SCORE": 40},
#     }),
#     "FACT_TRANSACTIONS": ("TRANSACTION_ID", {
#         "T1001": {"CUSTOMER_ID": "C001", "ACCOUNT_ID": "A1001", "MERCHANT_ID": "M001", "AMOUNT": 5000, "IS_FRAUD": 0},
#         "T1002": {"CUSTOMER_ID": "C002", "ACCOUNT_ID": "A1002", "MERCHANT_ID": "M002", "AMOUNT": 7000, "IS_FRAUD": 1},
#     })
# }

# def upload_data():
#     # Initialize the Snowpark session
#     session = get_session()
#     print("Connected securely to Snowflake!")

#     try:
#         for table_name, (id_col, rows) in data_dict.items():
#             # Standardize structural records for Pandas DataFrame loading
#             records = []
#             for key, inner_dict in rows.items():
#                 row_data = {id_col: key}
#                 row_data.update(inner_dict)
#                 records.append(row_data)
            
#             # Convert raw python structures into standard DataFrames
#             df = pd.DataFrame(records)
            
#             # Convert DataFrame columns to uppercase to align with Snowflake standards
#             df.columns = [col.upper() for col in df.columns]

#             # Build and write the Snowpark DataFrame directly to Snowflake targets
#             snowpark_df = session.create_dataframe(df)
            
#             # mode="overwrite" drops and recreates the target table automatically
#             snowpark_df.write.mode("overwrite").save_as_table(table_name)
#             print(f"Successfully processed and uploaded table: {table_name}")

#     finally:
#         # Ensure session resources are gracefully closed out
#         session.close()
#         print("Snowflake session disconnected cleanly.")

# if __name__ == "__main__":
#     upload_data()
