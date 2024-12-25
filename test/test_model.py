import pytest
from app.model.stock import Stock
from app.model.watchlist import Watchlist

def test_stock_model():
    stock = Stock("AAPL")
    assert stock.ticker == "AAPL"

def test_watchlist_model():
    watchlist = Watchlist()
    stock1 = Stock("AAPL")
    stock2 = Stock("MSFT")

    watchlist.add_stock(stock1)
    watchlist.add_stock(stock2)
    assert watchlist.get_all_stocks() == ["AAPL", "MSFT"]

    watchlist.remove_stock(stock1)
    assert watchlist.get_all_stocks() == ["MSFT"]
