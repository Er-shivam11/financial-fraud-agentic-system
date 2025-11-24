
CREATE OR REPLACE TABLE silver.transactions AS
WITH cleaned AS (

    SELECT
        -- Standardize IDs
        UPPER(TRIM(txn_id))         AS txn_id,
        UPPER(TRIM(customer_id))    AS customer_id,
        UPPER(TRIM(account_id))     AS account_id,
        UPPER(TRIM(merchant_id))    AS merchant_id,
        UPPER(TRIM(timestamp))    AS timestamp,

        -- Amount numeric cleanup
        TRY_TO_NUMBER(amount)       AS amount,

        -- Location formatting
        INITCAP(TRIM(location))     AS location,

        CURRENT_TIMESTAMP()         AS load_timestamp

    FROM bronze.transactions
),

deduped AS (
    SELECT
        *,
        ROW_NUMBER() OVER (PARTITION BY txn_id ORDER BY load_timestamp DESC) AS rn
    FROM cleaned
)

SELECT
    txn_id,
    customer_id,
    account_id,
    merchant_id,
    amount,
    timestamp,
    location,
    load_timestamp
FROM deduped
WHERE rn = 1;