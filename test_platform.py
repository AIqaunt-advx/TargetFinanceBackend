#!/usr/bin/env python3
"""
Simple CLI tool to test the quant finance platform
"""
import asyncio
import sys
from src.data_fetcher import DataFetcher
from src.ranking_engine import RankingEngine

async def test_stock_data(symbol: str):
    """Test fetching stock data"""
    print(f"\n=== Testing Stock Data for {symbol} ===")
    fetcher = DataFetcher()
    
    try:
        data = await fetcher.get_stock_data(symbol)
        print(f"Symbol: {data.symbol}")
        print(f"Current Price: ${data.current_price:.2f}")
        print(f"Day Change: {data.day_change_percent:.2f}%")
        print(f"PE Ratio: {data.pe_ratio}")
        print(f"ROE: {data.roe}")
        print(f"Sector: {data.sector}")
        return data
    except Exception as e:
        print(f"Error: {e}")
        return None

async def test_sector_ranking(sector: str):
    """Test sector ranking"""
    print(f"\n=== Testing Sector Ranking for {sector} ===")
    engine = RankingEngine()
    
    try:
        rankings = await engine.rank_sector(sector, limit=5)
        print(f"Top 5 stocks in {sector}:")
        for ranking in rankings:
            print(f"{ranking.rank}. {ranking.symbol} - Score: {ranking.score:.1f} - {ranking.recommendation}")
            print(f"   Strengths: {', '.join(ranking.strengths) if ranking.strengths else 'None'}")
    except Exception as e:
        print(f"Error: {e}")

async def test_stock_comparison(symbols: list):
    """Test stock comparison"""
    print(f"\n=== Comparing Stocks: {', '.join(symbols)} ===")
    engine = RankingEngine()
    
    try:
        comparison = await engine.compare_stocks(symbols)
        print(f"Best Performer: {comparison['best_performer']}")
        print(f"Average Score: {comparison['summary']['avg_score']:.1f}")
        
        for symbol, data in comparison['stocks'].items():
            print(f"\n{symbol}:")
            print(f"  Score: {data['score']:.1f}")
            print(f"  Price: ${data['current_price']:.2f}")
            print(f"  Recommendation: {data['recommendation']}")
    except Exception as e:
        print(f"Error: {e}")

async def main():
    """Main test function"""
    print("🚀 Quant Finance Platform Test Suite")
    
    # Test individual stock
    await test_stock_data("AAPL")
    
    # Test sector ranking
    await test_sector_ranking("Technology")
    
    # Test stock comparison
    await test_stock_comparison(["AAPL", "MSFT", "GOOGL"])
    
    print("\n✅ Testing complete!")

if __name__ == "__main__":
    asyncio.run(main())