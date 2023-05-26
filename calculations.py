def assign_sentiment_values(headlines):
    sentiment_values = []
    for headline in headlines:
        sentiment = analyze_sentiment(headline['headline'], headline['company'])
        if sentiment == "YES":
            sentiment_values.append(1)
        elif sentiment == "UNKNOWN":
            sentiment_values.append(0)
        elif sentiment == "NO":
            sentiment_values.append(-1)
    return sentiment_values

sentiment_values = assign_sentiment_values(headlines)
print(sentiment_values)

def calculate_weighted_values(sentiment_values, top_holdings):
    weighted_values = {}
    for i, company in enumerate(top_holdings):
        sentiment_sum = sum(
            sentiment_values[j] for j, headline in enumerate(headlines) if headline['symbol'] == company['symbol']
        )
        weighted_value = sentiment_sum / len(headlines)
        weight = float(company['percent']) / 10.0
        weighted_values[company['name']] = weighted_value * weight
    return weighted_values

weighted_values = calculate_weighted_values(sentiment_values, top_holdings)
print(weighted_values)

def get_trading_recommendation(weighted_values):
    average_weighted_value = sum(weighted_values.values()) / len(weighted_values)
    if average_weighted_value >= 7:
        return "Buy Calls"
    elif average_weighted_value >= 4:
        return "Don't Trade Today"
    else:
        return "Buy Puts"

recommendation = get_trading_recommendation(weighted_values)
print(recommendation)

