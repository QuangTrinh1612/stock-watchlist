from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.route.home import router as home_router
from app.route.api_watchlist import router as watchlist_router
from app.route.api_stock import router as stock_router

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Include routers
app.include_router(home_router)
app.include_router(watchlist_router)
app.include_router(stock_router)

# Run using uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)