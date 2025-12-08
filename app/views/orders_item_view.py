import tkinter as tk
from tkinter import ttk, messagebox
from app.controllers.order_items_controller import OrderItemsController
from app.core.validators import is_positive_int, is_positive_number

def render_order_items(parent):
    ctrl = OrderItemsController()

    frame = ttk.Frame(parent)
    frame.pack(fill="both", expand=True)

    cols = ("OrderID", "ProductID", "Quantity", "Price")
    tree = ttk.Treeview(frame, columns=cols, show="headings")
    for c in cols:
        tree.heading(c, text=c)
        tree.column(c, width=160)
    tree.pack(fill="both", expand=True)

    def load():
        tree.delete(*tree.get_children())
        for r in ctrl.list():
            tree.insert("", "end", values=r)

    load()

    btn_frame = ttk.Frame(frame)
    btn_frame.pack(fill="x")

    def on_add():
        w = tk.Toplevel()
        w.title("Add Item")

        ttk.Label(w, text="Order ID").pack()
        e_oid = ttk.Entry(w); e_oid.pack()

        ttk.Label(w, text="Product ID").pack()
        e_pid = ttk.Entry(w); e_pid.pack()

        ttk.Label(w, text="Quantity").pack()
        e_qty = ttk.Entry(w); e_qty.pack()

        ttk.Label(w, text="Price").pack()
        e_price = ttk.Entry(w); e_price.pack()

        def save():
            oid, pid, qty, price = e_oid.get(), e_pid.get(), e_qty.get(), e_price.get()

            if not is_positive_int(qty) or not is_positive_number(price):
                messagebox.showerror("Error", "Invalid quantity/price")
                return

            ctrl.add(oid, pid, int(qty), float(price))
            load()
            w.destroy()

        ttk.Button(w, text="Save", command=save).pack(pady=5)

    ttk.Button(btn_frame, text="Add", command=on_add).pack(side="left", padx=5)
