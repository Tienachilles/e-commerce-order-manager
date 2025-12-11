import tkinter as tk
from tkinter import ttk, messagebox
from app.controllers.products_controller import ProductsController
from app.core.validators import is_positive_number
from app.views.table_factory import TableFactory

def render_products(parent):
    ctrl = ProductsController()

    frame = ttk.Frame(parent)
    frame.pack(fill="both", expand=True)

    columns = ("ProductID", "Name", "Price")
    table = TableFactory.create(frame, columns)

    def load():
        table.delete(*table.get_children())
        for r in ctrl.list():
            table.insert("", "end", values=r)

    load()

    btn_frame = ttk.Frame(frame)
    btn_frame.pack(fill="x", pady=10)

    def on_add():
        w = tk.Toplevel()
        w.title("Add Product")

        ttk.Label(w, text="ID").pack()
        e_id = ttk.Entry(w); e_id.pack()

        ttk.Label(w, text="Name").pack()
        e_name = ttk.Entry(w); e_name.pack()

        ttk.Label(w, text="Price").pack()
        e_price = ttk.Entry(w); e_price.pack()

        def save():
            pid = e_id.get()
            name = e_name.get()
            price = e_price.get()

            if not is_positive_number(price):
                messagebox.showerror("Error", "Invalid price")
                return

            ctrl.add(pid, name, float(price))
            load()
            w.destroy()

        ttk.Button(w, text="Save", command=save).pack(pady=5)

    ttk.Button(btn_frame, text="Add", command=on_add).pack(side="left", padx=5)
