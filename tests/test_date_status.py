import pandas as pd
import app.services.reports_service as report

# tạo data giả để test
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
    # Tất cả Status phải thuộc danh sách hợp lệ
    valid_status = {"Pending", "Completed", "Cancelled"}
    assert all(s in valid_status for s in df["Status"])

def test_status_invalid(monkeypatch):
    monkeypatch.setattr(report, "fetch_all_orders", mock_orders_invalid_status)
    df = report.df_orders()
    valid_status = {"Pending", "Completed", "Cancelled"}
    # Phải phát hiện giá trị sai
    assert not all(s in valid_status for s in df["Status"])

# test date rule
from datetime import datetime

def test_date_not_future(monkeypatch):
    monkeypatch.setattr(report, "fetch_all_orders", mock_orders_invalid_date)
    df = report.df_orders()
    today = datetime.today().date()
    order_dates = pd.to_datetime(df["OrderDate"]).dt.date
    # Check có order nào trong tương lai
    assert all(d <= today for d in order_dates) == False

