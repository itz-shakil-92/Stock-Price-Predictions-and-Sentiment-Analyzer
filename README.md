# 📈 Stock Price Prediction & Sentiment Analysis

A comprehensive machine learning application that predicts stock prices and analyzes market sentiment using news data for Indian stocks.

## 🚀 Features

- **Stock Price Prediction**: ML-based forecasting for 20 major Indian stocks
- **Sentiment Analysis**: News sentiment analysis with scoring
- **Interactive Dashboard**: Streamlit-based web interface
- **Visual Analytics**: Candlestick charts and sentiment plots
- **Real-time Data**: Live stock data and news scraping

## 📊 Supported Stocks

The application supports 20 major Indian stocks:
- RELIANCE, TCS, INFY, HDFCBANK, ICICIBANK
- HCLTECH, LT, SBIN, WIPRO, ITC
- BAJFINANCE, HINDUNILVR, KOTAKBANK, ASIANPAINT
- NTPC, TATAMOTORS, ONGC, SUNPHARMA, TECHM, POWERGRID

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/stock-prediction-project.git
   cd stock-prediction-project
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

## 📁 Project Structure

```
Final_year_project/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── data/                 # Stock data CSV files
├── models/               # Trained ML models (.pkl files)
├── models_notebook/      # Jupyter notebooks for model training
├── scripts/              # Data scraping and utility scripts
└── utils/                # Utility modules
    ├── model_utils.py    # Model loading and prediction functions
    ├── plotting_utils.py # Visualization functions
    └── sentiment_utils.py # Sentiment analysis functions
```

## 🎯 Usage

### Stock Price Prediction
1. Select a stock from the dropdown
2. Choose prediction start and end dates
3. Select display format (Tabulation or Candle Plot)
4. Click "Predict Price" to get forecasts

### Sentiment Analysis
1. Select a stock for sentiment analysis
2. Choose analysis date range
3. Select display format (Tabulation or Plot)
4. Click "Analyze Sentiment" to get sentiment scores and news

## 🔧 Technical Details

- **Frontend**: Streamlit
- **Data Processing**: Pandas, NumPy
- **Machine Learning**: Scikit-learn
- **Visualization**: Plotly, Matplotlib
- **Data Sources**: Yahoo Finance, News APIs
- **Sentiment Analysis**: TextBlob, NLTK

## 📈 Model Performance

The application uses trained machine learning models for each stock, providing:
- Price predictions with confidence intervals
- Historical accuracy metrics
- Real-time model updates

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



## ⚠️ Disclaimer

This application is for educational and research purposes only. Stock predictions are not financial advice. Always consult with financial professionals before making investment decisions.

## 📞 Contact

For questions or support, please open an issue on GitHub.

---

**Note**: This is a final year project demonstrating machine learning applications in financial analysis. 