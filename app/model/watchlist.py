class Watchlist:
    def __init__(self):
        self.stocks = []

    def add_stock(self, stock):
        if stock not in self.stocks:
            self.stocks.append(stock)

    def remove_stock(self, stock):
        if stock in self.stocks:
            self.stocks.remove(stock)

    def get_all_stocks(self):
        return [stock.ticker for stock in self.stocks]