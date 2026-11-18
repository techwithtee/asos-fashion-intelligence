-- 01_exploration.sql
-- First look at the raw products table.

-- Row count
SELECT COUNT(*) AS total_rows FROM products_raw;

-- Sample rows
SELECT TOP 20 * FROM products_raw;

-- Column names and types
SELECT COLUMN_NAME, DATA_TYPE, IS_NULLABLE
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'products_raw'
ORDER BY ORDINAL_POSITION;
