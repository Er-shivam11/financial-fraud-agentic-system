
  CREATE OR REPLACE TABLE silver.merchant_info AS
WITH cleaned AS (

    SELECT
        -- Standardize text fields
        UPPER(TRIM(merchant_id))              AS merchant_id,
        INITCAP(TRIM(merchant_name))          AS merchant_name,
        INITCAP(TRIM(category))               AS category,
        INITCAP(TRIM(country))                AS country,

        -- Cast numeric fields
        TRY_CAST(risk_score AS INTEGER)       AS risk_score,

        -- Metadata columns
        CURRENT_TIMESTAMP()                   AS load_timestamp

    FROM bronze.merchant_info
),

-- Remove duplicates (prefer latest load if present)
deduped AS (
    SELECT
        *,
        ROW_NUMBER() OVER (PARTITION BY merchant_id ORDER BY load_timestamp DESC) AS rn
    FROM cleaned
)

SELECT
    merchant_id,
    merchant_name,
    category,
    country,
    risk_score,
    load_timestamp
FROM deduped
WHERE rn = 1;