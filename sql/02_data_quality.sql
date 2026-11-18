-- 02_data_quality.sql
-- Data quality checks on the raw products table.

-- Duplicate check (replace product_id with the real key column)
-- SELECT product_id, COUNT(*) AS n
-- FROM products_raw
-- GROUP BY product_id
-- HAVING COUNT(*) > 1;

-- Null profile (repeat per column)
-- SELECT
--     SUM(CASE WHEN name IS NULL THEN 1 ELSE 0 END)  AS null_name,
--     SUM(CASE WHEN price IS NULL THEN 1 ELSE 0 END) AS null_price
-- FROM products_raw;
