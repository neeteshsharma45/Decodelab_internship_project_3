SELECT * FROM orders LIMIT 5;
SELECT COUNT(*) AS total_orders FROM orders;

SELECT SUM(TotalPrice) AS total_revenue FROM orders;

SELECT AVG(TotalPrice) AS average_order_value FROM orders;


SELECT Product, SUM(TotalPrice) AS revenue
FROM orders
GROUP BY Product
ORDER BY revenue DESC;

SELECT PaymentMethod, COUNT(*) AS total_orders
FROM orders
GROUP BY PaymentMethod
ORDER BY total_orders DESC;

SELECT OrderID, Product, TotalPrice
FROM orders
WHERE OrderStatus = 'Delivered';
