import pandas as pd
import re

# Load the data
data = pd.read_csv("wallstreetbets_posts_with_sentiment.csv")

# Define a list of stock ticker patterns
# This example covers common tickers in uppercase (e.g., $AAPL, TSLA)
ticker_pattern = re.compile(r'\b[A-Z]{1,5}\b|\$[A-Z]{1,5}')

# Extract tickers from post titles and bodies
def extract_tickers(text):
    matches = ticker_pattern.findall(str(text))
    return list(set(matches))  # Remove duplicates

# Apply extraction to both title and body columns
data["tickers"] = data["title"].apply(extract_tickers)

# Expand the list of tickers into separate rows
data_expanded = data.explode("tickers")

# Save the extracted tickers to a new file
data_expanded.to_csv("wallstreetbets_posts_with_tickers.csv", index=False)
print("Extracted stock tickers and saved to wallstreetbets_posts_with_tickers.csv")
