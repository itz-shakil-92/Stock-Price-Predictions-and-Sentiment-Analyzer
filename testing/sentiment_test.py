from datetime import date, timedelta
df, top_news = analyze_sentiment("RELIANCE", date.today() - timedelta(days=10), date.today())
print(df.head())
print("Top news:", top_news)
