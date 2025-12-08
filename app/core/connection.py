from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv()

def get_connection():
    """
    Return MySQL connection using .env variables.
    Must have: DB_HOST, DB_USER, DB_PASS, DB_NAME
    """
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        database=os.getenv("DB_NAME")
    )

# --------------------------
# Generic fetch helpers
# --------------------------

def fetch_all_customers():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT CustomerID, Name FROM Customers ORDER BY CustomerID")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows


def fetch_all_products():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT ProductID, Name, Price FROM Products ORDER BY ProductID")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows


def fetch_all_orders():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT OrderID, CustomerID, OrderDate, Status 
        FROM Orders 
        ORDER BY OrderDate DESC
    """)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows


def fetch_order_items(order_id=None):
    conn = get_connection()
    cur = conn.cursor()

    if order_id:
        cur.execute("""
            SELECT OrderID, ProductID, Quantity, Price 
            FROM OrdersItems 
            WHERE OrderID=%s
        """, (order_id,))
    else:
        cur.execute("""
            SELECT OrderID, ProductID, Quantity, Price 
            FROM OrdersItems
        """)

    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows
