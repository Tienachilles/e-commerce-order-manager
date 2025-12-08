from app.core.connection import get_connection

# -------------------------
# PRODUCT CRUD
# -------------------------

def add_product(product_id, name, price):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO Products (ProductID, Name, Price) VALUES (%s, %s, %s)",
        (product_id, name, price)
    )
    conn.commit()
    cur.close()
    conn.close()


def get_product(product_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT ProductID, Name, Price FROM Products WHERE ProductID=%s",
        (product_id,)
    )
    row = cur.fetchone()
    cur.close()
    conn.close()
    return row


def update_product(product_id, name, price):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE Products SET Name=%s, Price=%s WHERE ProductID=%s",
        (name, price, product_id)
    )
    conn.commit()
    cur.close()
    conn.close()


def delete_product(product_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "DELETE FROM Products WHERE ProductID=%s",
        (product_id,)
    )
    conn.commit()
    cur.close()
    conn.close()
