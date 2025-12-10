import tkinter as tk
from tkinter import ttk
from functools import partial
from PIL import Image, ImageTk
import os
import sys

# --- 1. ROBUST IMPORT HANDLING ---
# This block allows the script to run as a module (python -m app.main)
# or directly (python app/main.py) without import errors.
try:
    from .views.dashboard_view import render_dashboard
    from .views.customers_view import render_customers
    from .views.products_view import render_products
    from .views.orders_view import render_orders
    from .views.orders_item_view import render_order_items
    from .views.reports_view import render_reports
except ImportError:
    # Add project root to python path if running directly
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    from app.views.dashboard_view import render_dashboard
    from app.views.customers_view import render_customers
    from app.views.products_view import render_products
    from app.views.orders_view import render_orders
    from app.views.orders_item_view import render_order_items
    from app.views.reports_view import render_reports

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("E-Commerce Manager Pro")
        # Increased default size to accommodate the hero image better
        self.root.geometry("1366x768") 
        self.root.minsize(1100, 650)

        # State tracking
        self.current_btn = None
        self.buttons = {}
        # Variable to keep image reference, preventing garbage collection
        self.hero_image_ref = None 

        self.setup_style()
        self.create_layout()
        
        # --- IMPORTANT CHANGE ---
        # Start with Welcome Screen instead of Dashboard
        self.show_welcome_screen()

    def setup_style(self):
        self.style = ttk.Style()
        self.style.theme_use("clam")

        # --- COLORS (Modern Palette) ---
        self.colors = {
            "bg_sidebar": "#1e293b",       # Dark Blue-Grey
            "bg_content": "#f8fafc",       # Very Light Grey
            "btn_default": "#1e293b",
            "btn_hover": "#334155",
            "btn_active": "#0f172a",
            "text_light": "#ffffff",
            "accent": "#38bdf8"            # Light Blue Highlight
        }

        # --- CONFIGURE STYLES ---
        self.style.configure("Sidebar.TFrame", background=self.colors["bg_sidebar"])
        self.style.configure("Content.TFrame", background=self.colors["bg_content"])

        # Navigation Buttons (Base Style)
        self.style.configure(
            "Nav.TButton",
            background=self.colors["btn_default"],
            foreground=self.colors["text_light"],
            font=("Segoe UI", 11),
            borderwidth=0,
            anchor="w",
            padding=(20, 12)
        )

        # Hover Effect
        self.style.map(
            "Nav.TButton",
            background=[("active", self.colors["btn_hover"])],
            foreground=[("active", self.colors["text_light"])]
        )

        # Active State Style
        self.style.configure(
            "Active.TButton",
            background=self.colors["btn_active"],
            foreground=self.colors["accent"],
            font=("Segoe UI", 11, "bold"),
            borderwidth=0,
            anchor="w",
            padding=(20, 12)
        )
        self.style.map("Active.TButton", background=[("active", self.colors["btn_active"])])

        # Remove focus ring layout hack
        self.style.layout(
            "Nav.TButton", 
            [('Button.padding', {'children': [('Button.label', {'side': 'left', 'expand': 1})], 'sticky': 'nswe'})]
        )
        self.style.layout(
            "Active.TButton", 
            [('Button.padding', {'children': [('Button.label', {'side': 'left', 'expand': 1})], 'sticky': 'nswe'})]
        )

        # Treeview Styles
        self.style.configure(
            "Treeview",
            background="white",
            fieldbackground="white",
            foreground="#333",
            rowheight=35,
            font=("Segoe UI", 10),
            borderwidth=0
        )
        self.style.configure(
            "Treeview.Heading",
            font=("Segoe UI", 10, "bold"),
            background="#e2e8f0",
            foreground="#1e293b",
            relief="flat"
        )
        self.style.map("Treeview", background=[("selected", "#38bdf8")])

    def create_layout(self):
        # Sidebar Container
        self.sidebar = ttk.Frame(self.root, width=240, style="Sidebar.TFrame")
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        # Logo Area
        logo_frame = tk.Frame(self.sidebar, bg=self.colors["bg_sidebar"], height=80)
        logo_frame.pack(fill="x", pady=(20, 20))
        
        lbl_logo = tk.Label(
            logo_frame, 
            text="ECOM ADMIN", 
            font=("Segoe UI", 20, "bold"),
            fg=self.colors["accent"],
            bg=self.colors["bg_sidebar"]
        )
        lbl_logo.pack()
        
        lbl_sub = tk.Label(
            logo_frame, 
            text="Management System", 
            font=("Segoe UI", 9),
            fg="#94a3b8",
            bg=self.colors["bg_sidebar"]
        )
        lbl_sub.pack()

        # Navigation Items (Key is lowercase)
        self.nav_items = [
            ("dashboard", "📊  Dashboard", self.show_dashboard),
            ("customers", "👥  Customers", self.show_customers),
            ("products", "📦  Products", self.show_products),
            ("orders", "🛒  Orders", self.show_orders),
            ("items", "🧾  Order Items", self.show_items),
            ("reports", "📈  Reports", self.show_reports),
        ]

        # Create Buttons
        for key, text, cmd in self.nav_items:
            func = partial(self.nav_click, key, cmd)
            btn = ttk.Button(
                self.sidebar, 
                text=text, 
                command=func, 
                style="Nav.TButton",
                cursor="hand2"
            )
            btn.pack(fill="x", pady=2, padx=10)
            self.buttons[key] = btn

        # Footer
        lbl_footer = tk.Label(
            self.sidebar,
            text="v1.0.0",
            fg="#64748b",
            bg=self.colors["bg_sidebar"],
            font=("Segoe UI", 8)
        )
        lbl_footer.pack(side="bottom", pady=20)

        # Content Area
        self.content = ttk.Frame(self.root, style="Content.TFrame")
        self.content.pack(side="right", fill="both", expand=True)

    def nav_click(self, key, command):
        # 1. Reset old button style
        if self.current_btn:
            self.buttons[self.current_btn].configure(style="Nav.TButton")
        
        # 2. Set new button style (Active)
        self.buttons[key].configure(style="Active.TButton")
        self.current_btn = key

        # 3. Change View
        self.clear_content()
        command()

    def clear_content(self):
        # Clear all widgets in content frame
        for widget in self.content.winfo_children():
            widget.destroy()
        # Reset image reference to free memory
        self.hero_image_ref = None

    # =========================================
    #  SHOW WELCOME SCREEN
    # =========================================
    def show_welcome_screen(self):
        self.clear_content()
        
        # Reset nav buttons (none selected)
        if self.current_btn:
            self.buttons[self.current_btn].configure(style="Nav.TButton")
            self.current_btn = None

        # Frame for welcome screen
        welcome_frame = tk.Frame(self.content, bg=self.colors["bg_content"])
        welcome_frame.pack(fill="both", expand=True)

        # --- ROBUST PATH FINDING ---
        # Determines the absolute path to the project root to find assets
        current_dir = os.path.dirname(os.path.abspath(__file__)) # .../app
        project_root = os.path.dirname(current_dir)              # .../ecommerce-order-manager
        image_path = os.path.join(project_root, "assets", "welcome_hero.jpg")

        print(f"DEBUG: Loading welcome image from: {image_path}")

        try:
            # 1. Open image with Pillow
            pil_img = Image.open(image_path)
            
            # 2. Resize to cover the area
            canvas_width = self.content.winfo_width() or 1100 
            canvas_height = self.content.winfo_height() or 700
            
            # Use LANCZOS for high quality downsampling
            resized_img = pil_img.resize((canvas_width, canvas_height), Image.Resampling.LANCZOS)
            
            # 3. Convert to Tkinter format
            tk_img = ImageTk.PhotoImage(resized_img)
            
            # IMPORTANT: Keep reference
            self.hero_image_ref = tk_img

            # 4. Display Image
            img_label = tk.Label(welcome_frame, image=tk_img, bg=self.colors["bg_content"])
            img_label.place(x=0, y=0, relwidth=1, relheight=1)

            # 5. Overlay Text
            title_lbl = tk.Label(
                welcome_frame, 
                text="Welcome Back, Administrator!", 
                font=("Segoe UI", 32, "bold"),
                fg="white",
                bg="#1e293b",
                padx=20, pady=10
            )
            title_lbl.place(relx=0.5, rely=0.4, anchor="center")
            
            sub_lbl = tk.Label(
                welcome_frame, 
                text="Select an option from the sidebar to begin managing your store.", 
                font=("Segoe UI", 14),
                fg="#cbd5e1",
                bg="#1e293b",
                padx=20, pady=5
            )
            sub_lbl.place(relx=0.5, rely=0.5, anchor="center")
            
        except FileNotFoundError:
            # Fallback if image missing
            err_frame = tk.Frame(welcome_frame, bg="#fee2e2")
            err_frame.pack(expand=True, fill="both", padx=50, pady=50)
            tk.Label(err_frame, text="⚠️ IMAGE NOT FOUND", font=("Arial", 20, "bold"), fg="red", bg="#fee2e2").pack(pady=10)
            tk.Label(err_frame, text=f"Path checked: {image_path}", font=("Arial", 10), bg="#fee2e2").pack()
        except Exception as e:
             tk.Label(
                welcome_frame, 
                text=f"Error loading image: {e}",
                font=("Segoe UI", 12), fg="red", bg=self.colors["bg_content"]
            ).pack(expand=True)

    # --- Wrapper functions ---
    def show_dashboard(self): render_dashboard(self.content)
    def show_customers(self): render_customers(self.content)
    def show_products(self): render_products(self.content)
    def show_orders(self): render_orders(self.content)
    def show_items(self): render_order_items(self.content)
    def show_reports(self): render_reports(self.content)

if __name__ == "__main__":
    root = tk.Tk()
    root.update_idletasks() 
    App(root)
    root.mainloop()
