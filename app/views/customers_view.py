import tkinter as tk
from tkinter import ttk, messagebox
from app.controllers.customers_controller import CustomersController

def render_customers(parent):
    ctrl = CustomersController()

    frame = ttk.Frame(parent)
    frame.pack(fill="both", expand=True, padx=10, pady=10)

    # table
    cols = ("CustomerID", "Name")
    tree = ttk.Treeview(frame, columns=cols, show="headings")
    for c in cols:
        tree.heading(c, text=c)
        tree.column(c, width=200)
    tree.pack(fill="both", expand=True)

    def load():
        tree.delete(*tree.get_children())
        for row in ctrl.list():
            tree.insert("", "end", values=row)

    load()

    # buttons
    btn_frame = ttk.Frame(frame)
    btn_frame.pack(fill="x")

    def on_add():
        w = tk.Toplevel()
        w.title("Add Customer")

        ttk.Label(w, text="ID").pack()
        e_id = ttk.Entry(w)
        e_id.pack()

        ttk.Label(w, text="Name").pack()
        e_name = ttk.Entry(w)
        e_name.pack()

        def save():
            cid = e_id.get()
            name = e_name.get()
            if not cid or not name:
                messagebox.showwarning("Error", "All fields required")
                return
            ctrl.add(cid, name)
            load()
            w.destroy()

        ttk.Button(w, text="Save", command=save).pack(pady=5)

    ttk.Button(btn_frame, text="Add", command=on_add).pack(side="left", padx=5)

    def on_delete():
        sel = tree.selection()
        if not sel:
            return
        cid = tree.item(sel[0])["values"][0]
        if messagebox.askyesno("Delete", f"Delete customer {cid}?"):
            ctrl.delete(cid)
            load()

    ttk.Button(btn_frame, text="Delete", command=on_delete).pack(side="left", padx=5)
