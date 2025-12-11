import tkinter as tk
from tkinter import ttk, messagebox
from app.controllers.orders_controller import OrdersController
from app.core.validators import parse_date
from app.views.table_factory import TableFactory

def render_orders(parent):
    ctrl = OrdersController()

    frame = ttk.Frame(parent)
    frame.pack(fill="both", expand=True)

    columns = ("OrderID", "CustomerID", "OrderDate", "Status")
    table = TableFactory.create(frame, columns)

    def load():
        table.delete(*table.get_children())
        for r in ctrl.list():
            table.insert("", "end", values=r)

    load()

    btn_frame = ttk.Frame(frame)
    btn_frame.pack(fill="x", pady=10)

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
            date = parse_date(e_date.get())
            if date is None:
                messagebox.showerror("Invalid Date", "Use YYYY-MM-DD")
                return

            ctrl.add(e_oid.get(), e_cid.get(), e_date.get(), e_status.get())
            load()
            w.destroy()

        ttk.Button(w, text="Save", command=save).pack(pady=5)

    ttk.Button(btn_frame, text="Add", command=on_add).pack(side="left", padx=5)
