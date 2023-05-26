from typing import Dict
from sentiment_analysis import assign_sentiment_values, calculate_weighted_values
from web_scraping import scrape_headlines
from caching import load_cached_headlines, save_headlines_to_cache

def get_trading_recommendation() -> str:
    headlines = scrape_headlines()
    sentiment_values = assign_sentiment_values(headlines)
    weighted_values = calculate_weighted_values(sentiment_values)
    recommendation = calculate_trading_recommendation(weighted_values)
    return recommendation

def calculate_trading_recommendation(weighted_values: Dict[str, float]) -> str:
    average_weighted_value = sum(weighted_values.values()) / len(weighted_values)
    if average_weighted_value >= 7:
        return "Buy Calls"
    elif average_weighted_value >= 4:
        return "Don't Trade Today"
    else:
        return "Buy Puts"

