from fastapi import APIRouter, HTTPException
from app.model.watchlist import Watchlist

router = APIRouter()
watchlist = Watchlist()

@router.get("/api/watchlist")
async def get_watchlist():
    """Retrieve all stocks in the watchlist."""
    return {"watchlist": watchlist.get_all_stocks()}

@router.post("/api/watchlist")
async def add_to_watchlist(ticker: str):
    """Add a stock to the watchlist."""
    if not ticker:
        raise HTTPException(status_code=400, detail="Invalid ticker")
    watchlist.add_stock(ticker)
    return {"message": f"{ticker} added to watchlist."}

@router.delete("/api/watchlist")
async def remove_from_watchlist(ticker: str):
    """Remove a stock from the watchlist."""
    if not ticker:
        raise HTTPException(status_code=400, detail="Invalid ticker")
    watchlist.remove_stock(ticker)
    return {"message": f"{ticker} removed from watchlist."}
