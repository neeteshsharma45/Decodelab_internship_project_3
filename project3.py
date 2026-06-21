import pandas as pd
import sqlite3

# Step 1: Load Excel file
df = pd.read_excel("cleaned_dataset.xlsx")

# Step 2: Connect to SQLite database
conn = sqlite3.connect("project3.db")

# Step 3: Store data in SQL table
df.to_sql("orders", conn, if_exists="replace", index=False)

print("Dataset loaded into SQL successfully!")

# Step 4: Query 1 - Show first 5 rows
query1 = "SELECT * FROM orders LIMIT 5;"
result1 = pd.read_sql(query1, conn)
print("\nFirst 5 Rows:")
print(result1)

# Step 5: Query 2 - Total number of orders
query2 = "SELECT COUNT(*) AS total_orders FROM orders;"
result2 = pd.read_sql(query2, conn)
print("\nTotal Orders:")
print(result2)

# Step 6: Query 3 - Total revenue
query3 = "SELECT SUM(TotalPrice) AS total_revenue FROM orders;"
result3 = pd.read_sql(query3, conn)
print("\nTotal Revenue:")
print(result3)

# Step 7: Query 4 - Average order value
query4 = "SELECT AVG(TotalPrice) AS average_order_value FROM orders;"
result4 = pd.read_sql(query4, conn)
print("\nAverage Order Value:")
print(result4)

# Step 8: Query 5 - Revenue by Product
query5 = """
SELECT Product, SUM(TotalPrice) AS revenue
FROM orders
GROUP BY Product
ORDER BY revenue DESC;
"""
result5 = pd.read_sql(query5, conn)
print("\nRevenue by Product:")
print(result5)

# Step 9: Query 6 - Orders by Payment Method
query6 = """
SELECT PaymentMethod, COUNT(*) AS total_orders
FROM orders
GROUP BY PaymentMethod
ORDER BY total_orders DESC;
"""
result6 = pd.read_sql(query6, conn)
print("\nOrders by Payment Method:")
print(result6)

# Step 10: Query 7 - Delivered orders only
query7 = """
SELECT OrderID, Product, TotalPrice
FROM orders
WHERE OrderStatus = 'Delivered';
"""
result7 = pd.read_sql(query7, conn)
print("\nDelivered Orders:")
print(result7.head())

# Close connection
conn.close()
print("\nProject 3 completed successfully!")
conn = sqlite3.connect("project3.db")