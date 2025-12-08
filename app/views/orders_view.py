import tkinter as tk
from tkinter import ttk, messagebox
from app.controllers.orders_controller import OrdersController
from app.core.validators import parse_date

def render_orders(parent):
    ctrl = OrdersController()

    frame = ttk.Frame(parent)
    frame.pack(fill="both", expand=True)

    cols = ("OrderID", "CustomerID", "OrderDate", "Status")
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
        w = tk.Toplevel(); w.title("Add Order")

        ttk.Label(w, text="Order ID").pack()
        e_oid = ttk.Entry(w); e_oid.pack()

        ttk.Label(w, text="Customer ID").pack()
        e_cid = ttk.Entry(w); e_cid.pack()

        ttk.Label(w, text="Date (YYYY-MM-DD)").pack()
        e_date = ttk.Entry(w); e_date.pack()

        ttk.Label(w, text="Status").pack()
        e_status = ttk.Entry(w); e_status.pack()

        def save():
            oid = e_oid.get()
            cid = e_cid.get()
            date = e_date.get()
            status = e_status.get()

            if parse_date(date) is None:
                messagebox.showerror("Invalid Date", "Use YYYY-MM-DD")
                return

            ctrl.add(oid, cid, date, status)
            load()
            w.destroy()

        ttk.Button(w, text="Save", command=save).pack(pady=5)

    ttk.Button(btn_frame, text="Add", command=on_add).pack(side="left", padx=5)
