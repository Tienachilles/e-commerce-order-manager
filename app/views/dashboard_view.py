import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from app.controllers.dashboard_controller import DashboardController

def render_dashboard(parent):
    ctrl = DashboardController()
    data = ctrl.get_kpis()

    frame = ttk.Frame(parent)
    frame.pack(fill="both", expand=True, padx=10, pady=10)

    # KPI row
    kpi_frame = ttk.Frame(frame)
    kpi_frame.pack(fill="x")

    ttk.Label(kpi_frame, text=f"Customers\n{data['customers']}",
              anchor="center", background="#f0f0f0",
              font=("Segoe UI", 14)).pack(side="left", expand=True, fill="x", padx=5, pady=5)

    ttk.Label(kpi_frame, text=f"Products\n{data['products']}",
              anchor="center", background="#f0f0f0",
              font=("Segoe UI", 14)).pack(side="left", expand=True, fill="x", padx=5, pady=5)

    ttk.Label(kpi_frame, text=f"Orders\n{data['orders']}",
              anchor="center", background="#f0f0f0",
              font=("Segoe UI", 14)).pack(side="left", expand=True, fill="x", padx=5, pady=5)

    ttk.Label(kpi_frame, text=f"Revenue\n{data['revenue']:,.2f}",
              anchor="center", background="#f0f0f0",
              font=("Segoe UI", 14)).pack(side="left", expand=True, fill="x", padx=5, pady=5)

    # Bar chart
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

    chart_frame = ttk.Frame(frame)
    chart_frame.pack(fill="both", expand=True)

    fig = Figure(figsize=(6, 3), dpi=100)
    ax = fig.add_subplot(111)

    if values:
        ax.bar(labels, values)
        ax.set_title("Top 10 Product Revenue")
        ax.tick_params(axis='x', rotation=45)
    else:
        ax.text(0.5, 0.5, "No Data", ha='center')

    canvas = FigureCanvasTkAgg(fig, master=chart_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)
