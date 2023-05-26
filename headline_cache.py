import hashlib
import json

CACHE_FILE = "headline_cache.json"

def load_cached_headlines():
    try:
        with open(CACHE_FILE, "r") as file:
            cache_data = json.load(file)
        return cache_data.get("headlines", [])
    except FileNotFoundError:
        return []

def save_headlines_to_cache(headlines):
    cache_data = {"headlines": headlines}
    with open(CACHE_FILE, "w") as file:
        json.dump(cache_data, file)

def scrape_headlines(companies):
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
            response = requests.get(url)
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
    save_headlines_to_cache(cached_headlines)
    return headlines

headlines = scrape_headlines(top_holdings)
print(headlines)

