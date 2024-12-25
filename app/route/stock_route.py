from flask import Blueprint, jsonify, request
from app.service.stock_service import StockService

stock_routes = Blueprint('stock_routes', __name__)

@stock_routes.route('/api/stock/<string:ticker>', methods=['GET'])
def get_stock(ticker):
    try:
        stock_data = StockService.get_stock_data(ticker)
        return jsonify({"ticker": ticker, "data": stock_data}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@stock_routes.route('/api/stock/<string:ticker>/price', methods=['GET'])
def get_stock_price(ticker):
    try:
        price = StockService.get_stock_price(ticker)
        return jsonify({"ticker": ticker, "price": price}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500