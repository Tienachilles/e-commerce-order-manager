from app.core.connection import (
    fetch_all_customers,
    fetch_all_products,
    fetch_all_orders,
    fetch_order_items
)

class DashboardController:
    def get_kpis(self):
        customers = fetch_all_customers()
        products = fetch_all_products()
        orders = fetch_all_orders()
        items = fetch_order_items()

        total_customers = len(customers)
        total_products = len(products)
        total_orders = len(orders)

        revenue = 0
        for o in items:
            qty = float(o[2])
            price = float(o[3])
            revenue += qty * price

        return {
            "customers": total_customers,
            "products": total_products,
            "orders": total_orders,
            "revenue": revenue,
            "items": items,
            "products_raw": products
        }
