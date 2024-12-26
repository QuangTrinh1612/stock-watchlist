from app.service.stock_service import StockService
from app.model.watchlist import Watchlist

def stock_test(ticker):
    price = StockService.get_stock_price(ticker)
    print(f"StockPrice - ticker {ticker}, price: {price}")

    data = StockService.get_stock_data(ticker)
    print(f"StockData - ticker {ticker}, price: {data}")

def watchlist_test():
    watchlist = Watchlist()
    watchlist.add_stock("AAPL")
    print(watchlist.list_stocks())

if __name__ == "__main__":
    # stock_test("AAPL")
    watchlist_test()