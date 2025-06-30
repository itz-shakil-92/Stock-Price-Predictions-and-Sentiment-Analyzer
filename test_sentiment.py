#!/usr/bin/env python3
"""
Test script for sentiment analysis functionality
"""

import sys
import os
from datetime import date, timedelta

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.sentiment_utils import analyze_sentiment, plot_sentiment
import matplotlib.pyplot as plt

def test_sentiment_analysis():
    """Test the sentiment analysis functionality"""
    
    print("🧪 Testing Sentiment Analysis...")
    print("=" * 50)
    
    # Test parameters
    test_stock = "RELIANCE"
    end_date = date.today()
    start_date = end_date - timedelta(days=7)  # Last 7 days
    
    print(f"📊 Stock: {test_stock}")
    print(f"📅 Date Range: {start_date} to {end_date}")
    print()
    
    try:
        # Test sentiment analysis
        print("🔄 Running sentiment analysis...")
        sentiment_df, summary, top_news_df = analyze_sentiment(test_stock, start_date, end_date)
        
        # Check results
        if sentiment_df.empty:
            print("❌ No sentiment data returned")
            return False
        
        print("✅ Sentiment analysis completed successfully!")
        print()
        
        # Display results
        print(f"📈 Overall Sentiment: {summary}")
        print(f"📰 Total Articles Analyzed: {len(sentiment_df)}")
        print()
        
        # Show sentiment distribution
        sentiment_counts = sentiment_df['Sentiment'].value_counts()
        print("📊 Sentiment Distribution:")
        for sentiment, count in sentiment_counts.items():
            print(f"   {sentiment}: {count} articles")
        print()
        
        # Show top news
        if not top_news_df.empty:
            print("🔥 Top 5 Influential News:")
            for i, (_, row) in enumerate(top_news_df.iterrows(), 1):
                print(f"   {i}. {row['Headline'][:80]}...")
                print(f"      Sentiment: {row['Sentiment']} (Score: {row['Score']:.3f})")
                print()
        
        # Test plotting
        print("📊 Testing sentiment plot...")
        try:
            fig = plot_sentiment(sentiment_df)
            print("✅ Sentiment plot created successfully!")
            
            # Save the plot
            plot_filename = "sentiment_test_plot.png"
            fig.savefig(plot_filename, dpi=300, bbox_inches='tight')
            print(f"💾 Plot saved as: {plot_filename}")
            plt.close(fig)
            
        except Exception as plot_error:
            print(f"❌ Error creating plot: {plot_error}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error during sentiment analysis: {e}")
        return False

def test_api_connection():
    """Test the News API connection"""
    
    print("🌐 Testing News API Connection...")
    print("=" * 50)
    
    import requests
    from utils.sentiment_utils import NEWS_API_KEY, NEWS_ENDPOINT
    
    # Test API key
    if NEWS_API_KEY == "your_api_key_here":
        print("❌ API key not set properly")
        return False
    
    # Test API endpoint
    test_params = {
        "q": "RELIANCE stock",
        "from": (date.today() - timedelta(days=1)).strftime("%Y-%m-%d"),
        "to": date.today().strftime("%Y-%m-%d"),
        "sortBy": "relevancy",
        "apiKey": NEWS_API_KEY,
        "language": "en",
        "pageSize": 5
    }
    
    try:
        response = requests.get(NEWS_ENDPOINT, params=test_params, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            articles = data.get("articles", [])
            print(f"✅ API connection successful!")
            print(f"📰 Found {len(articles)} articles in test query")
            return True
        else:
            print(f"❌ API Error: {response.status_code}")
            print(f"   Message: {response.json().get('message', 'Unknown error')}")
            return False
            
    except Exception as e:
        print(f"❌ Connection error: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Starting Sentiment Analysis Tests")
    print("=" * 60)
    print()
    
    # Test 1: API Connection
    api_success = test_api_connection()
    print()
    
    if api_success:
        # Test 2: Full Sentiment Analysis
        sentiment_success = test_sentiment_analysis()
        print()
        
        # Summary
        print("📋 Test Summary:")
        print("=" * 30)
        print(f"🌐 API Connection: {'✅ PASS' if api_success else '❌ FAIL'}")
        print(f"🧠 Sentiment Analysis: {'✅ PASS' if sentiment_success else '❌ FAIL'}")
        
        if api_success and sentiment_success:
            print("\n🎉 All tests passed! Sentiment analysis is working correctly.")
        else:
            print("\n⚠️ Some tests failed. Please check the error messages above.")
    else:
        print("❌ API connection failed. Cannot proceed with sentiment analysis test.")
        print("   Please check your API key and internet connection.") 