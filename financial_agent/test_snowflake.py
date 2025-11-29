# test_snowflake.py
from snowflake_tool import query_snowflake

# Example SQL query
sql_query = """
SELECT *
FROM gold.dim_customer
LIMIT 5
"""

# Run the query and get results
result = query_snowflake(sql_query)

print("=== Snowflake Query Result ===")
print(result)
