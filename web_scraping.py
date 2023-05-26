import requests
from bs4 import BeautifulSoup
from typing import List, Dict
from caching import load_cached_headlines, save_headlines_to_cache

def scrape_headlines() -> List[Dict[str, str]]:
    companies = fetch_top_holdings()
    cached_headlines = load_cached_headlines()
    headlines = []
    for company in companies:
        for website in [
            'https://finance.yahoo.com/news/',
            'https://www.google.com/finance/',
            'https://www.benzinga.com/news',
            'https://www.reuters.com/business/finance/',
            'https://markets.businessinsider.com/news',
            'https://www.bloomberg.com/markets',
            'https://seekingalpha.com/market-news'
        ]:
            url = f"{website}{company['symbol']}"
            try:
                response = requests.get(url)
                response.raise_for_status()
                soup = BeautifulSoup(response.text, 'html.parser')
                news_links = soup.find_all('a', href=True)
                for link in news_links:
                    headline = link.text.strip()
                    if headline and headline not in cached_headlines:
                        headlines.append({
                            'company': company['name'],
                            'symbol': company['symbol'],
                            'headline': headline
                        })
                        cached_headlines.append(headline)
            except requests.RequestException as e:
                print(f"Error while scraping headlines for {company['name']}: {e}")
    save_headlines_to_cache(cached_headlines)
    return headlines

def fetch_top_holdings() -> List[Dict[str, str]]:
    url = "https://query1.finance.yahoo.com/v1/finance/quote"
    params = {
        'symbols': 'SPY',
        'fields': 'topHoldings'
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        if 'quoteResponse' in data and 'result' in data['quoteResponse']:
            result = data['quoteResponse']['result']
            if len(result) > 0 and 'topHoldings' in result[0]:
                holdings = result[0]['topHoldings']['holding']
                return holdings
    except requests.RequestException as e:
        print(f"Error while fetching top holdings: {e}")
    return []

