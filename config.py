import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # API Keys (optional for enhanced data)
    ALPHA_VANTAGE_KEY = os.getenv('ALPHA_VANTAGE_KEY')
    FINNHUB_KEY = os.getenv('FINNHUB_KEY')
    
    # Cache settings
    CACHE_DURATION = 300  # 5 minutes
    
    # Ranking weights (can be adjusted)
    RANKING_WEIGHTS = {
        'pe_ratio': -0.15,
        'pb_ratio': -0.10,
        'debt_to_equity': -0.15,
        'roe': 0.25,
        'revenue_growth': 0.20,
        'profit_margin': 0.20,
        'momentum': 0.15
    }
    
    # Sector thresholds for scoring
    SECTOR_BENCHMARKS = {
        'Technology': {'avg_pe': 25, 'avg_roe': 0.18},
        'Healthcare': {'avg_pe': 20, 'avg_roe': 0.15},
        'Financial': {'avg_pe': 12, 'avg_roe': 0.12},
        'Energy': {'avg_pe': 15, 'avg_roe': 0.10},
        'Consumer': {'avg_pe': 18, 'avg_roe': 0.14}
    }