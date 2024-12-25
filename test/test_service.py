import pytest
from app.service.stock_service import StockService

def test_get_stock_data():
    data = StockService.get_stock_data("AAPL")
    assert "Close" in data[list(data.keys())[0]]

def test_get_stock_price():
    price = StockService.get_stock_price("AAPL")
    assert price > 0  # Ensure the price is a positive number
