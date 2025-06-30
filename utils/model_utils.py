import pandas as pd
import pickle
import os
from datetime import timedelta

def load_model(stock_name):
    """
    Load a trained model for the specified stock.
    
    Args:
        stock_name (str): Name of the stock
    
    Returns:
        model: The loaded machine learning model
    """
    model_path = f"models/{stock_name.lower()}.pkl"
    
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found: {model_path}")
    
    try:
        with open(model_path, "rb") as f:
            model = pickle.load(f)
        return model
    except Exception as e:
        raise Exception(f"Error loading model for {stock_name}: {str(e)}")

def predict_prices(stock, start_date, end_date):
    """
    Predict stock prices for the given date range.
    
    Args:
        stock (str): Stock symbol
        start_date (date): Start date for prediction
        end_date (date): End date for prediction
    
    Returns:
        tuple: (predicted_df, actual_df)
    """
    try:
        # Load data
        data_path = f"data/{stock.lower()}.csv"
        if not os.path.exists(data_path):
            raise FileNotFoundError(f"Data file not found: {data_path}")
        
        df = pd.read_csv(data_path)
        
        # Convert all required numeric columns and drop NaNs
        numeric_columns = ['Open', 'High', 'Low', 'Close', 'Volume']
        for col in numeric_columns:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce')
        
        # Drop rows with NaN values in any of the required columns
        df = df.dropna(subset=numeric_columns)
        
        # Check if we have enough data
        if len(df) == 0:
            raise ValueError("No valid numeric data found in the CSV file")
        
        df['Date'] = pd.to_datetime(df['Date'])
        df = df.sort_values('Date')

        # Calculate technical indicators
        df['SMA7'] = df['Close'].rolling(window=7).mean()
        df['SMA21'] = df['Close'].rolling(window=21).mean()
        
        try:
            from ta.momentum import RSIIndicator
            from ta.trend import MACD

            # Ensure Close is a pandas Series
            close_series = pd.Series(df['Close'].values, index=df.index)
            df['RSI'] = RSIIndicator(close=close_series).rsi()
            macd = MACD(close=close_series)
            df['MACD'] = macd.macd()
            df['MACD_Signal'] = macd.macd_signal()
        except ImportError:
            # Fallback if ta library is not available
            df['RSI'] = 50  # Default neutral RSI
            df['MACD'] = 0  # Default MACD
            df['MACD_Signal'] = 0  # Default MACD signal

        df.dropna(inplace=True)
        
        if df.empty:
            raise ValueError("No data available after preprocessing")
        
        features = ['Open', 'High', 'Low', 'Volume', 'RSI', 'MACD', 'MACD_Signal', 'SMA7', 'SMA21']
        
        # Check if all required features are available
        missing_features = [f for f in features if f not in df.columns]
        if missing_features:
            raise ValueError(f"Missing features: {missing_features}")
        
        # Load model
        model = load_model(stock)

        # Filter data for prediction period
        predict_df = df[(df['Date'] >= pd.to_datetime(start_date)) & 
                       (df['Date'] <= pd.to_datetime(end_date))].copy()
        
        if predict_df.empty:
            raise ValueError(f"No data available for the specified date range: {start_date} to {end_date}")

        # Make predictions
        predict_df['Predicted_Close'] = model.predict(predict_df[features])

        # Prepare return dataframes
        pred_df = predict_df[['Date', 'Predicted_Close']].copy()
        pred_df.columns = ['Date', 'Close']

        actual_df = predict_df[['Date', 'Close']].copy()
        
        return pred_df, actual_df

    except Exception as e:
        raise Exception(f"Error predicting prices for {stock}: {str(e)}")
