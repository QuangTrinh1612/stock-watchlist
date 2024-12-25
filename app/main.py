from flask import Flask
from app.route.stock_route import stock_routes
from app.route.watchlist_route import watchlist_routes
from app.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Register Blueprints
    app.register_blueprint(stock_routes)
    app.register_blueprint(watchlist_routes)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run()