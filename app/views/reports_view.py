import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from app.services.reports_service import (
    report_inner_join,
    report_left_join,
    report_multi_join,
    report_order_summary
)

def render_reports(parent):
    frame = ttk.Frame(parent)
    frame.pack(fill="both", expand=True)

    ttk.Label(frame, text="Reports", font=("Segoe UI", 14)).pack(pady=5)

    def show_df(df, title):
        win = tk.Toplevel()
        win.title(title)
        win.geometry("850x500")

        cols = list(df.columns)
        tree = ttk.Treeview(win, columns=cols, show="headings")
        for c in cols:
            tree.heading(c, text=c)
            tree.column(c, width=140)
        tree.pack(fill="both", expand=True)

        for row in df.itertuples(index=False, name=None):
            tree.insert("", "end", values=row)

        def export():
            path = filedialog.asksaveasfilename(defaultextension=".csv")
            if path:
                df.to_csv(path, index=False)
                messagebox.showinfo("Saved", f"Exported to {path}")

        ttk.Button(win, text="Export CSV", command=export).pack(pady=5)

    ttk.Button(frame, text="INNER JOIN", command=lambda: show_df(report_inner_join(), "INNER JOIN")).pack(fill="x", pady=3)
    ttk.Button(frame, text="LEFT JOIN", command=lambda: show_df(report_left_join(), "LEFT JOIN")).pack(fill="x", pady=3)
    ttk.Button(frame, text="MULTI JOIN", command=lambda: show_df(report_multi_join(), "MULTI JOIN")).pack(fill="x", pady=3)
    ttk.Button(frame, text="ORDER SUMMARY", command=lambda: show_df(report_order_summary(), "ORDER SUMMARY")).pack(fill="x", pady=3)
