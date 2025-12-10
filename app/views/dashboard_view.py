import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from app.controllers.dashboard_controller import DashboardController

def render_dashboard(parent):
    ctrl = DashboardController()
    data = ctrl.get_kpis()

    # Background color matches main theme (Light Grey)
    BG_COLOR = "#f1f5f9"
    
    # Main container (scrollable if needed, but using pack fill here)
    main_frame = tk.Frame(parent, bg=BG_COLOR)
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # --- TITLE ---
    tk.Label(
        main_frame, 
        text="Overview Dashboard", 
        font=("Segoe UI", 24, "bold"),
        bg=BG_COLOR, fg="#1e293b"
    ).pack(anchor="w", pady=(0, 20))

    # --- KPI CARDS ROW ---
    kpi_container = tk.Frame(main_frame, bg=BG_COLOR)
    kpi_container.pack(fill="x", pady=(0, 20))

    # Function to draw a single KPI card
    def create_card(parent, title, value, icon, color_border):
        # Card frame (white background, faux shadow using border)
        card = tk.Frame(parent, bg="white", padx=20, pady=15)
        
        # Colored strip on the left for accent
        strip = tk.Frame(card, bg=color_border, width=5)
        strip.pack(side="left", fill="y", padx=(0, 15))

        # Content
        content_frame = tk.Frame(card, bg="white")
        content_frame.pack(side="left", fill="both", expand=True)

        tk.Label(content_frame, text=title, font=("Segoe UI", 10, "bold"), fg="#64748b", bg="white").pack(anchor="w")
        tk.Label(content_frame, text=value, font=("Segoe UI", 18, "bold"), fg="#1e293b", bg="white").pack(anchor="w")
        
        # Icon (Emoji) on the right
        tk.Label(card, text=icon, font=("Segoe UI", 24), bg="white", fg="#cbd5e1").pack(side="right")
        
        return card

    # Data processing
    revenue_txt = f"${data['revenue']:,.2f}"
    
    # Draw 4 cards
    c1 = create_card(kpi_container, "TOTAL CUSTOMERS", str(data['customers']), "👥", "#3b82f6") # Blue
    c2 = create_card(kpi_container, "TOTAL PRODUCTS", str(data['products']), "📦", "#10b981")   # Green
    c3 = create_card(kpi_container, "TOTAL ORDERS", str(data['orders']), "🛒", "#f59e0b")     # Orange
    c4 = create_card(kpi_container, "TOTAL REVENUE", revenue_txt, "💰", "#ef4444")            # Red

    # Grid layout for cards (to keep them even)
    for i, card in enumerate([c1, c2, c3, c4]):
        card.pack(side="left", fill="both", expand=True, padx=10)


    # --- CHART SECTION ---
    # Frame containing the chart (white background, rounded corners)
    chart_wrapper = tk.Frame(main_frame, bg="white", padx=10, pady=10)
    chart_wrapper.pack(fill="both", expand=True, padx=10)

    # Process chart data
    products = {p[0]: p[1] for p in data["products_raw"]}
    rev_map = {}
    for item in data["items"]:
        pid = item[1]
        qty = float(item[2])
        price = float(item[3])
        rev_map[pid] = rev_map.get(pid, 0) + qty * price

    sorted_rev = sorted(rev_map.items(), key=lambda x: x[1], reverse=True)[:10]
    labels = [products.get(pid, pid) for pid, _ in sorted_rev]
    values = [v for _, v in sorted_rev]

    # Draw Matplotlib Chart
    # Match Figure background color with card white
    fig = Figure(figsize=(6, 4), dpi=100, facecolor='white') 
    ax = fig.add_subplot(111)
    
    # Axis background color
    ax.set_facecolor('white') 

    if values:
        bars = ax.bar(labels, values, color="#3b82f6", width=0.6)
        ax.set_title("Top 10 Products by Revenue", fontsize=12, fontweight='bold', pad=15, color="#1e293b")
        ax.set_ylabel("Revenue ($)", fontsize=10, color="#64748b")
        ax.tick_params(axis='x', rotation=30, colors="#64748b")
        ax.tick_params(axis='y', colors="#64748b")
        
        # Remove top and right spines for a cleaner look
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_color('#cbd5e1')
        ax.spines['bottom'].set_color('#cbd5e1')
        
    else:
        ax.text(0.5, 0.5, "No Data Available", ha='center', va='center', color="#94a3b8")
        ax.axis('off')

    canvas = FigureCanvasTkAgg(fig, master=chart_wrapper)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)
