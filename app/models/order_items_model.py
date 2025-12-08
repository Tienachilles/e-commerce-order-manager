from app.core.connection import get_connection

# -------------------------
# ORDER ITEMS CRUD
# -------------------------

def add_order_item(order_id, product_id, quantity, price):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO OrdersItems (OrderID, ProductID, Quantity, Price) VALUES (%s, %s, %s, %s)",
        (order_id, product_id, quantity, price)
    )
    conn.commit()
    cur.close()
    conn.close()


def get_order_item(order_id, product_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT OrderID, ProductID, Quantity, Price FROM OrdersItems WHERE OrderID=%s AND ProductID=%s",
        (order_id, product_id)
    )
    row = cur.fetchone()
    cur.close()
    conn.close()
    return row


def update_order_item(order_id, product_id, quantity, price):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE OrdersItems SET Quantity=%s, Price=%s WHERE OrderID=%s AND ProductID=%s",
        (quantity, price, order_id, product_id)
    )
    conn.commit()
    cur.close()
    conn.close()


def delete_order_item(order_id, product_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "DELETE FROM OrdersItems WHERE OrderID=%s AND ProductID=%s",
        (order_id, product_id)
    )
    conn.commit()
    cur.close()
    conn.close()
