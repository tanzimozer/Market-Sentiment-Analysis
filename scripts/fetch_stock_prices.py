import yfinance as yf
import pandas as pd
import os

# Ensure the "stock_data" folder exists
os.makedirs("stock_data", exist_ok=True)

# Load the tickers from the sentiment analysis file
tickers = pd.read_csv("stock_ticker_sentiment.csv")["tickers"].tolist()

# Define the date range for historical data
start_date = "2023-01-01"  # Adjust as needed
end_date = "2023-12-31"    # Adjust as needed

# Fetch stock prices for each ticker
for ticker in tickers:
    try:
        stock_data = yf.download(ticker, start=start_date, end=end_date)
        stock_data.to_csv(f"stock_data/{ticker}_prices.csv")
        print(f"Downloaded data for {ticker}")
    except Exception as e:
        print(f"Failed to fetch data for {ticker}: {e}")
