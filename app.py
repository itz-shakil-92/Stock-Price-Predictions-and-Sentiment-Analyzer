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

# STOCK LIST
stock_list = ["RELIANCE", "TCS", "INFY", "HDFCBANK", "ICICIBANK", "HCLTECH", "LT", "SBIN", "WIPRO", "ITC",
              "BAJFINANCE", "HINDUNILVR", "KOTAKBANK", "ASIANPAINT", "NTPC", "TATAMOTORS", "ONGC", "SUNPHARMA", "TECHM", "POWERGRID"]

# -------- TAB 1: Price Prediction --------
with tabs[0]:
    st.subheader("📊 Stock Price Prediction")

    stock = st.selectbox("Select Stock", options=stock_list)
    start_date = st.date_input("Prediction Start Date", value=date(2025, 6, 1))
    end_date = st.date_input("Prediction End Date", value=date(2025, 6, 28),
                             min_value=start_date, max_value=start_date + timedelta(days=30))

    plot_type = st.radio("Display Format", ["Tabulation", "Candle Plot"], horizontal=True)

    if st.button("🚀 Predict Price"):
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
    sentiment_start = st.date_input("Sentiment Start Date", value=date(2025, 6, 1), key="sent_start")
    sentiment_end = st.date_input("Sentiment End Date", value=date(2025, 6, 28), key="sent_end")

    sentiment_type = st.radio("Display Format", ["Tabulation", "Plot"], horizontal=True)

    if st.button("📥 Analyze Sentiment"):
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
