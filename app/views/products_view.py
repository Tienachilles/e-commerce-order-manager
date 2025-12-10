import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os
from app.controllers.products_controller import ProductsController
from app.core.validators import is_positive_number

# Image cache to prevent multiple reloads causing lag
image_cache = {}

def render_products(parent):
    ctrl = ProductsController()
    
    # --- 1. SETUP SCROLLABLE FRAME ---
    # Main Wrapper
    wrapper = tk.Frame(parent, bg="#f1f5f9")
    wrapper.pack(fill="both", expand=True)

    # Canvas and Scrollbar
    canvas = tk.Canvas(wrapper, bg="#f1f5f9", highlightthickness=0)
    scrollbar = ttk.Scrollbar(wrapper, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#f1f5f9")

    # Function to update scroll region
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Scrollbar layout (Canvas left, Scrollbar right)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # --- 2. HEADER & TOOLBAR (Fixed at top) ---
    toolbar = tk.Frame(parent, bg="#f1f5f9", pady=10, padx=20)
    # Use pack 'before' to place it above the wrapper
    toolbar.pack(side="top", fill="x", before=wrapper)

    tk.Label(toolbar, text="Product Catalog", font=("Segoe UI", 20, "bold"), bg="#f1f5f9", fg="#1e293b").pack(side="left")

    # --- Add Product Button ---
    def show_add_dialog():
        w = tk.Toplevel()
        w.title("Add Product")
        w.geometry("320x300")
        w.configure(bg="white")
        
        ttk.Label(w, text="Product ID (e.g., P099)").pack(pady=5)
        e_id = ttk.Entry(w); e_id.pack()
        
        ttk.Label(w, text="Product Name").pack(pady=5)
        e_name = ttk.Entry(w); e_name.pack()
        
        ttk.Label(w, text="Price ($)").pack(pady=5)
        e_price = ttk.Entry(w); e_price.pack()

        def save():
            pid, name, price = e_id.get(), e_name.get(), e_price.get()
            if not is_positive_number(price):
                messagebox.showerror("Error", "Invalid price")
                return
            try:
                ctrl.add(pid, name, float(price))
                w.destroy()
                # Reload interface to show new product
                render_products(parent) 
            except Exception as e:
                messagebox.showerror("Error", str(e))

        ttk.Button(w, text="Save Product", command=save).pack(pady=20)

    btn_add = tk.Button(
        toolbar, text="+ Add New Product", 
        bg="#3b82f6", fg="white", font=("Segoe UI", 10, "bold"),
        relief="flat", padx=15, pady=5, cursor="hand2",
        command=show_add_dialog
    )
    btn_add.pack(side="right")

    # --- 3. PRODUCT GRID DISPLAY LOGIC ---
    products = ctrl.list() # Fetch list from DB
    
    # Number of columns (4 products per row)
    COLUMNS = 4
    
    # Function to find image in assets/products folder
    def get_product_image(pid):
        if pid in image_cache:
            return image_cache[pid]
            
        # Prioritize .jpg, then .png
        paths = [
            os.path.join("assets", "products", f"{pid}.jpg"),
            os.path.join("assets", "products", f"{pid}.png"),
            os.path.join("assets", "products", "default.png") # Fallback image
        ]
        
        found_path = None
        for p in paths:
            if os.path.exists(p):
                found_path = p
                break
        
        # Thumbnail size
        img_size = (150, 150) 
        
        tk_img = None
        if found_path:
            try:
                pil_img = Image.open(found_path)
                # Resize image maintaining high quality
                pil_img = pil_img.resize(img_size, Image.Resampling.LANCZOS)
                tk_img = ImageTk.PhotoImage(pil_img)
            except:
                pass
        
        # If no image, create a gray placeholder
        if not tk_img:
            img = Image.new('RGB', img_size, color='#e2e8f0')
            tk_img = ImageTk.PhotoImage(img)

        # Save to cache
        image_cache[pid] = tk_img
        return tk_img


    # Loop to draw each Card
    for index, item in enumerate(products):
        pid, name, price = item[0], item[1], item[2]
        
        # Calculate row/col position
        row = index // COLUMNS
        col = index % COLUMNS
        
        # Product Card Frame
        card = tk.Frame(scrollable_frame, bg="white", padx=10, pady=10)
        # Faux shadow effect (border width=1, relief=solid)
        card.configure(highlightbackground="#e2e8f0", highlightthickness=1)
        card.grid(row=row, column=col, padx=15, pady=15, sticky="nsew")
        
        # 1. Image
        img = get_product_image(pid)
        if img:
            lbl_img = tk.Label(card, image=img, bg="white")
            lbl_img.pack(pady=(0, 10))
            
        # 2. Name
        lbl_name = tk.Label(
            card, text=name, 
            font=("Segoe UI", 11, "bold"), 
            bg="white", fg="#1e293b",
            wraplength=140, justify="center"
        )
        lbl_name.pack(anchor="n")
        
        # 3. Price
        lbl_price = tk.Label(
            card, text=f"${price:,.2f}", 
            font=("Segoe UI", 10, "bold"), 
            bg="white", fg="#ef4444"
        )
        lbl_price.pack(anchor="n")
        
        # 4. ID
        tk.Label(card, text=f"#{pid}", font=("Segoe UI", 8), fg="#94a3b8", bg="white").pack(pady=(5,0))

    # --- 4. MOUSE SCROLL SUPPORT ---
    def _on_mousewheel(event):
        # Factor -1 ensures correct scroll direction
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    
    # Bind mouse wheel event to canvas
    canvas.bind_all("<MouseWheel>", _on_mousewheel)
