from app.core.connection import get_connection

# -------------------------
# CUSTOMER CRUD
# -------------------------

def add_customer(customer_id, name):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO Customers (CustomerID, Name) VALUES (%s, %s)",
        (customer_id, name)
    )
    conn.commit()
    cur.close()
    conn.close()


def get_customer(customer_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT CustomerID, Name FROM Customers WHERE CustomerID=%s",
        (customer_id,)
    )
    row = cur.fetchone()
    cur.close()
    conn.close()
    return row


def update_customer(customer_id, name):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE Customers SET Name=%s WHERE CustomerID=%s",
        (name, customer_id)
    )
    conn.commit()
    cur.close()
    conn.close()


def delete_customer(customer_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "DELETE FROM Customers WHERE CustomerID=%s",
        (customer_id,)
    )
    conn.commit()
    cur.close()
    conn.close()
