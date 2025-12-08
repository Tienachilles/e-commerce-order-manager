from app.core.connection import get_connection

# -------------------------
# ORDER CRUD
# -------------------------

def add_order(order_id, customer_id, order_date, status):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO Orders (OrderID, CustomerID, OrderDate, Status) VALUES (%s, %s, %s, %s)",
        (order_id, customer_id, order_date, status)
    )
    conn.commit()
    cur.close()
    conn.close()


def get_order(order_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT OrderID, CustomerID, OrderDate, Status FROM Orders WHERE OrderID=%s",
        (order_id,)
    )
    row = cur.fetchone()
    cur.close()
    conn.close()
    return row


def update_order(order_id, customer_id, order_date, status):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE Orders SET CustomerID=%s, OrderDate=%s, Status=%s WHERE OrderID=%s",
        (customer_id, order_date, status, order_id)
    )
    conn.commit()
    cur.close()
    conn.close()


def delete_order(order_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "DELETE FROM Orders WHERE OrderID=%s",
        (order_id,)
    )
    conn.commit()
    cur.close()
    conn.close()
