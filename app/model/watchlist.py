from app.model.stock import Stock
import yfinance as yf

class Watchlist:
    """
    Represents a user's stock watchlist.
    """

    def __init__(self):
        self.stocks = {}

    def add_stock(self, ticker: str):
        """
        Adds a stock to the watchlist.
        """
        ticker = ticker.upper()
        if ticker in self.stocks:
            raise ValueError(f"Stock '{ticker}' is already in the watchlist.")
        self.stocks[ticker] = Stock(ticker)

    def remove_stock(self, ticker: str):
        """
        Removes a stock from the watchlist.
        """
        ticker = ticker.upper()
        if ticker not in self.stocks:
            raise ValueError(f"Stock '{ticker}' is not in the watchlist.")
        del self.stocks[ticker]

    def get_stock(self, ticker: str) -> Stock:
        """
        Retrieves a stock from the watchlist.
        """
        ticker = ticker.upper()
        if ticker not in self.stocks:
            raise ValueError(f"Stock '{ticker}' is not in the watchlist.")
        return self.stocks[ticker]

    def update_prices(self):
        """
        Updates the prices of all stocks in the watchlist.
        """
        tickers = list(self.stocks.keys())
        if not tickers:
            return
        try:
            data = yf.download(tickers, period="1d", interval="1d", progress=False)
            for ticker in tickers:
                if ticker in data.index:
                    latest_price = data.loc[ticker]["Close"]
                    self.stocks[ticker].update_price(latest_price)
        except Exception as e:
            print(f"Error updating prices: {e}")

    def list_stocks(self, update_prices=True):
        """
        Returns a list of all stocks in the watchlist.
        Updates their prices before returning if `update_prices` is True.
        """
        if update_prices:
            self.update_prices()
        return list(self.stocks.values())

    def to_dict(self):
        """
        Converts the watchlist to a dictionary for JSON serialization.
        """
        return {
            "watchlist": [stock.to_dict() for stock in self.stocks.values()]
        }