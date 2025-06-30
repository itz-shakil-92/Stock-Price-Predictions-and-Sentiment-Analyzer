# 🚀 Deployment Guide

This guide will help you set up and run the Stock Price Prediction & Sentiment Analysis application.

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git

## 🛠️ Installation Steps

### 1. Clone the Repository
```bash
git clone https://github.com/itz-shakil-92/Stock-Price-Predictions-and-Sentiment-Analyzer.git
cd Stock-Price-Predictions-and-Sentiment-Analyzer
```

### 2. Create Virtual Environment (Recommended)
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file in the project root:
```bash
# News API Key (Get from https://newsapi.org/)
NEWS_API_KEY=your_news_api_key_here
```

### 5. Run the Application
```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

## 🔧 Configuration

### News API Setup
1. Go to [NewsAPI.org](https://newsapi.org/)
2. Sign up for a free account
3. Get your API key
4. Add it to the `.env` file

### Model and Data Files
The application expects:
- Model files in the `models/` directory (`.pkl` files)
- Data files in the `data/` directory (`.csv` files)

If these files are not included in the repository due to size limitations, you'll need to:
1. Train the models using the notebooks in `models_notebook/`
2. Download stock data and place it in the `data/` directory

## 🐳 Docker Deployment (Optional)

If you prefer using Docker:

```bash
# Build the Docker image
docker build -t stock-prediction .

# Run the container
docker run -p 8501:8501 stock-prediction
```

## ☁️ Cloud Deployment

### Heroku
1. Create a `Procfile`:
```
web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
```

2. Deploy using Heroku CLI:
```bash
heroku create your-app-name
git push heroku main
```

### Streamlit Cloud
1. Connect your GitHub repository to [Streamlit Cloud](https://streamlit.io/cloud)
2. Deploy automatically

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

4. **Port Already in Use**: Use a different port
   ```bash
   streamlit run app.py --server.port 8502
   ```

### Getting Help
- Check the logs for error messages
- Ensure all dependencies are compatible
- Verify file paths and permissions

## 📊 Performance Tips

- Use recent date ranges for better performance
- Limit the number of articles analyzed
- Consider using a paid News API plan for more requests

## 🔒 Security Notes

- Never commit API keys to version control
- Use environment variables for sensitive data
- Regularly update dependencies for security patches 