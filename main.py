from flask import Flask, render_template, request, jsonify
from app.service.stock_service import StockService
from app.model.watchlist import Watchlist

# Create a Flask app instance
def create_app():
    app = Flask(__name__, template_folder="app/template")
    app.config['SECRET_KEY'] = "your_secret_key"

    # Initialize Watchlist instance
    watchlist = Watchlist()

    @app.route("/")
    def home():
        """Render the homepage."""
        return render_template("index.html")

    @app.route("/stock/<string:ticker>")
    def stock_details(ticker):
        """Render the stock details page."""
        return render_template("stock_details.html", ticker=ticker)

    @app.route("/api/watchlist", methods=["GET", "POST", "DELETE"])
    def api_watchlist():
        """Handle watchlist API actions."""
        if request.method == "GET":
            return jsonify({"watchlist": watchlist.get_all_stocks()})
        elif request.method == "POST":
            data = request.get_json()
            ticker = data.get("ticker")
            if ticker:
                watchlist.add_stock(ticker)
                return jsonify({"message": f"{ticker} added to watchlist."}), 201
            return jsonify({"error": "Invalid ticker"}), 400
        elif request.method == "DELETE":
            data = request.get_json()
            ticker = data.get("ticker")
            if ticker:
                watchlist.remove_stock(ticker)
                return jsonify({"message": f"{ticker} removed from watchlist."}), 200
            return jsonify({"error": "Invalid ticker"}), 400

    @app.route("/api/stock/<string:ticker>/price", methods=["GET"])
    def api_stock_price(ticker):
        """Get the current stock price."""
        try:
            price = StockService.get_stock_price(ticker)
            return jsonify({"ticker": ticker, "price": price}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return app

# Run the app
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)