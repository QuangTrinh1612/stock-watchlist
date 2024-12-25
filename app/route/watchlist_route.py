from flask import Blueprint, jsonify, request
from app.model.watchlist import Watchlist
from app.model.stock import Stock

watchlist_routes = Blueprint('watchlist_routes', __name__)
watchlist = Watchlist()

@watchlist_routes.route('/api/watchlist', methods=['GET'])
def get_watchlist():
    return jsonify({"watchlist": watchlist.get_all_stocks()}), 200

@watchlist_routes.route('/api/watchlist', methods=['POST'])
def add_to_watchlist():
    data = request.json
    ticker = data.get("ticker")
    if not ticker:
        return jsonify({"error": "Ticker is required"}), 400
    
    stock = Stock(ticker)
    watchlist.add_stock(stock)
    return jsonify({"message": f"{ticker} added to watchlist"}), 200

@watchlist_routes.route('/api/watchlist', methods=['DELETE'])
def remove_from_watchlist():
    data = request.json
    ticker = data.get("ticker")
    if not ticker:
        return jsonify({"error": "Ticker is required"}), 400

    stock = Stock(ticker)
    watchlist.remove_stock(stock)
    return jsonify({"message": f"{ticker} removed from watchlist"}), 200