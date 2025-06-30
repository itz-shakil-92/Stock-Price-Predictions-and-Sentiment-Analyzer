import pandas as pd
import pickle
from datetime import timedelta

def load_model(stock_name):
    with open(f"models/{stock_name.lower()}.pkl", "rb") as f:
        model = pickle.load(f)
    return model

def predict_prices(stock, start_date, end_date):
    df = pd.read_csv(f"data/{stock.lower()}.csv")
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date')

    df['SMA7'] = df['Close'].rolling(window=7).mean()
    df['SMA21'] = df['Close'].rolling(window=21).mean()
    from ta.momentum import RSIIndicator
    from ta.trend import MACD

    df['RSI'] = RSIIndicator(close=df['Close']).rsi()
    macd = MACD(close=df['Close'])
    df['MACD'] = macd.macd()
    df['MACD_Signal'] = macd.macd_signal()

    df.dropna(inplace=True)
    
    features = ['Open', 'High', 'Low', 'Volume', 'RSI', 'MACD', 'MACD_Signal', 'SMA7', 'SMA21']
    model = load_model(stock)

    predict_df = df[(df['Date'] >= pd.to_datetime(start_date)) & (df['Date'] <= pd.to_datetime(end_date))].copy()
    predict_df['Predicted_Close'] = model.predict(predict_df[features])

    pred_df = predict_df[['Date', 'Predicted_Close']].copy()
    pred_df.rename(columns={"Predicted_Close": "Close"}, inplace=True)

    actual_df = predict_df[['Date', 'Close']].copy()
    return pred_df, actual_df
