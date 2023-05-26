import requests
from bs4 import BeautifulSoup

def scrape_headlines(companies):
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
                if headline:
                    headlines.append({
                        'company': company['name'],
                        'symbol': company['symbol'],
                        'headline': headline
                    })
    return headlines

headlines = scrape_headlines(top_holdings)
print(headlines)

