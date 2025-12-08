from connection import get_connection
from Products_model import add_product, get_product
from Order_model import get_order

# ===== READ =====
def get_order_item(OrderID, ProductID):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "SELECT OrderID, ProductID, Quantity, Price FROM OrdersItems WHERE OrderID = %s AND ProductID = %s"
    cursor.execute(sql, (OrderID, ProductID))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result


# ===== CREATE =====
def add_order_item(OrderID, ProductID, Quantity, Price):

    # Nếu Order không tồn tại → không được thêm
    if not get_order(OrderID):
        print("⚠ Không thể thêm OrderItem vì OrderID chưa tồn tại!")
        return

    # Nếu Product chưa tồn tại → tự thêm sản phẩm
    if not get_product(ProductID):
        print("⚠ Product chưa tồn tại. Đang thêm mới...")
        add_product(ProductID, f"Product_{ProductID}", Price)

    conn = get_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO OrdersItems(OrderID, ProductID, Quantity, Price) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (OrderID, ProductID, Quantity, Price))
    conn.commit()
    cursor.close()
    conn.close()
    print(f"Đã thêm OrdersItem: {OrderID}, {ProductID}, Qty={Quantity}, Price={Price}")


# ===== UPDATE =====
def update_order_item(OrderID, ProductID, Quantity, Price):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "UPDATE OrdersItems SET Quantity = %s, Price = %s WHERE OrderID = %s AND ProductID = %s"
    cursor.execute(sql, (Quantity, Price, OrderID, ProductID))
    conn.commit()
    cursor.close()
    conn.close()
    print(f"Đã cập nhật OrdersItem: {OrderID}, {ProductID}, Qty={Quantity}, Price={Price}")


# ===== DELETE =====
def delete_order_item(OrderID, ProductID):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "DELETE FROM OrdersItems WHERE OrderID = %s AND ProductID = %s"
    cursor.execute(sql, (OrderID, ProductID))
    conn.commit()
    cursor.close()
    conn.close()
    print(f"Đã xóa OrdersItem: {OrderID}, {ProductID}")
