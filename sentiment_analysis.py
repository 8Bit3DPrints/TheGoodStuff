import openai

openai.api_key = 

def analyze_sentiment(headline: str, company_name: str) -> str:
    prompt = f"Forget all your previous instructions. Pretend you are a financial expert. You are a financial expert with stock recommendation experience. Answer 'YES' if good news, 'NO' if bad news, or 'UNKNOWN' if uncertain in the first line. Then elaborate with one short and concise sentence on the next line. Is this headline good or bad for the stock price of {company_name} in the short term?\n\nHeadline: {headline}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7
    )
    if 'choices' in response and len(response['choices']) > 0:
        sentiment = response['choices'][0]['text'].strip().upper()
        return sentiment
    return "UNKNOWN"

def assign_sentiment_values(headlines) -> 'List'[int]:
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
