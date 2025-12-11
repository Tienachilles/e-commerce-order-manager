import tkinter as tk
from tkinter import ttk
from functools import partial
from PIL import Image, ImageTk
import os
import sys

# -----------------------------------------------------------------------------
#  ROBUST IMPORT HANDLING 
# -----------------------------------------------------------------------------
try:
    from .views.dashboard_view import render_dashboard
    from .views.customers_view import render_customers
    from .views.products_view import render_products
    from .views.orders_view import render_orders
    from .views.orders_item_view import render_order_items
    from .views.reports_view import render_reports
except ImportError:
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    from app.views.dashboard_view import render_dashboard
    from app.views.customers_view import render_customers
    from app.views.products_view import render_products
    from app.views.orders_view import render_orders
    from app.views.orders_item_view import render_order_items
    from app.views.reports_view import render_reports


# =============================================================================
#   APP VERSION 2.0 
# =============================================================================
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("E-Commerce Manager Pro — Version 2.0")
        self.root.geometry("1380x820")
        self.root.minsize(1200, 760)

        # Track navigation state
        self.current_btn = None
        self.buttons = {}
        self.hero_image_ref = None

        # UI v2.0 setup
        self.setup_style()
        self.create_layout()
        self.show_welcome_screen()

    # =============================================================================
    #   STYLE SYSTEM 
    # =============================================================================
    def setup_style(self):
        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.colors = {
            "bg_dark": "#1e293b",
            "bg_light": "#f1f5f9",
            "accent": "#38bdf8",
            "accent_dark": "#0ea5e9",
            "text_light": "#ffffff",
            "text_dark": "#0f172a",
        }

        # Sidebar + content colors
        self.style.configure("Sidebar.TFrame", background=self.colors["bg_dark"])
        self.style.configure("Content.TFrame", background=self.colors["bg_light"])

        # Navigation buttons
        self.style.configure(
            "Nav.TButton",
            background=self.colors["bg_dark"],
            foreground=self.colors["text_light"],
            font=("Segoe UI", 12),
            padding=(20, 14),
            anchor="w",
            borderwidth=0
        )
        self.style.map("Nav.TButton", background=[("active", "#334155")])

        # Active button style
        self.style.configure(
            "Active.TButton",
            background="#0f172a",
            foreground=self.colors["accent"],
            font=("Segoe UI", 12, "bold"),
            padding=(20, 14),
            anchor="w",
            borderwidth=0
        )

        # Table styling (used by all views)
        self.style.configure(
            "Treeview",
            background="white",
            foreground=self.colors["text_dark"],
            fieldbackground="white",
            rowheight=38,
            borderwidth=0,
            font=("Segoe UI", 10)
        )
        self.style.configure(
            "Treeview.Heading",
            font=("Segoe UI", 11, "bold"),
            background="#e2e8f0",
            foreground=self.colors["text_dark"],
            relief="flat"
        )
        self.style.map("Treeview", background=[("selected", self.colors["accent"])])

    # =============================================================================
    #   LAYOUT SYSTEM 
    # =============================================================================
    def create_layout(self):
        # Sidebar
        self.sidebar = ttk.Frame(self.root, width=260, style="Sidebar.TFrame")
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        # Logo / brand block
        logo_frame = tk.Frame(self.sidebar, bg=self.colors["bg_dark"])
        logo_frame.pack(pady=25)

        tk.Label(
            logo_frame,
            text="ECOM PRO",
            font=("Segoe UI", 22, "bold"),
            fg=self.colors["accent"],
            bg=self.colors["bg_dark"]
        ).pack()

        tk.Label(
            logo_frame,
            text="Management System",
            font=("Segoe UI", 10),
            fg="#94a3b8",
            bg=self.colors["bg_dark"]
        ).pack()

        # Navigation Structure
        nav_items = [
            ("dashboard", "Dashboard", self.show_dashboard),
            ("customers", "Customers", self.show_customers),
            ("products", "Products", self.show_products),
            ("orders", "Orders", self.show_orders),
            ("items", "Order Items", self.show_items),
            ("reports", "Reports", self.show_reports),
        ]

        for key, text, cmd in nav_items:
            func = partial(self.nav_click, key, cmd)
            button = ttk.Button(
                self.sidebar,
                text=text,
                command=func,
                cursor="hand2",
                style="Nav.TButton"
            )
            button.pack(fill="x", pady=4, padx=14)
            self.buttons[key] = button

        # Footer version label
        tk.Label(
            self.sidebar,
            text="Version 2.0",
            font=("Segoe UI", 9),
            bg=self.colors["bg_dark"],
            fg="#64748b"
        ).pack(side="bottom", pady=20)

        # Content Frame
        self.content = ttk.Frame(self.root, style="Content.TFrame")
        self.content.pack(side="right", fill="both", expand=True)

    # =============================================================================
    #   NAVIGATION LOGIC
    # =============================================================================
    def nav_click(self, key, command):
        if self.current_btn:
            self.buttons[self.current_btn].configure(style="Nav.TButton")

        self.buttons[key].configure(style="Active.TButton")
        self.current_btn = key

        self.clear_content()
        command()

    def clear_content(self):
        for widget in self.content.winfo_children():
            widget.destroy()
        self.hero_image_ref = None

    # =============================================================================
    #   WELCOME SCREEN 
    # =============================================================================
    def show_welcome_screen(self):
        self.clear_content()

        # reset nav buttons
        if self.current_btn:
            self.buttons[self.current_btn].configure(style="Nav.TButton")
            self.current_btn = None

        self.welcome_frame = tk.Frame(self.content, bg=self.colors["bg_light"])
        self.welcome_frame.pack(fill="both", expand=True)

        # Path to welcome image
        img_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            "assets",
            "welcome_hero.jpg"
        )

        # load original image once (full resolution)
        try:
            self.original_hero_img = Image.open(img_path)
        except:
            tk.Label(self.welcome_frame, text="Welcome Image Not Found", font=("Arial", 20)).pack(expand=True)
            return

        # Create a label for dynamic image
        self.hero_label = tk.Label(self.welcome_frame, bg=self.colors["bg_light"])
        self.hero_label.place(relwidth=1, relheight=1)

        # overlay texts
        self.hero_title = tk.Label(
            self.welcome_frame,
            text="Welcome Back, Administrator!",
            font=("Segoe UI", 34, "bold"),
            fg="white",
            bg="#1e293b",
            padx=20,
            pady=10
        )
        self.hero_title.place(relx=0.5, rely=0.4, anchor="center")

        self.hero_sub = tk.Label(
            self.welcome_frame,
            text="Select an option from the sidebar to begin managing your store.",
            font=("Segoe UI", 16),
            fg="#cbd5e1",
            bg="#1e293b"
        )
        self.hero_sub.place(relx=0.5, rely=0.5, anchor="center")

        # BIND window resize event
        self.content.bind("<Configure>", self.resize_welcome_image)

    # =============================================================================
    #   RESIZE LOGIC FOR HERO IMAGE
    # =============================================================================
    def resize_welcome_image(self, event):
        if event.width < 400 or event.height < 300:
            return  # avoid weird small resizing

        # dynamically resize original image
        resized = self.original_hero_img.resize(
            (event.width, event.height),
            Image.Resampling.LANCZOS
        )

        self.hero_image_ref = ImageTk.PhotoImage(resized)
        self.hero_label.config(image=self.hero_image_ref)


    # =============================================================================
    #   PAGE ROUTERS (CALL VIEW FILES)
    # =============================================================================
    def show_dashboard(self): render_dashboard(self.content)
    def show_customers(self): render_customers(self.content)
    def show_products(self): render_products(self.content)
    def show_orders(self): render_orders(self.content)
    def show_items(self): render_order_items(self.content)
    def show_reports(self): render_reports(self.content)


# =============================================================================
#   EXECUTION ENTRY POINT
# =============================================================================
if __name__ == "__main__":
    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    except Exception:
        pass

    root = tk.Tk()
    root.update_idletasks()
    App(root)
    root.mainloop()


