import tkinter as tk
from tkinter import ttk

class TableFactory:

    @staticmethod
    def create(parent, columns, column_width=160):
        style = ttk.Style()

        # Base table style
        style.configure(
            "Enhanced.Treeview",
            background="white",
            foreground="#1e293b",
            rowheight=32,
            fieldbackground="white",
            borderwidth=0,
            font=("Segoe UI", 10)
        )

        style.configure(
            "Enhanced.Treeview.Heading",
            background="#e2e8f0",
            foreground="#0f172a",
            font=("Segoe UI", 11, "bold"),
            relief="flat",
            padding=6
        )

        style.map(
            "Enhanced.Treeview",
            background=[("selected", "#bae6fd")],
            foreground=[("selected", "#000000")]
        )

        wrapper = tk.Frame(parent, bg="white")
        wrapper.pack(fill="both", expand=True)

        table = ttk.Treeview(
            wrapper,
            columns=columns,
            show="headings",
            style="Enhanced.Treeview"
        )

        scroll_y = ttk.Scrollbar(wrapper, orient="vertical", command=table.yview)
        scroll_x = ttk.Scrollbar(wrapper, orient="horizontal", command=table.xview)
        table.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

        scroll_y.pack(side="right", fill="y")
        scroll_x.pack(side="bottom", fill="x")
        table.pack(side="left", fill="both", expand=True)

        for c in columns:
            table.heading(c, text=c)
            table.column(c, width=column_width, anchor="w")

        return table
