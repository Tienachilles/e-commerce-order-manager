import pandas as pd
import app.services.reports_service as report # import cái file tính revenue, còn file export chỉ là xuất file thôi, # vì nó trong thư mục service, service là con của app nên phải ghi app.services.report

# phần dữ liệu giả lập thay vì data thật
def mock_fetch_order_items_case1():
    # OrderID, ProductID, Quantity, Price
    return [
        (1, 101, 2, 10),   # 2 * 10 = 20
        (1, 102, 1, 30),   # 1 * 30 = 30
        (2, 103, 3, 5),    # 3 * 5 = 15
    ]

def test_revenue_basic(monkeypatch):
    """Test tính doanh thu cơ bản."""
    
    monkeypatch.setattr(
        report, "fetch_order_items", mock_fetch_order_items_case1
    )

# Quantity hoặc Price = 0
def mock_fetch_order_items_zero():
    return [
        (1, 101, 0, 50),   # revenue = 0
        (1, 102, 5, 0),    # revenue = 0
        (2, 103, 1, 100),  # revenue = 100
    ]

def test_revenue_zero(monkeypatch):
    """Test xử lý Quantity/Price = 0."""    
    monkeypatch.setattr(
        report, "fetch_order_items", mock_fetch_order_items_zero
    )
    df = report.report_order_summary()
    expected = pd.DataFrame({
        "OrderID": [1, 2],
        "OrderRevenue": [0, 100]
    })
    pd.testing.assert_frame_equal(df, expected)

# Không có items
def mock_fetch_empty():
    return []

def test_revenue_empty(monkeypatch):
    """Test khi không có dữ liệu."""    
    monkeypatch.setattr(
        report, "fetch_order_items", mock_fetch_empty
    )

    df = report.report_order_summary()
    expected = pd.DataFrame(columns=["OrderID", "OrderRevenue"])
    pd.testing.assert_frame_equal(df, expected)

