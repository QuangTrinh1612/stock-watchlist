class Stock:
    """
    Represents a stock with a ticker symbol and associated details.
    """

    def __init__(self, ticker: str, price: float = None):
        self.ticker = ticker.upper()
        self.price = price

    def get_price(self) -> float:
        return self.price

    def update_price(self, new_price: float):
        """
        Updates the stock's price.
        """
        self.price = new_price

    def to_dict(self):
        """
        Converts the stock instance to a dictionary for JSON serialization.
        """
        return {
            "ticker": self.ticker,
            "price": self.price,
        }