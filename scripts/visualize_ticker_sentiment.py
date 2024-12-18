import os
import pandas as pd
import matplotlib.pyplot as plt

# Ensure the "visualization results" folder exists
os.makedirs("visualization results", exist_ok=True)

# Load the ticker sentiment data
ticker_sentiment = pd.read_csv("stock_ticker_sentiment.csv")

# Load the expanded dataset with tickers and sentiment scores
data = pd.read_csv("wallstreetbets_posts_with_tickers.csv")

# Top 10 tickers by sentiment score
top_tickers = ticker_sentiment.nlargest(10, "sentiment_score")

# Bottom 10 tickers by sentiment score
bottom_tickers = ticker_sentiment.nsmallest(10, "sentiment_score")

# 1. Plot Top 10 Tickers by Sentiment Score
plt.figure(figsize=(10, 6))
plt.bar(top_tickers["tickers"], top_tickers["sentiment_score"], color="green")
plt.title("Top 10 Tickers by Sentiment Score", fontsize=16)
plt.xlabel("Stock Ticker", fontsize=14)
plt.ylabel("Average Sentiment Score", fontsize=14)
plt.tight_layout()
plt.savefig("visualization results/top_tickers_sentiment.png")
plt.show()

# 2. Plot Bottom 10 Tickers by Sentiment Score
plt.figure(figsize=(10, 6))
plt.bar(bottom_tickers["tickers"], bottom_tickers["sentiment_score"], color="red")
plt.title("Bottom 10 Tickers by Sentiment Score", fontsize=16)
plt.xlabel("Stock Ticker", fontsize=14)
plt.ylabel("Average Sentiment Score", fontsize=14)
plt.tight_layout()
plt.savefig("visualization results/bottom_tickers_sentiment.png")
plt.show()

# 3. Sentiment Distribution by Ticker
top_tickers_list = top_tickers["tickers"].tolist()
data_top_tickers = data[data["tickers"].isin(top_tickers_list)]

plt.figure(figsize=(12, 8))
data_top_tickers.boxplot(column="sentiment_score", by="tickers", grid=False, vert=False, patch_artist=True, showmeans=True)
plt.title("Sentiment Distribution by Ticker", fontsize=16)
plt.suptitle("")  # Removes default subplot title
plt.xlabel("Sentiment Score", fontsize=14)
plt.ylabel("Stock Ticker", fontsize=14)
plt.tight_layout()
plt.savefig("visualization results/sentiment_distribution_by_ticker.png")
plt.show()

# 4. Most Frequently Mentioned Tickers
ticker_counts = data["tickers"].value_counts().nlargest(10)

plt.figure(figsize=(10, 6))
ticker_counts.plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Most Frequently Mentioned Tickers", fontsize=16)
plt.xlabel("Stock Ticker", fontsize=14)
plt.ylabel("Mention Count", fontsize=14)
plt.tight_layout()
plt.savefig("visualization results/most_frequently_mentioned_tickers.png")
plt.show()

# 5. Average Sentiment Over Time for Top Ticker
top_ticker = ticker_counts.idxmax()
data_top_ticker = data[data["tickers"] == top_ticker]
data_top_ticker["created"] = pd.to_datetime(data_top_ticker["created"], unit="s")
sentiment_over_time = data_top_ticker.groupby(data_top_ticker["created"].dt.date)["sentiment_score"].mean()

plt.figure(figsize=(12, 6))
sentiment_over_time.plot(kind="line", marker="o", color="green")
plt.title(f"Average Sentiment Over Time for {top_ticker}", fontsize=16)
plt.xlabel("Date", fontsize=14)
plt.ylabel("Average Sentiment Score", fontsize=14)
plt.grid(True)
plt.tight_layout()
plt.savefig(f"visualization results/average_sentiment_over_time_{top_ticker}.png")
plt.show()
