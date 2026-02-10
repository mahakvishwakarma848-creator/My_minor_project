-- 1. Database
CREATE DATABASE IF NOT EXISTS realtime_db;
USE realtime_db;

-- 2. Table
CREATE TABLE IF NOT EXISTS sales_data (
    order_id INT,
    order_time DATETIME,
    product VARCHAR(100),
    category VARCHAR(50),
    quantity INT,
    price FLOAT,
    city VARCHAR(50),
    payment_mode VARCHAR(20)
);

-- 3. Total Revenue
SELECT SUM(quantity * price) AS total_revenue
FROM sales_data;

-- 4. Total Orders
SELECT COUNT(order_id) AS total_orders
FROM sales_data;

-- 5. Revenue by City
SELECT city, SUM(quantity * price) AS revenue
FROM sales_data
GROUP BY city;

-- 6. Top Selling Products
SELECT product, SUM(quantity) AS total_quantity
FROM sales_data
GROUP BY product
ORDER BY total_quantity DESC;

-- 7. Payment Mode Analysis
SELECT payment_mode, COUNT(*) AS total_transactions
FROM sales_data
GROUP BY payment_mode;

-- 8. Daily Sales Trend
SELECT DATE(order_time) AS order_date,
       SUM(quantity * price) AS daily_sales
FROM sales_data
GROUP BY DATE(order_time)
ORDER BY order_date;
