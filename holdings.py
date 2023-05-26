import requests

def fetch_top_holdings():
    url = "https://query1.finance.yahoo.com/v1/finance/quote"
    params = {
        'symbols': 'SPY',
        'fields': 'topHoldings'
    }
    response = requests.get(url, params=params)
    data = response.json()
    if 'quoteResponse' in data and 'result' in data['quoteResponse']:
        result = data['quoteResponse']['result']
        if len(result) > 0 and 'topHoldings' in result[0]:
            holdings = result[0]['topHoldings']['holding']
            return holdings
    return []

top_holdings = fetch_top_holdings()
print(top_holdings)

