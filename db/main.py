# ==========================
# IMPORT CÁC MODEL
# ==========================
from Customer_model import add_customer, get_customer, update_customer, delete_customer
from Order_model import add_order, get_order, update_order, delete_order
from Products_model import add_product, get_product, update_product, delete_product
from Ordersitem_model import add_order_item, get_order_item, update_order_item, delete_order_item
import sys
sys.stdout.reconfigure(encoding='utf-8')

# ==========================
#         MENU CHÍNH
# ==========================
print("======== MENU CHÍNH ========")
print("1. Customers")
print("2. Orders")
print("3. Products")
print("4. OrderItems")
print("0. Thoát")

table_choice = input("Chọn bảng muốn thao tác: ")


# =====================================================
#                   CUSTOMERS MENU
# =====================================================
if table_choice == "1":
    print("----- CUSTOMERS MENU -----")
    print("1. Thêm Customer")
    print("2. Sửa Customer")
    print("3. Xóa Customer")
    print("4. Xem Customer")

    choice = input("Chọn chức năng: ")

    if choice == "1":
        cid = input("Nhập CustomerID: ")
        name = input("Nhập CustomerName: ")
        add_customer(cid, name)

    elif choice == "2":
        cid = input("Nhập CustomerID muốn cập nhật: ")
        name = input("Nhập CustomerName mới: ")
        update_customer(cid, name)

    elif choice == "3":
        cid = input("Nhập CustomerID muốn xóa: ")
        delete_customer(cid)

    elif choice == "4":
        cid = input("Nhập CustomerID muốn xem: ")
        customer = get_customer(cid)
        if customer:
            print("CustomerID:", customer[0])
            print("Name:", customer[1])
        else:
            print("Không tìm thấy khách hàng!")


# =====================================================
#                      ORDERS MENU
# =====================================================
elif table_choice == "2":
    print("----- ORDERS MENU -----")
    print("1. Thêm Order")
    print("2. Sửa Order")
    print("3. Xóa Order")
    print("4. Xem Order")

    choice = input("Chọn chức năng: ")

    if choice == "1":
        cid = input("Nhập CustomerID (sẽ tự thêm nếu chưa có): ")
        oid = input("Nhập OrderID: ")
        odate = input("Nhập OrderDate (YYYY-MM-DD): ")
        status = input("Nhập Status: ")
        add_order(oid, cid, odate, status)

    elif choice == "2":
        oid = input("Nhập OrderID muốn cập nhật: ")
        cid = input("Nhập CustomerID mới: ")
        odate = input("Nhập OrderDate mới (YYYY-MM-DD): ")
        status = input("Nhập Status mới: ")
        update_order(oid, cid, odate, status)

    elif choice == "3":
        oid = input("Nhập OrderID muốn xóa: ")
        delete_order(oid)

    elif choice == "4":
        oid = input("Nhập OrderID muốn xem: ")
        order = get_order(oid)
        if order:
            print("OrderID:", order[0])
            print("CustomerID:", order[1])
            print("OrderDate:", order[2])
            print("Status:", order[3])
        else:
            print("Không tìm thấy đơn hàng!")


# =====================================================
#                     PRODUCTS MENU
# =====================================================
elif table_choice == "3":
    print("----- PRODUCTS MENU -----")
    print("1. Thêm Product")
    print("2. Sửa Product")
    print("3. Xóa Product")
    print("4. Xem Product")

    choice = input("Chọn chức năng: ")

    if choice == "1":
        pid = input("Nhập ProductID: ")
        name = input("Nhập ProductName: ")
        price = float(input("Nhập Price: "))
        add_product(pid, name, price)

    elif choice == "2":
        pid = input("Nhập ProductID muốn cập nhật: ")
        name = input("Nhập ProductName mới: ")
        price = float(input("Nhập Price mới: "))
        update_product(pid, name, price)

    elif choice == "3":
        pid = input("Nhập ProductID muốn xóa: ")
        delete_product(pid)

    elif choice == "4":
        pid = input("Nhập ProductID muốn xem: ")
        product = get_product(pid)
        if product:
            print("ProductID:", product[0])
            print("Name:", product[1])
            print("Price:", product[2])
        else:
            print("Không tìm thấy sản phẩm!")


# =====================================================
#                ORDER ITEMS MENU
# =====================================================
elif table_choice == "4":
    print("----- ORDER ITEMS MENU -----")
    print("1. Thêm OrderItem")
    print("2. Sửa OrderItem")
    print("3. Xóa OrderItem")
    print("4. Xem OrderItem")

    choice = input("Chọn chức năng: ")

    if choice == "1":
        oid = input("Nhập OrderID: ")
        pid = input("Nhập ProductID (auto-add nếu chưa có): ")
        qty = int(input("Nhập Quantity: "))
        price = float(input("Nhập Price: "))
        add_order_item(oid, pid, qty, price)

    elif choice == "2":
        oid = input("Nhập OrderID muốn cập nhật: ")
        pid = input("Nhập ProductID muốn cập nhật: ")
        qty = int(input("Nhập Quantity mới: "))
        price = float(input("Nhập Price mới: "))
        update_order_item(oid, pid, qty, price)

    elif choice == "3":
        oid = input("Nhập OrderID muốn xóa: ")
        pid = input("Nhập ProductID muốn xóa: ")
        delete_order_item(oid, pid)

    elif choice == "4":
        oid = input("Nhập OrderID muốn xem: ")
        pid = input("Nhập ProductID muốn xem: ")
        item = get_order_item(oid, pid)
        if item:
            print("OrderID:", item[0])
            print("ProductID:", item[1])
            print("Quantity:", item[2])
            print("Price:", item[3])
        else:
            print("Không tìm thấy OrderItem!")


# =====================================================
#                    THOÁT CHƯƠNG TRÌNH
# =====================================================
elif table_choice == "0":
    print("Đã thoát chương trình!")

else:
    print("Lựa chọn không hợp lệ!")
