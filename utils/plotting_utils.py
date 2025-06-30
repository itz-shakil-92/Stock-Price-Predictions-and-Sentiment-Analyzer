import plotly.graph_objects as go
import matplotlib.pyplot as plt

def plot_candlestick(df):
    fig = go.Figure(data=[
        go.Candlestick(
            x=df['Date'],
            open=df['Open'],
            high=df['High'],
            low=df['Low'],
            close=df['Close_Actual'],
            name='Actual'
        ),
        go.Scatter(x=df['Date'], y=df['Close_Predicted'], mode='lines', name='Predicted')
    ])
    fig.update_layout(title='Candlestick Plot with Predictions', xaxis_title='Date', yaxis_title='Price')
    return fig

def plot_sentiment(df):
    color_map = df['Sentiment'].map({'POSITIVE': 'green', 'NEGATIVE': 'red'})
    fig, ax = plt.subplots()
    ax.barh(df['Headline'], df['Score'], color=color_map)
    ax.set_xlabel("Sentiment Score")
    ax.set_title("Top 5 News Sentiment")
    plt.tight_layout()
    return fig