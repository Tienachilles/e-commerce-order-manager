from connection import get_connection
from Customer_model import get_customer, add_customer


# READ
def get_order(OrderID):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "SELECT OrderID, CustomerID, OrderDate, Status FROM Orders WHERE OrderID = %s"
    cursor.execute(sql, (OrderID,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result


# CREATE
def add_order(OrderID, CustomerID, OrderDate, Status):

    # If customer does not exist -> automatically add
    if not get_customer(CustomerID):
        print("⚠ Customer does not exist. Adding new customer...")
        add_customer(CustomerID, f"Customer_{CustomerID}")

    conn = get_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO Orders(OrderID, CustomerID, OrderDate, Status) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (OrderID, CustomerID, OrderDate, Status))
    conn.commit()
    cursor.close()
    conn.close()
    print("Inserted order:", OrderID)


# UPDATE
def update_order(OrderID, CustomerID, OrderDate, Status):

    # If new customer ID does not exist -> automatically add
    if not get_customer(CustomerID):
        print("New customer ID does not exist. Adding new customer...")
        add_customer(CustomerID, f"Customer_{CustomerID}")

    conn = get_connection()
    cursor = conn.cursor()
    sql = "UPDATE Orders SET CustomerID = %s, OrderDate = %s, Status = %s WHERE OrderID = %s"
    cursor.execute(sql, (CustomerID, OrderDate, Status, OrderID))
    conn.commit()
    cursor.close()
    conn.close()
    print("Updated order:", OrderID)


# DELETE
def delete_order(OrderID):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "DELETE FROM Orders WHERE OrderID = %s"
    cursor.execute(sql, (OrderID,))
    conn.commit()
    cursor.close()
    conn.close()
    print("Deleted order:", OrderID)
