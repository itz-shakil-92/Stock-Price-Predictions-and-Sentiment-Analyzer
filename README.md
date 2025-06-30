# 📈 Stock Price Prediction & Sentiment Analysis

A comprehensive machine learning application that predicts stock prices and analyzes market sentiment using news data for Indian stocks.

## 🚀 Features

- **Stock Price Prediction**: ML-based forecasting for 20 major Indian stocks
- **Sentiment Analysis**: News sentiment analysis with interactive timeline visualization
- **Interactive Dashboard**: Streamlit-based web interface with modern UI
- **Visual Analytics**: Line plots for price predictions and timeline plots for sentiment
- **Real-time Data**: Live stock data and news scraping
- **Date Range Validation**: Smart date picker with validation
- **Error Handling**: Robust error handling and user feedback

## 📊 Supported Stocks

The application supports 20 major Indian stocks:
- RELIANCE, TCS, INFY, HDFCBANK, ICICIBANK
- HCLTECH, LT, SBIN, WIPRO, ITC
- BAJFINANCE, HINDUNILVR, KOTAKBANK, ASIANPAINT
- NTPC, TATAMOTORS, ONGC, SUNPHARMA, TECHM, POWERGRID

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/itz-shakil-92/Stock-Price-Predictions-and-Sentiment-Analyzer.git
   cd Stock-Price-Predictions-and-Sentiment-Analyzer
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables** (Optional)
   ```bash
   # For Windows
   set NEWS_API_KEY=your_news_api_key_here
   
   # For macOS/Linux
   export NEWS_API_KEY=your_news_api_key_here
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

## 📁 Project Structure

```
Final_year_project/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── setup.py              # Package setup configuration
├── DEPLOYMENT.md         # Detailed deployment guide
├── test_sentiment.py     # Sentiment analysis test script
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
2. Choose prediction start and end dates (max 30 days)
3. Select display format (Tabulation or Line Plot)
4. Click "Predict Price" to get forecasts
5. View the comparison between predicted and actual prices

### Sentiment Analysis
1. Select a stock for sentiment analysis
2. Choose analysis date range (max 30 days)
3. Select display format (Tabulation or Plot)
4. Click "Analyze Sentiment" to get sentiment scores and news
5. View the interactive timeline showing sentiment distribution over time

## 🔧 Technical Details

- **Frontend**: Streamlit
- **Data Processing**: Pandas, NumPy
- **Machine Learning**: Scikit-learn, XGBoost
- **Visualization**: Plotly, Matplotlib
- **Data Sources**: Yahoo Finance, News APIs
- **Sentiment Analysis**: TextBlob, NLTK
- **Technical Indicators**: TA-Lib

## 📈 Model Performance

The application uses trained machine learning models for each stock, providing:
- Price predictions with confidence intervals
- Historical accuracy metrics
- Real-time model updates
- Technical indicator calculations (RSI, MACD, SMA)

## 🧪 Testing

Run the sentiment analysis test:
```bash
python test_sentiment.py
```

## 🚀 Deployment

### Local Development
```bash
streamlit run app.py
```

### Cloud Deployment
See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions on:
- Heroku deployment
- Streamlit Cloud deployment
- Docker deployment
- Environment setup

## 🔍 Troubleshooting

### Common Issues

1. **Import Errors**: Make sure all dependencies are installed
   ```bash
   pip install -r requirements.txt
   ```

2. **API Key Errors**: Ensure your News API key is set correctly
   ```bash
   export NEWS_API_KEY=your_key_here
   ```

3. **Model/Data File Errors**: Check if model and data files exist
   ```bash
   ls models/
   ls data/
   ```

4. **Date Selection Errors**: Use recent date ranges (within 30 days)

### Getting Help
- Check the logs for error messages
- Ensure all dependencies are compatible
- Verify file paths and permissions

## 📊 Performance Tips

- Use recent date ranges for better performance
- Limit the number of articles analyzed
- Consider using a paid News API plan for more requests
- Clear Streamlit cache if you encounter UI issues

## 🔒 Security Notes

- Never commit API keys to version control
- Use environment variables for sensitive data
- Regularly update dependencies for security patches

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This application is for educational and research purposes only. Stock predictions are not financial advice. Always consult with financial professionals before making investment decisions.

## 📞 Contact

For questions or support, please open an issue on GitHub.

---

**Note**: This is a final year project demonstrating machine learning applications in financial analysis. 