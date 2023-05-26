import openai


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

