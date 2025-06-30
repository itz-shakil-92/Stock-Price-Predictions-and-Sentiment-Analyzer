import plotly.graph_objects as go
import matplotlib.pyplot as plt
import pandas as pd

def plot_candlestick(df):
    """
    Create a line plot comparing predicted vs actual close prices.
    
    Args:
        df (DataFrame): DataFrame with Date, Close_Actual, Close_Predicted columns
    
    Returns:
        plotly.graph_objects.Figure: The line chart
    """
    if df.empty:
        # Return empty plot if no data
        fig = go.Figure()
        fig.add_annotation(text="No data available", xref="paper", yref="paper", x=0.5, y=0.5, showarrow=False)
        fig.update_layout(title='Price Prediction vs Actual')
        return fig
    
    # Check if required columns exist
    required_cols = ['Date', 'Close_Actual', 'Close_Predicted']
    missing_cols = [col for col in required_cols if col not in df.columns]
    
    if missing_cols:
        # Return error plot if columns are missing
        fig = go.Figure()
        fig.add_annotation(text=f"Missing columns: {', '.join(missing_cols)}", 
                          xref="paper", yref="paper", x=0.5, y=0.5, showarrow=False)
        fig.update_layout(title='Price Prediction vs Actual')
        return fig
    
    fig = go.Figure()
    
    # Add actual price line
    fig.add_trace(go.Scatter(
        x=df['Date'],
        y=df['Close_Actual'],
        mode='lines+markers',
        name='Actual Price',
        line=dict(color='blue', width=2),
        marker=dict(size=6)
    ))
    
    # Add predicted price line
    fig.add_trace(go.Scatter(
        x=df['Date'],
        y=df['Close_Predicted'],
        mode='lines+markers',
        name='Predicted Price',
        line=dict(color='red', width=2, dash='dash'),
        marker=dict(size=6, symbol='diamond')
    ))
    
    fig.update_layout(
        title='Stock Price Prediction vs Actual',
        xaxis_title='Date',
        yaxis_title='Price (₹)',
        template='plotly_white',
        hovermode='x unified',
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )
    
    return fig

def plot_sentiment(df):
    """
    Create a sentiment timeline plot using Plotly.
    
    Args:
        df (DataFrame): DataFrame with Date, Sentiment, and Score columns
    
    Returns:
        plotly.graph_objects.Figure: The sentiment timeline plot
    """
    if df.empty:
        # Return empty plot if no data
        fig = go.Figure()
        fig.add_annotation(text="No data available", xref="paper", yref="paper", x=0.5, y=0.5, showarrow=False)
        fig.update_layout(title="Sentiment Timeline")
        return fig
    
    # Check if required columns exist
    if 'Date' not in df.columns or 'Sentiment' not in df.columns:
        fig = go.Figure()
        fig.add_annotation(text="Missing Date or Sentiment columns", xref="paper", yref="paper", x=0.5, y=0.5, showarrow=False)
        fig.update_layout(title="Sentiment Timeline")
        return fig
    
    # Group by date and sentiment
    sentiment_counts = df.groupby(['Date', 'Sentiment']).size().reset_index(name='Count')
    
    # Create color mapping
    color_map = {'POSITIVE': 'green', 'NEGATIVE': 'red', 'NEUTRAL': 'orange'}
    
    fig = go.Figure()
    
    # Plot each sentiment type
    for sentiment in ['POSITIVE', 'NEGATIVE', 'NEUTRAL']:
        sentiment_data = sentiment_counts[sentiment_counts['Sentiment'] == sentiment]
        if not sentiment_data.empty:
            fig.add_trace(go.Scatter(
                x=sentiment_data['Date'],
                y=sentiment_data['Count'],
                mode='markers',
                name=f'{sentiment} ({sentiment_data["Count"].sum()} total)',
                marker=dict(
                    color=color_map[sentiment],
                    size=12,
                    line=dict(color='black', width=1)
                ),
                hovertemplate=f'<b>{sentiment}</b><br>Date: %{{x}}<br>Articles: %{{y}}<extra></extra>'
            ))
    
    # Customize the plot
    fig.update_layout(
        title='Sentiment Analysis Timeline',
        xaxis_title='Date',
        yaxis_title='Number of Articles/Signals',
        template='plotly_white',
        hovermode='x unified',
        legend=dict(
            title='Sentiment Types',
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        annotations=[
            dict(
                text=f"Total Articles: {len(df)}",
                showarrow=False,
                xref="paper",
                yref="paper",
                x=0.02,
                y=0.98,
                bgcolor="wheat",
                bordercolor="black",
                borderwidth=1
            )
        ]
    )
    
    return fig