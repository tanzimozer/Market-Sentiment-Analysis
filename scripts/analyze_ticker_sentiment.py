import pandas as pd

# Load the expanded data with tickers
data = pd.read_csv("wallstreetbets_posts_with_tickers.csv")

# Group by ticker and calculate average sentiment
ticker_sentiment = data.groupby("tickers")["sentiment_score"].mean().reset_index()

# Sort tickers by sentiment scores
ticker_sentiment = ticker_sentiment.sort_values(by="sentiment_score", ascending=False)

# Save the results to a new CSV file
ticker_sentiment.to_csv("stock_ticker_sentiment.csv", index=False)
print("Ticker-specific sentiment analysis saved to stock_ticker_sentiment.csv")
