from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict, Optional
import uvicorn

from src.data_fetcher import DataFetcher
from src.ranking_engine import RankingEngine
from src.models import CompanyRanking, StockData

app = FastAPI(title="Quant Finance Platform", version="1.0.0")

# CORS middleware for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize core components
data_fetcher = DataFetcher()
ranking_engine = RankingEngine()

@app.get("/")
async def root():
    return {"message": "Quant Finance Platform API"}

@app.get("/stock/{symbol}", response_model=StockData)
async def get_stock_data(symbol: str):
    """Get real-time stock data for a symbol"""
    try:
        data = await data_fetcher.get_stock_data(symbol)
        return data
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Stock data not found: {str(e)}")

@app.get("/rankings/{sector}", response_model=List[CompanyRanking])
async def get_sector_rankings(sector: str, limit: int = 10):
    """Get AI-based rankings for companies in a sector"""
    try:
        rankings = await ranking_engine.rank_sector(sector, limit)
        return rankings
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ranking error: {str(e)}")

@app.get("/compare")
async def compare_stocks(symbols: str):
    """Compare multiple stocks (comma-separated symbols)"""
    try:
        symbol_list = [s.strip().upper() for s in symbols.split(",")]
        comparison = await ranking_engine.compare_stocks(symbol_list)
        return comparison
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Comparison error: {str(e)}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)