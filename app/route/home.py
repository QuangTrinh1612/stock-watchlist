from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

router = APIRouter()
templates = Jinja2Templates(directory="app/template")

@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Serve the homepage."""
    return templates.TemplateResponse("index.html", {"request": request})

@router.get("/stock/{ticker}", response_class=HTMLResponse)
async def stock_details(request: Request, ticker: str):
    """Serve the stock details page."""
    return templates.TemplateResponse("stock_details.html", {"request": request, "ticker": ticker})