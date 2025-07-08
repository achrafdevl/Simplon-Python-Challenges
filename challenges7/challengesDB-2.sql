-- CREATE TABLE customers (
--     customer_id SERIAL PRIMARY KEY,
--     first_name VARCHAR(50),
--     last_name VARCHAR(50),
--     email VARCHAR(100),
--     phone_number VARCHAR(20)
-- );

-- CREATE TABLE products (
--     product_id SERIAL PRIMARY KEY,
--     name VARCHAR(100),
--     price NUMERIC(10, 2),
--     category VARCHAR(50)
-- );

-- CREATE TABLE orders (
--     order_id SERIAL PRIMARY KEY,
--     customer_id INTEGER REFERENCES customers(customer_id) ON DELETE CASCADE,
--     order_date DATE,
--     total_amount NUMERIC(10, 2)
-- );

-- CREATE TABLE order_items (
--     item_id SERIAL PRIMARY KEY,
--     order_id INTEGER REFERENCES orders(order_id) ON DELETE CASCADE,
--     product_id INTEGER REFERENCES products(product_id),
--     quantity INTEGER
-- );


-- INSERT INTO customers (first_name, last_name, email, phone_number) VALUES
-- ('John', 'Doe', 'john.doe@gmail.com', '0612345678'),
-- ('Alice', 'Smith', 'alice.smith@yahoo.com', '0623456789'),
-- ('David', 'Dubois', 'david.dubois@live.com', '0634567890'),
-- ('Maria', 'Gonzalez', 'maria.gon@gmail.com', '0645678901'),
-- ('Karim', 'Dali', 'karim.dali@outlook.com', '0656789012');

-- INSERT INTO products (name, price, category) VALUES
-- ('Laptop', 899.99, 'Electronics'),
-- ('Smartphone', 599.50, 'Electronics'),
-- ('Office Chair', 149.90, 'Furniture'),
-- ('Coffee Maker', 79.99, 'Appliances'),
-- ('USB-C Cable', 15.00, 'Accessories');


-- INSERT INTO orders (customer_id, order_date, total_amount) VALUES
-- (1, '2024-01-15', 914.99),
-- (3, '2024-03-02', 78.99),
-- (2, '2023-12-30', 149.90),
-- (1, '2024-04-18', 614.50),
-- (5, '2022-11-01', 79.99);


-- INSERT INTO order_items (order_id, product_id, quantity) VALUES
-- (1, 1, 1),
-- (1, 5, 1),
-- (2, 4, 1),
-- (3, 3, 1),
-- (4, 2, 1),
-- (5, 4, 1);

-- SELECT * FROM Customers;

-- SELECT * FROM orders WHERE order_date > '2024-01-01';

-- SELECT c.first_name,c.email
-- FROM customers c
-- JOIN orders o ON c.customer_id = o.customer_id;


-- SELECT * FROM customers WHERE first_name = 'John';
-- SELECT * FROM orders WHERE total_amount > 100;
-- SELECT * FROM customers WHERE first_name LIKE 'D%';

-- UPDATE customers
-- SET phone_number = '0610101010'
-- WHERE customer_id = 1;

-- UPDATE orders
-- SET total_amount = total_amount * 1.10;

-- UPDATE customers
-- SET email = 'john.doe@newdomain.com'
-- WHERE email = 'john.doe@gmail.com';


-- DELETE FROM orders WHERE order_date < '2023-01-01' 

-- DELETE FROM customers WHERE customer_id = 1;
-- DELETE FROM orders  WHERE customer_id = 1;

-- DELETE FROM orders  WHERE customer_id = 2;

-- ********************* challenge 2 ****************
-- SELECT
--   o.order_id,
--   o.order_date,
--   o.total_amount,
--   c.first_name,
--   c.last_name
-- FROM orders o
-- JOIN customers c ON o.customer_id = c.customer_id;


-- SELECT 
-- 	c.customer_id,
-- 	o.order_id,
-- 	c.first_name,
-- 	c.last_name
-- FROM customers c
-- LEFT JOIN orders o ON o.customer_id = c.customer_id
-- WHERE o.order_id IS NULL

-- SELECT 
--   c.customer_id,
--   c.first_name,
--   COUNT(c.customer_id) AS nombre_commandes
-- FROM customers c
-- LEFT JOIN orders o ON o.customer_id = c.customer_id
-- GROUP BY c.customer_id, c.first_name
-- ORDER BY nombre_commandes DESC;

-- SELECT SUM(total_amount) AS total_orders 
-- FROM orders;

-- SELECT COUNT(*) AS nombre_clients
-- FROM customers;

-- select avg(total_amount) from orders

-- SELECT 
--   c.customer_id,
--   c.first_name,
--   c.last_name,
--   SUM(o.total_amount) AS total_orders
-- FROM customers c
-- JOIN orders o ON c.customer_id = o.customer_id
-- GROUP BY c.customer_id, c.first_name, c.last_name
-- ORDER BY total_orders DESC;

-- SELECT 
--   TO_CHAR(order_date, 'MM') AS mois,
--   COUNT(*) AS nombre_commandes
-- FROM orders
-- GROUP BY mois
-- ORDER BY mois;


-- SELECT 
--   TO_CHAR(order_date, 'MM') AS mois,
--   AVG(total_amount) AS montant_moyen
-- FROM orders
-- GROUP BY mois
-- ORDER BY mois;

-- SELECT 
--   c.customer_id,
--   c.first_name,
--   c.last_name,
--   SUM(o.total_amount) AS total_commandes
-- FROM customers c
-- JOIN orders o ON c.customer_id = o.customer_id
-- GROUP BY c.customer_id, c.first_name, c.last_name
-- HAVING SUM(o.total_amount) > 100
-- ORDER BY total_commandes DESC;

-- ***********************


-- SELECT DISTINCT c.*
-- FROM customers c
-- WHERE c.customer_id IN (
--   SELECT customer_id
--   FROM orders
--   WHERE total_amount > 200
-- );


-- SELECT c.customer_id, c.first_name, c.last_name, total
-- FROM customers c
-- JOIN (
--   SELECT customer_id, SUM(total_amount) AS total
--   FROM orders
--   GROUP BY customer_id
--   ORDER BY total DESC
--   LIMIT 1
-- ) AS sub ON c.customer_id = sub.customer_id;


-- SELECT *
-- FROM orders
-- WHERE total_amount > (
--   SELECT AVG(total_amount) FROM orders
-- );


-- CREATE OR REPLACE VIEW customer_orders_view AS
-- SELECT 
--   c.customer_id,
--   c.first_name,
--   c.last_name,
--   o.order_id,
--   o.order_date,
--   o.total_amount
-- FROM customers c
-- JOIN orders o ON c.customer_id = o.customer_id;


-- SELECT 
--   customer_id,
--   first_name,
--   last_name,
--   SUM(total_amount) AS total_commandes
-- FROM customer_orders_view
-- GROUP BY customer_id, first_name, last_name
-- HAVING SUM(total_amount) > 1000
-- ORDER BY total_commandes DESC;



-- CREATE OR REPLACE VIEW monthly_sales_view AS
-- SELECT 
--   TO_CHAR(order_date, 'MM') AS mois,
--   SUM(total_amount) AS total_ventes
-- FROM orders
-- GROUP BY mois
-- ORDER BY mois;

