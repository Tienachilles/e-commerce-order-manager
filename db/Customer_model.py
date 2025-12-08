from connection import get_connection

def add_customer(CustomerID, Name):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO Customers(CustomerID, Name) VALUES (%s, %s)"
    cursor.execute(sql, (CustomerID, Name))
    conn.commit()
    cursor.close()
    conn.close()
    print("Đã chèn:", CustomerID, Name)

def get_customer(CustomerID):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "SELECT CustomerID, Name FROM Customers WHERE CustomerID = %s"
    cursor.execute(sql, (CustomerID,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def update_customer(CustomerID, Name):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "UPDATE Customers SET Name = %s WHERE CustomerID = %s"
    cursor.execute(sql, (Name, CustomerID))
    conn.commit()
    cursor.close()
    conn.close()
    print("Đã cập nhật:", CustomerID, "thành", Name)

def delete_customer(CustomerID):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "DELETE FROM Customers WHERE CustomerID = %s"
    cursor.execute(sql, (CustomerID,))
    conn.commit()
    cursor.close()
    conn.close()
    print("Đã xóa:", CustomerID)
