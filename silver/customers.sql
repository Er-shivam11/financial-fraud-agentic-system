-- Create Silver table if not exists
CREATE OR REPLACE TABLE SILVER.CUSTOMERS AS
SELECT
    CUSTOMER_ID,
    FIRST_NAME,
    LAST_NAME,

    -- AGE kept as is
    AGE,

    -- Gender imputed: NULL → 'O'
    COALESCE(GENDER, 'O') AS GENDER,

    -- Country kept but NULL → 'Unknown' (optional best practice)
    COALESCE(COUNTRY, 'Unknown') AS COUNTRY,

    -- Signup date must not be NULL (those rows removed)
    SIGNUP_DATE,

    -- Add metadata columns
    CURRENT_TIMESTAMP() AS LOAD_TS,
    'BRONZE' AS SOURCE_LAYER

FROM BRONZE.CUSTOMERS

-- ❌ Remove unusable rows
WHERE CUSTOMER_ID IS NOT NULL
  AND FIRST_NAME IS NOT NULL
  AND LAST_NAME IS NOT NULL
  AND SIGNUP_DATE IS NOT NULL;
