# Quant Finance Platform

A real-time financial data platform with AI-based company ranking for quantitative finance users.

## Features

- **Real-time Financial Data**: Fetch live stock data using yfinance
- **AI-Based Ranking**: Quantitative algorithm that ranks companies based on financial metrics
- **Sector Analysis**: Compare companies within their sectors
- **RESTful API**: FastAPI backend for easy integration
- **Multi-stock Comparison**: Compare multiple stocks simultaneously

## Quick Start

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Test the Platform**
   ```bash
   python test_platform.py
   ```

3. **Start the API Server**
   ```bash
   python main.py
   ```

4. **Access the API**
   - API Documentation: http://localhost:8000/docs
   - Get stock data: http://localhost:8000/stock/AAPL
   - Get sector rankings: http://localhost:8000/rankings/Technology

## API Endpoints

### Stock Data
```
GET /stock/{symbol}
```
Returns comprehensive stock data including financial metrics.

### Sector Rankings
```
GET /rankings/{sector}?limit=10
```
Returns AI-based rankings for companies in a sector.

### Stock Comparison
```
GET /compare?symbols=AAPL,MSFT,GOOGL
```
Compares multiple stocks with detailed analysis.

## Ranking Algorithm

The AI ranking system evaluates companies based on:

- **Valuation Metrics**: PE ratio, PB ratio
- **Profitability**: ROE, profit margins
- **Growth**: Revenue growth rates
- **Financial Health**: Debt-to-equity ratio
- **Market Momentum**: Price performance

Each metric is weighted and normalized to produce a composite score (0-100).

## Supported Sectors

- Technology
- Healthcare
- Financial
- Energy
- Consumer

## Configuration

Create a `.env` file for optional API keys:
```
ALPHA_VANTAGE_KEY=your_key_here
FINNHUB_KEY=your_key_here
```

## Example Usage

```python
from src.data_fetcher import DataFetcher
from src.ranking_engine import RankingEngine

# Fetch stock data
fetcher = DataFetcher()
stock_data = await fetcher.get_stock_data("AAPL")

# Get sector rankings
engine = RankingEngine()
rankings = await engine.rank_sector("Technology", limit=10)
```

## Next Steps

- Add more data sources (Alpha Vantage, Finnhub)
- Implement machine learning models for predictions
- Add technical analysis indicators
- Create a web frontend
- Add portfolio optimization features