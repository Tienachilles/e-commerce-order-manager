import pandas as pd
from app.core.connection import (
    fetch_all_customers,
    fetch_all_products,
    fetch_all_orders,
    fetch_order_items
)

# Convert SQL result to DataFrame
def df_customers():
    return pd.DataFrame(fetch_all_customers(), columns=["CustomerID", "Name"])

def df_products():
    return pd.DataFrame(fetch_all_products(), columns=["ProductID", "Name", "Price"])

def df_orders():
    return pd.DataFrame(fetch_all_orders(), columns=["OrderID", "CustomerID", "OrderDate", "Status"])

def df_items():
    return pd.DataFrame(fetch_order_items(), columns=["OrderID", "ProductID", "Quantity", "Price"])


# --------------------------
# REPORT FUNCTIONS
# --------------------------

def report_inner_join():
    return pd.merge(
        df_orders(),
        df_customers(),
        on="CustomerID",
        how="inner"
    )

def report_left_join():
    return pd.merge(
        df_orders(),
        df_customers(),
        on="CustomerID",
        how="left"
    )

def report_multi_join():
    s1 = pd.merge(df_orders(), df_items(), on="OrderID", how="inner")
    s2 = pd.merge(s1, df_products(), on="ProductID", how="inner")
    return s2


def report_order_summary():
    s = df_items()
    s["Total"] = s["Quantity"] * s["Price"]

    summary = s.groupby("OrderID")["Total"].sum().reset_index()
    summary.columns = ["OrderID", "OrderRevenue"]
    return summary
