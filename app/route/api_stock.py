from fastapi import APIRouter, HTTPException
from app.service.stock_service import StockService

router = APIRouter()

@router.get("/api/stock/{ticker}/price")
async def get_stock_price(ticker: str):
    """Get the current stock price."""
    try:
        price = StockService.get_stock_price(ticker)
        return {"ticker": ticker, "price": price}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))