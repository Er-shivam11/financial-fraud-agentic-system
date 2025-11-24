
CREATE OR REPLACE TABLE silver.fraud_labels AS
WITH cleaned AS (

    SELECT
        -- Standardize txn_id
        UPPER(TRIM(txn_id)) AS txn_id,

        -- Ensure fraud flag is numeric and only 0 or 1
        CASE 
            WHEN TRY_TO_NUMBER(is_fraud) IN (0,1)
                THEN TRY_TO_NUMBER(is_fraud)
            ELSE 0   -- default safe value
        END AS is_fraud,

        CURRENT_TIMESTAMP() AS load_timestamp
    FROM bronze.fraud_labels
    WHERE txn_id IS NOT NULL
),

deduped AS (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY txn_id ORDER BY load_timestamp DESC) AS rn
    FROM cleaned
)

SELECT txn_id, is_fraud, load_timestamp
FROM deduped
WHERE rn = 1;