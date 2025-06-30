import yfinance as yf
import pandas as pd

stock_tickers = {
    "reliance": "RELIANCE.NS",
    "tcs": "TCS.NS",
    "infy": "INFY.NS",
    "hdfcbank": "HDFCBANK.NS",
    "icicibank": "ICICIBANK.NS",
    "hcltech": "HCLTECH.NS",
    "lt": "LT.NS",
    "sbin": "SBIN.NS",
    "wipro": "WIPRO.NS",
    "itc": "ITC.NS",
    "bajfinance": "BAJFINANCE.NS",
    "hindunilvr": "HINDUNILVR.NS",
    "kotakbank": "KOTAKBANK.NS",
    "asianpaint": "ASIANPAINT.NS",
    "ntpc": "NTPC.NS",
    "tatamotors": "TATAMOTORS.NS",
    "ongc": "ONGC.NS",
    "sunpharma": "SUNPHARMA.NS",
    "techm": "TECHM.NS",
    "powergrid": "POWERGRID.NS",
}

start_date = "2024-01-01"
end_date = "2025-05-28"

for name, ticker in stock_tickers.items():
    print(f"Fetching {ticker}...")
    df = yf.download(ticker, start=start_date, end=end_date)
    if not df.empty:
        df.reset_index(inplace=True)
        df.to_csv(f"{name}.csv", index=False)
        print(f"✅ Saved: {name}.csv")
    else:
        print(f"⚠️ No data for {ticker}")
