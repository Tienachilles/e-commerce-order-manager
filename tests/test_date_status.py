import pandas as pd
import app.services.reports_service as report

# Create mock data for testing
def mock_orders_valid():
    return [
        (1, 1, "2025-12-01", "Completed"),
        (2, 2, "2025-12-05", "Pending"),
    ]

def mock_orders_invalid_status():
    return [
        (1, 1, "2025-12-01", "Done"),    # invalid status
        (2, 2, "2025-12-05", "Pending"),
    ]

def mock_orders_invalid_date():
    return [
        (1, 1, "2026-01-01", "Completed"),  # date in future
        (2, 2, "2025-12-05", "Pending"),
    ]

# test status
def test_status_valid(monkeypatch):
    monkeypatch.setattr(report, "fetch_all_orders", mock_orders_valid)
    df = report.df_orders()
    # All Statuses must belong to the valid list
    valid_status = {"Pending", "Completed", "Cancelled"}
    assert all(s in valid_status for s in df["Status"])

def test_status_invalid(monkeypatch):
    monkeypatch.setattr(report, "fetch_all_orders", mock_orders_invalid_status)
    df = report.df_orders()
    valid_status = {"Pending", "Completed", "Cancelled"}
    # Must detect invalid values
    assert not all(s in valid_status for s in df["Status"])

# test date
