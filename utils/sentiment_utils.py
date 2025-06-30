import requests
import pandas as pd
from datetime import datetime, timedelta
import os
from textblob import TextBlob
import matplotlib.pyplot as plt

# News API Config - Use environment variable or placeholder
NEWS_API_KEY = os.getenv("NEWS_API_KEY", "10918c1fb6964375be2d936bdea986a5")  # Set your API key as environment variable
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

def analyze_sentiment(stock, start_date, end_date):
    """
    Analyze sentiment for a given stock using news articles.
    
    Args:
        stock (str): Stock symbol
        start_date (date): Start date for analysis
        end_date (date): End date for analysis
    
    Returns:
        tuple: (sentiment_df, summary, top_news_df)
    """
    today = datetime.today().date()
    max_allowed = today - timedelta(days=30)

    if start_date < max_allowed:
        error_msg = "❌ Free API supports only last 30 days! Please upgrade to premium."
        return pd.DataFrame(), error_msg, pd.DataFrame()

    # Prepare query
    params = {
        "q": f"{stock} stock",
        "from": start_date.strftime("%Y-%m-%d"),
        "to": end_date.strftime("%Y-%m-%d"),
        "sortBy": "relevancy",
        "apiKey": NEWS_API_KEY,
        "language": "en",
        "pageSize": 50
    }

    try:
        response = requests.get(NEWS_ENDPOINT, params=params, timeout=10)
        if response.status_code != 200:
            error_msg = f"⚠️ API Error: {response.json().get('message', 'Unknown error')}"
            return pd.DataFrame(), error_msg, pd.DataFrame()

        articles = response.json().get("articles", [])
        if not articles:
            error_msg = "⚠️ No articles found in this date range."
            return pd.DataFrame(), error_msg, pd.DataFrame()

        results = []
        for article in articles:
            title = article.get('title', '')
            published_at = article.get('publishedAt', '')[:10]
            url = article.get('url', '')
            
            if title:
                # Use TextBlob for sentiment analysis
                blob = TextBlob(title)
                sentiment_score = blob.sentiment.polarity
                
                # Convert score to label
                if sentiment_score > 0.1:
                    sentiment_label = "POSITIVE"
                elif sentiment_score < -0.1:
                    sentiment_label = "NEGATIVE"
                else:
                    sentiment_label = "NEUTRAL"
                
                results.append({
                    "Date": published_at,
                    "Headline": title,
                    "URL": url,
                    "Sentiment": sentiment_label,
                    "Score": round(sentiment_score, 3)
                })

        if not results:
            error_msg = "⚠️ No valid articles found for sentiment analysis."
            return pd.DataFrame(), error_msg, pd.DataFrame()

        df = pd.DataFrame(results)
        df['Date'] = pd.to_datetime(df['Date'])
        
        # Calculate overall sentiment summary
        positive_count = len(df[df['Sentiment'] == 'POSITIVE'])
        negative_count = len(df[df['Sentiment'] == 'NEGATIVE'])
        neutral_count = len(df[df['Sentiment'] == 'NEUTRAL'])
        
        if positive_count > negative_count:
            summary = "POSITIVE"
        elif negative_count > positive_count:
            summary = "NEGATIVE"
        else:
            summary = "NEUTRAL"

        # Top 5 influential news (by absolute score)
        top_news_df = df.sort_values(by="Score", key=abs, ascending=False).head(5)

        return df, summary, top_news_df

    except requests.exceptions.RequestException as e:
        error_msg = f"⚠️ Network Error: {str(e)}"
        return pd.DataFrame(), error_msg, pd.DataFrame()
    except Exception as e:
        error_msg = f"⚠️ Unexpected Error: {str(e)}"
        return pd.DataFrame(), error_msg, pd.DataFrame()


def plot_sentiment(df):
    """
    Create a sentiment distribution plot.
    
    Args:
        df (DataFrame): DataFrame with sentiment data
    
    Returns:
        matplotlib.figure.Figure: The plot figure
    """
    if df.empty:
        # Return empty plot if no data
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.text(0.5, 0.5, 'No data available', ha='center', va='center', transform=ax.transAxes)
        ax.set_title("Sentiment Distribution")
        return fig
    
    sentiment_counts = df["Sentiment"].value_counts()
    colors = ['green' if label == 'POSITIVE' else 'red' if label == 'NEGATIVE' else 'gray' 
              for label in sentiment_counts.index]

    fig, ax = plt.subplots(figsize=(8, 6))
    bars = sentiment_counts.plot(kind='bar', color=colors, ax=ax)
    ax.set_title("Sentiment Distribution", fontsize=14, fontweight='bold')
    ax.set_ylabel("Article Count", fontsize=12)
    ax.set_xlabel("Sentiment", fontsize=12)
    
    # Add value labels on bars
    for i, v in enumerate(sentiment_counts.values):
        ax.text(i, v + 0.1, str(v), ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    return fig
