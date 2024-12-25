import yfinance as yf

class StockService:
    @staticmethod
    def get_stock_data(ticker):
        """Fetch historical data for a stock."""
        stock = yf.Ticker(ticker)
        data = stock.history(period="1mo")
        if data.empty:
            raise ValueError(f"No data found for ticker: {ticker}")
        return data.to_dict(orient="index")

    @staticmethod
    def get_stock_price(ticker):
        """Fetch the latest closing price for a stock."""
        stock = yf.Ticker(ticker)
        data = stock.history(period="1d")
        if data.empty:
            raise ValueError(f"No price data found for ticker: {ticker}")
        return data['Close'].iloc[-1]