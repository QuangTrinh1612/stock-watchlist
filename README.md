```
stock-watchlist/
│
├── app/
│   ├── __init__.py          # Initialize Flask app
│   ├── config.py            # Configuration settings (e.g., API keys, environment variables)
│   ├── models/
│   │   ├── __init__.py      # Initialize models package
│   │   ├── stock.py         # Stock model (OOP design)
│   │   ├── watchlist.py     # Watchlist model
│   ├── routes/
│   │   ├── __init__.py      # Initialize routes
│   │   ├── stock_routes.py  # API routes for stocks
│   │   ├── watchlist_routes.py  # API routes for watchlists
│   ├── services/
│   │   ├── __init__.py      # Initialize services package
│   │   ├── stock_service.py # Interact with yfinance
│   ├── templates/           # HTML files (web UI)
│   │   ├── base.html        # Base template (common layout)
│   │   ├── index.html       # Homepage (watchlist overview)
│   │   ├── stock_details.html  # Stock price chart/details
│   ├── static/              # Static files (CSS, JS, Images)
│   │   ├── css/
│   │   │   ├── styles.css   # Custom CSS for styling
│   │   ├── js/
│   │   │   ├── app.js       # JavaScript for interactivity
│   │   ├── images/          # Static images
│   ├── main.py              # Entry point for Flask application
│
├── tests/
│   ├── test_app.py          # Tests for the Flask application
│   ├── test_models.py       # Tests for models
│   ├── test_services.py     # Tests for services
│
├── requirements.txt         # Python dependencies
├── README.md                # Project description and instructions
└── .gitignore               # Ignored files and folders
```