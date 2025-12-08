import tkinter as tk
from tkinter import ttk
from functools import partial

from .views.dashboard_view import render_dashboard
from .views.customers_view import render_customers
from .views.products_view import render_products
from .views.orders_view import render_orders
from .views.orders_item_view import render_order_items
from .views.reports_view import render_reports

# ----------------------------
# Main Application Window
# ----------------------------
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("E-Commerce Management System")
        self.root.geometry("1200x700")
        self.root.minsize(1100, 650)

        # Setup style
        self.setup_style()
        self.create_layout()

    def setup_style(self):
        self.style = ttk.Style()
        self.style.theme_use("clam")

        # Sidebar frame
        self.style.configure("Sidebar.TFrame", background="#2c3e50")
        # Content frame
        self.style.configure("Content.TFrame", background="#ecf0f1")
        # Sidebar buttons
        self.style.configure("Sidebar.TButton",
                             font=("Segoe UI", 11),
                             foreground="white",
                             background="#2c3e50",
                             relief="flat",
                             anchor="w",
                             padding=10)
        self.style.map("Sidebar.TButton",
                       background=[("active", "#34495e")],
                       foreground=[("active", "white")])

        # Treeview style
        self.style.configure("Treeview",
                             font=("Segoe UI", 10),
                             rowheight=28)
        self.style.configure("Treeview.Heading",
                             font=("Segoe UI", 11, "bold"))

    def create_layout(self):
        # Sidebar
        self.sidebar = ttk.Frame(self.root, width=220, style="Sidebar.TFrame")
        self.sidebar.pack(side="left", fill="y")

        # Logo
        logo = tk.Label(self.sidebar, text="ECOM", font=("Segoe UI", 22, "bold"),
                        bg="#2c3e50", fg="white")
        logo.pack(pady=20)

        # Sidebar buttons with icons
        self.nav_buttons = [
            ("📊 Dashboard", self.show_dashboard),
            ("👥 Customers", self.show_customers),
            ("🛍️ Products", self.show_products),
            ("📦 Orders", self.show_orders),
            ("📝 Order Items", self.show_items),
            ("📈 Reports", self.show_reports),
        ]

        self.buttons = []
        for text, cmd in self.nav_buttons:
            btn = ttk.Button(self.sidebar, text=text, command=cmd, style="Sidebar.TButton")
            btn.pack(fill="x", pady=5, padx=10)
            # Hover effect
            btn.bind("<Enter>", lambda e, b=btn: b.config(style="Hovered.TButton"))
            btn.bind("<Leave>", lambda e, b=btn: b.config(style="Sidebar.TButton"))
            self.buttons.append(btn)

        # Hover style
        self.style.configure("Hovered.TButton", background="#34495e", foreground="white")

        # Content frame
        self.content = ttk.Frame(self.root, style="Content.TFrame")
        self.content.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        # Load default page
        self.show_dashboard()

    # ----------------------------
    # Routing functions
    # ----------------------------
    def clear_content(self):
        for widget in self.content.winfo_children():
            widget.destroy()

    def show_dashboard(self):
        self.clear_content()
        render_dashboard(self.content)

    def show_customers(self):
        self.clear_content()
        render_customers(self.content)

    def show_products(self):
        self.clear_content()
        render_products(self.content)

    def show_orders(self):
        self.clear_content()
        render_orders(self.content)

    def show_items(self):
        self.clear_content()
        render_order_items(self.content)

    def show_reports(self):
        self.clear_content()
        render_reports(self.content)


# ----------------------------
# APP ENTRY POINT
# ----------------------------
if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()
