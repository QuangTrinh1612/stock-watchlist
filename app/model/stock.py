import yfinance as yf

class Stock:
    def __init__(self, ticker):
        self.ticker = ticker
        self.data = None

    def fetch_data(self):
        self.data = yf.Ticker(self.ticker)
        return self.data.history(period="1mo")

    def get_price(self):
        if self.data:
            return self.data.history(period="1d")['Close'].iloc[-1]
        return None

    def get_chart_data(self):
        return self.fetch_data()