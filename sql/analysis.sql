-- E-Commerce Sales Analytics - SQL Analysis
-- Database: ecommerce_sales
-- Table: sales

-- 1. Total Sales and Profit
SELECT
    SUM(Sales) AS total_sales,
    SUM(Profit) AS total_profit
FROM sales;

-- 2. Sales and Profit by Category
SELECT
    Category,
    SUM(Sales) AS total_sales,
    SUM(Profit) AS total_profit
FROM sales
GROUP BY Category
ORDER BY total_sales DESC;

-- 3. Sales and Profit by Sub-Category
SELECT
    `Sub-Category`,
    SUM(Sales) AS total_sales,
    SUM(Profit) AS total_profit
FROM sales
GROUP BY `Sub-Category`
ORDER BY total_sales DESC;

-- 4. Sales and Profit by Year
SELECT
    YEAR(`Order Date`) AS year,
    SUM(Sales) AS total_sales,
    SUM(Profit) AS total_profit
FROM sales
GROUP BY YEAR(`Order Date`)
ORDER BY year;

-- 5. Top 10 Products by Sales
SELECT
    `Product Name`,
    SUM(Sales) AS total_sales,
    SUM(Profit) AS total_profit
FROM sales
GROUP BY `Product Name`
ORDER BY total_sales DESC
LIMIT 10;


