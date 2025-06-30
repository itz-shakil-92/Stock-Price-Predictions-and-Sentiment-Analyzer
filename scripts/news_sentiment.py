from newsapi import NewsApiClient
from transformers import pipeline
import pandas as pd
from datetime import datetime

# 🔑 Replace with your actual key
newsapi = NewsApiClient(api_key='YOUR_NEWSAPI_KEY')

# Load sentiment classifier
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def get_sentiment_news(stock_name, start_date, end_date):
    articles = newsapi.get_everything(
        q=stock_name,
        from_param=start_date,
        to=end_date,
        sort_by='relevancy',
        language='en',
        page_size=20,
    )

    news_data = []
    for article in articles['articles']:
        title = article['title']
        content = f"{title} {article.get('description', '')}"
        sentiment = sentiment_pipeline(content[:512])[0]  # cap length

        news_data.append({
            'Headline': title,
            'Sentiment': sentiment['label'],
            'Score': round(sentiment['score'], 2),
            'URL': article['url']
        })

    df = pd.DataFrame(news_data)
    df_sorted = df.sort_values(by='Score', ascending=False).head(5)

    # Overall summary
    pos_count = (df_sorted['Sentiment'] == 'POSITIVE').sum()
    neg_count = (df_sorted['Sentiment'] == 'NEGATIVE').sum()
    overall = "Positive" if pos_count > neg_count else "Negative"

    return df_sorted, overall
