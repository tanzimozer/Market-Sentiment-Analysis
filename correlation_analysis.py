import pandas as pd
import os

# Load sentiment data
sentiment_data = pd.read_csv("wallstreetbets_posts_with_tickers.csv")

# Prepare a DataFrame to store correlation results
correlation_results = []

# Loop through each ticker
for ticker in sentiment_data["tickers"].unique():
    price_file = f"stock_data/{ticker}_prices.csv"

    # Check if price data exists for this ticker
    if os.path.exists(price_file):
        # Load stock price data
        stock_data = pd.read_csv(price_file)
        stock_data["Date"] = pd.to_datetime(stock_data["Date"])

        # Aggregate sentiment scores by date
        sentiment_daily = sentiment_data[sentiment_data["tickers"] == ticker]
        sentiment_daily = sentiment_daily.groupby("created")["sentiment_score"].mean().reset_index()
        sentiment_daily["created"] = pd.to_datetime(sentiment_daily["created"])

        # Merge stock prices and sentiment data
        merged_data = pd.merge(
            stock_data, sentiment_daily, left_on="Date", right_on="created", how="inner"
        )

        # Calculate correlation between sentiment and closing prices
        correlation = merged_data["sentiment_score"].corr(merged_data["Close"])
        correlation_results.append({"ticker": ticker, "correlation": correlation})
        print(f"Correlation for {ticker}: {correlation}")
    else:
        print(f"No price data available for {ticker}")

# Save correlation results
correlation_df = pd.DataFrame(correlation_results)
correlation_df.to_csv("correlation_results.csv", index=False)
print("Correlation analysis completed. Results saved to correlation_results.csv")
