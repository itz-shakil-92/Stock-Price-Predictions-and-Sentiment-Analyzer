from transformers import pipeline
from newsapi import NewsApiClient
import pandas as pd

def analyze_sentiment(stock, start_date, end_date):
    newsapi = NewsApiClient(api_key='10918c1fb6964375be2d936bdea986a5')
    sentiment_model = pipeline("sentiment-analysis")

    articles = newsapi.get_everything(
        q=stock,
        from_param=start_date,
        to=end_date,
        sort_by='relevancy',
        language='en',
        page_size=20,
    )

    headlines = []
    for article in articles['articles']:
        title = article['title']
        desc = article.get('description', '')
        content = title + " " + desc
        sentiment = sentiment_model(content[:512])[0]

        headlines.append({
            'Headline': title,
            'Sentiment': sentiment['label'],
            'Score': round(sentiment['score'], 2),
            'URL': article['url']
        })

    df = pd.DataFrame(headlines)
    df_sorted = df.sort_values(by='Score', ascending=False).head(5)

    pos_count = (df_sorted['Sentiment'] == 'POSITIVE').sum()
    neg_count = (df_sorted['Sentiment'] == 'NEGATIVE').sum()
    summary = "Positive" if pos_count > neg_count else "Negative"

    return df_sorted[['Headline', 'Sentiment', 'Score', 'URL']], summary, df_sorted

