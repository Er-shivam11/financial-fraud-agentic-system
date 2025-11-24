
CREATE OR REPLACE TABLE silver.alerts_history AS
WITH cleaned AS (
    SELECT
        -- Standardize IDs
        UPPER(TRIM(alert_id))     AS alert_id,
        UPPER(TRIM(customer_id))  AS customer_id,
        UPPER(TRIM(txn_id))       AS txn_id,

        -- Proper-case alert types
        INITCAP(TRIM(alert_type)) AS alert_type,

        -- Normalize status
        CASE 
            WHEN LOWER(TRIM(status)) = 'open'   THEN 'OPEN'
            WHEN LOWER(TRIM(status)) = 'closed' THEN 'CLOSED'
            ELSE 'UNKNOWN'
        END AS status,

        -- Already valid timestamp
        created_at,

        CURRENT_TIMESTAMP() AS load_timestamp

    FROM bronze.alerts_history
    WHERE alert_id IS NOT NULL
),

deduped AS (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY alert_id ORDER BY load_timestamp DESC) AS rn
    FROM cleaned
)

SELECT
    alert_id,
    customer_id,
    txn_id,
    alert_type,
    status,
    created_at,
    load_timestamp
FROM deduped
WHERE rn = 1;