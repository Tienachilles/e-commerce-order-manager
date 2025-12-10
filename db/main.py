# ==========================
# IMPORT MODELS
# ==========================
from Customer_model import add_customer, get_customer, update_customer, delete_customer
from Order_model import add_order, get_order, update_order, delete_order
from Products_model import add_product, get_product, update_product, delete_product
from Ordersitem_model import add_order_item, get_order_item, update_order_item, delete_order_item
import sys
sys.stdout.reconfigure(encoding='utf-8')

# ==========================
#         MAIN MENU
# ==========================
print("======== MAIN MENU ========")
print("1. Customers")
print("2. Orders")
print("3. Products")
print("4. OrderItems")
print("0. Exit")

table_choice = input("Select table to operate on: ")


# =====================================================
#                   CUSTOMERS MENU
# =====================================================
if table_choice == "1":
    print("----- CUSTOMERS MENU -----")
    print("1. Add Customer")
    print("2. Edit Customer")
    print("3. Delete Customer")
    print("4. View Customer")

    choice = input("Select action: ")

    if choice == "1":
        cid = input("Enter CustomerID: ")
        name = input("Enter CustomerName: ")
        add_customer(cid, name)

    elif choice == "2":
        cid = input("Enter CustomerID to update: ")
        name = input("Enter new CustomerName: ")
        update_customer(cid, name)

    elif choice == "3":
        cid = input("Enter CustomerID to delete: ")
        delete_customer(cid)

    elif choice == "4":
        cid = input("Enter CustomerID to view: ")
        customer = get_customer(cid)
        if customer:
            print("CustomerID:", customer[0])
            print("Name:", customer[1])
        else:
            print("Customer not found!")


# =====================================================
#                      ORDERS MENU
# =====================================================
elif table_choice == "2":
    print("----- ORDERS MENU -----")
    print("1. Add Order")
    print("2. Edit Order")
    print("3. Delete Order")
    print("4. View Order")

    choice = input("Select action: ")

    if choice == "1":
        cid = input("Enter CustomerID (will auto-add if missing): ")
        oid = input("Enter OrderID: ")
        odate = input("Enter OrderDate (YYYY-MM-DD): ")
        status = input("Enter Status: ")
        add_order(oid, cid, odate, status)

    elif choice == "2":
        oid = input("Enter OrderID to update: ")
        cid = input("Enter new CustomerID: ")
        odate = input("Enter new OrderDate (YYYY-MM-DD): ")
        status = input("Enter new Status: ")
        update_order(oid, cid, odate, status)

    elif choice == "3":
        oid = input("Enter OrderID to delete: ")
        delete_order(oid)

    elif choice == "4":
        oid = input("Enter OrderID to view: ")
        order = get_order(oid)
        if order:
            print("OrderID:", order[0])
            print("CustomerID:", order[1])
            print("OrderDate:", order[2])
            print("Status:", order[3])
        else:
            print("Order not found!")


# =====================================================
#                     PRODUCTS MENU
# =====================================================
elif table_choice == "3":
    print("----- PRODUCTS MENU -----")
    print("1. Add Product")
    print("2. Edit Product")
    print("3. Delete Product")
    print("4. View Product")

    choice = input("Select action: ")

    if choice == "1":
        pid = input("Enter ProductID: ")
        name = input("Enter ProductName: ")
        price = float(input("Enter Price: "))
        add_product(pid, name, price)

    elif choice == "2":
        pid = input("Enter ProductID to update: ")
        name = input("Enter new ProductName: ")
        price = float(input("Enter new Price: "))
        update_product(pid, name, price)

    elif choice == "3":
        pid = input("Enter ProductID to delete: ")
        delete_product(pid)

    elif choice == "4":
        pid = input("Enter ProductID to view: ")
        product = get_product(pid)
        if product:
            print("ProductID:", product[0])
            print("Name:", product[1])
            print("Price:", product[2])
        else:
            print("Product not found!")


# =====================================================
#                ORDER ITEMS MENU
# =====================================================
elif table_choice == "4":
    print("----- ORDER ITEMS MENU -----")
    print("1. Add OrderItem")
    print("2. Edit OrderItem")
    print("3. Delete OrderItem")
    print("4. View OrderItem")

    choice = input("Select action: ")

    if choice == "1":
        oid = input("Enter OrderID: ")
        pid = input("Enter ProductID (will auto-add if missing): ")
        qty = int(input("Enter Quantity: "))
        price = float(input("Enter Price: "))
        add_order_item(oid, pid, qty, price)

    elif choice == "2":
        oid = input("Enter OrderID to update: ")
        pid = input("Enter ProductID to update: ")
        qty = int(input("Enter new Quantity: "))
        price = float(input("Enter new Price: "))
        update_order_item(oid, pid, qty, price)

    elif choice == "3":
        oid = input("Enter OrderID to delete: ")
        pid = input("Enter ProductID to delete: ")
        delete_order_item(oid, pid)

    elif choice == "4":
        oid = input("Enter OrderID to view: ")
        pid = input("Enter ProductID to view: ")
        item = get_order_item(oid, pid)
        if item:
            print("OrderID:", item[0])
            print("ProductID:", item[1])
            print("Quantity:", item[2])
            print("Price:", item[3])
        else:
            print("OrderItem not found!")


# =====================================================
#                    EXIT PROGRAM
# =====================================================
elif table_choice == "0":
    print("Exited program!")

else:
    print("Invalid selection!")
