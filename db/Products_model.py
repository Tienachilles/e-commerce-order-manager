from connection import get_connection

# READ
def get_product(ProductID):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "SELECT ProductID, Name, Price FROM Products WHERE ProductID = %s"
    cursor.execute(sql, (ProductID,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result


# CREATE
def add_product(ProductID, Name, Price):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO Products(ProductID, Name, Price) VALUES (%s, %s, %s)"
    cursor.execute(sql, (ProductID, Name, Price))
    conn.commit()
    cursor.close()
    conn.close()
    print("Inserted product:", ProductID, Name, Price)


# UPDATE
def update_product(ProductID, Name, Price):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "UPDATE Products SET Name = %s, Price = %s WHERE ProductID = %s"
    cursor.execute(sql, (Name, Price, ProductID))
    conn.commit()
    cursor.close()
    conn.close()
    print("Updated product:", ProductID, Name, Price)


# DELETE
def delete_product(ProductID):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "DELETE FROM Products WHERE ProductID = %s"
    cursor.execute(sql, (ProductID,))
    conn.commit()
    cursor.close()
    conn.close()
    print("Deleted product:", ProductID)
