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

    # Nếu khách hàng chưa tồn tại → tự động thêm
    if not get_customer(CustomerID):
        print("⚠ Khách hàng chưa tồn tại. Đang thêm mới...")
        add_customer(CustomerID, f"Customer_{CustomerID}")

    conn = get_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO Orders(OrderID, CustomerID, OrderDate, Status) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (OrderID, CustomerID, OrderDate, Status))
    conn.commit()
    cursor.close()
    conn.close()
    print("Đã chèn đơn hàng:", OrderID)


# UPDATE
def update_order(OrderID, CustomerID, OrderDate, Status):

    # Nếu khách hàng chưa tồn tại → tự động thêm
    if not get_customer(CustomerID):
        print("Khách hàng mới chưa tồn tại. Đang thêm mới...")
        add_customer(CustomerID, f"Customer_{CustomerID}")

    conn = get_connection()
    cursor = conn.cursor()
    sql = "UPDATE Orders SET CustomerID = %s, OrderDate = %s, Status = %s WHERE OrderID = %s"
    cursor.execute(sql, (CustomerID, OrderDate, Status, OrderID))
    conn.commit()
    cursor.close()
    conn.close()
    print("Đã cập nhật đơn hàng:", OrderID)


# DELETE
def delete_order(OrderID):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "DELETE FROM Orders WHERE OrderID = %s"
    cursor.execute(sql, (OrderID,))
    conn.commit()
    cursor.close()
    conn.close()
    print("Đã xóa đơn hàng:", OrderID)
