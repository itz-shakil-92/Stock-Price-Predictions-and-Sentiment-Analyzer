import streamlit as st
from datetime import date, timedelta
import pandas as pd
import plotly.graph_objects as go
from utils.model_utils import load_model, predict_prices
from utils.sentiment_utils import analyze_sentiment
from utils.plotting_utils import plot_candlestick, plot_sentiment

# Set page config
st.set_page_config(page_title="Stock Insights", layout="wide")

# Title and Tabs
st.title("📈 Stock Price Prediction & Sentiment Analysis")
tabs = st.tabs(["🔮 Predict Stock Price", "📰 Analyze Sentiment"])

# Set default dates to today and a recent range
_today = date.today()
default_start = _today - timedelta(days=7)
default_end = _today

# If you see date picker errors, use Streamlit's 'Clear cache' option in the menu.

# STOCK LIST
stock_list = ["RELIANCE", "TCS", "INFY", "HDFCBANK", "ICICIBANK", "HCLTECH", "LT", "SBIN", "WIPRO", "ITC",
              "BAJFINANCE", "HINDUNILVR", "KOTAKBANK", "ASIANPAINT", "NTPC", "TATAMOTORS", "ONGC", "SUNPHARMA", "TECHM", "POWERGRID"]

# -------- TAB 1: Price Prediction --------
with tabs[0]:
    st.subheader("📊 Stock Price Prediction")

    stock = st.selectbox("Select Stock", options=stock_list)
    start_date = st.date_input("Prediction Start Date", value=default_start)
    if isinstance(start_date, tuple):
        start_date = start_date[0] if start_date else default_start
    end_date = st.date_input("Prediction End Date", value=default_end)
    if isinstance(end_date, tuple):
        end_date = end_date[0] if end_date else default_end

    plot_type = st.radio("Display Format", ["Tabulation", "Line Plot"], horizontal=True)

    # Validate date range
    date_error = None
    if start_date is None or end_date is None:
        date_error = "❌ Please select both start and end dates."
    elif end_date < start_date:
        date_error = "❌ End date must be after start date."
    elif (end_date - start_date).days > 30:
        date_error = "❌ Date range cannot exceed 30 days."

    if date_error:
        st.error(date_error)
    elif st.button("🚀 Predict Price"):
        pred_df, actual_df = predict_prices(stock, start_date, end_date)
        st.success("✅ Prediction Complete!")

        combined = pd.merge(actual_df, pred_df, on="Date", suffixes=("_Actual", "_Predicted"))

        if plot_type == "Tabulation":
            st.dataframe(combined, use_container_width=True)
        else:
            fig = plot_candlestick(combined)
            st.plotly_chart(fig, use_container_width=True)

# -------- TAB 2: Sentiment Analysis --------
with tabs[1]:
    st.subheader("🧠 Sentiment Analysis")

    stock = st.selectbox("Select Stock", options=stock_list, key="sent_stock")
    sentiment_start = st.date_input("Sentiment Start Date", value=default_start, key="sent_start")
    if isinstance(sentiment_start, tuple):
        sentiment_start = sentiment_start[0] if sentiment_start else default_start
    sentiment_end = st.date_input("Sentiment End Date", value=default_end, key="sent_end")
    if isinstance(sentiment_end, tuple):
        sentiment_end = sentiment_end[0] if sentiment_end else default_end

    sentiment_type = st.radio("Display Format", ["Tabulation", "Plot"], horizontal=True)

    # Validate date range
    sent_date_error = None
    if sentiment_start is None or sentiment_end is None:
        sent_date_error = "❌ Please select both start and end dates."
    elif sentiment_end < sentiment_start:
        sent_date_error = "❌ End date must be after start date."
    elif (sentiment_end - sentiment_start).days > 30:
        sent_date_error = "❌ Date range cannot exceed 30 days."

    if sent_date_error:
        st.error(sent_date_error)
    elif st.button("📥 Analyze Sentiment"):
        sent_df, summary, top_news_df = analyze_sentiment(stock, sentiment_start, sentiment_end)
        st.success(f"✅ Overall Sentiment: **{summary}**")

        if sentiment_type == "Tabulation":
            st.dataframe(sent_df, use_container_width=True)
        else:
            fig = plot_sentiment(sent_df)
            st.plotly_chart(fig, use_container_width=True)

        st.markdown("### 📰 Top 5 Influential News")
        for i, row in top_news_df.iterrows():
            st.markdown(f"**{i+1}.** [{row['Headline']}]({row['URL']}) — *{row['Sentiment']}* (Score: {row['Score']})")
