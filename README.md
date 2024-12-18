# Market_Sentiment_Analysis
Stock Sentiment Analysis Using Reddit Data

# Summary
The Market-Sentiment-Analysis project leverages Natural Language Processing (NLP) to analyze how public sentiment influences financial markets. Using Reddit as the primary data source, it dynamically identifies trending stocks based on sentiment scores, correlates sentiment trends with market activity, and provides actionable insights for traders and investors. This project demonstrates cutting-edge data science techniques, including:

# Data scraping using the Reddit API.
Sentiment scoring with VADER.
Visualization of sentiment trends.
Correlation analysis between sentiment and stock prices.
Workflow automation for dynamic stock analysis.


#Folder Structure

Market-Sentiment-Analysis/
├── .gitignore                     # Ignore unnecessary files
├── LICENSE                        # Licensing details
├── README.md                      # Main project overview
├── scripts/                       # Python scripts for automation
│   ├── Readme.md                  # Detailed instructions for scripts
│   ├── analyze_ticker_sentiment.py # Analyze sentiment by stock ticker
│   ├── extract_stock_tickers.py   # Extract stock tickers from Reddit posts
│   ├── fetch_stock_prices.py      # Fetch historical stock prices
│   ├── reddit_api_config.py       # API configuration for Reddit
│   ├── reddit_data_collection.py  # Collect Reddit posts
│   ├── reddit_sentiment_analysis.py # Sentiment analysis
│   ├── reddit_sentiment_visualization.py # Visualize sentiment trends
│   ├── reddit_test_connection.py  # Test Reddit API connection
│   ├── visualize_ticker_sentiment.py # Generate sentiment and correlation visualizations
├── stock_data/                    # Fetched stock price data (CSV files)
│   ├── $ASTS_prices.csv
│   ├── $GSAT_prices.csv
│   ├── ...
├── visualization results/         # Saved visualizations (e.g., PNG images)
│   ├── average_sentiment_over_time_I.png
│   ├── bottom_posts_sentiment.png
│   ├── bottom_tickers_sentiment.png
│   ├── boxplot_sentiment.png
│   ├── most_frequently_mentioned_tickers.png
│   ├── post_length_vs_sentiment.png
│   ├── sentiment_by_comments_buckets.png
│   ├── sentiment_by_score_buckets.png
│   ├── sentiment_distribution.png
│   ├── sentiment_distribution_by_ticker.png
│   ├── sentiment_over_time.png
│   ├── sentiment_vs_comments.png
│   ├── sentiment_vs_score.png
│   ├── top_posts_sentiment.png
│   ├── top_tickers_sentiment.png
└── correlation_analysis.py        # Main script for correlation analysis


# Project Goals
Dynamically collect and analyze sentiment data from Reddit.
Correlate sentiment trends with potential market activity.
Visualize actionable insights for financial decision-making.
Provide a reproducible workflow for sentiment-based analysis.


#Steps Taken
1. Reddit Data Collection
Tool: Python praw (Reddit API wrapper).
Collected posts from r/wallstreetbets, focusing on titles and text bodies.
Stored the data in wallstreetbets_posts.csv.
2. Sentiment Analysis
Tool: VADER Sentiment Analyzer.
Assigned sentiment scores (positive, neutral, negative) to each post.
Saved results to wallstreetbets_posts_with_sentiment.csv.
3. Stock Ticker Extraction
Extracted stock tickers mentioned in Reddit posts (e.g., $TSLA, $AAPL) using regular expressions.
Saved the expanded data with tickers to wallstreetbets_posts_with_tickers.csv.
4. Stock Price Fetching
Tool: yfinance library.
Collected historical stock prices (open, close, high, low) for extracted tickers.
Saved the data for each ticker in the stock_data/ folder.
5. Correlation Analysis
Merged sentiment scores with stock price data to calculate correlation coefficients.
Correlation results were saved in correlation_results.csv.
6. Visualization
Generated visualizations using matplotlib:
Top/Bottom Tickers by Sentiment: Bar charts of average sentiment scores.
Sentiment Distribution: Boxplot showing sentiment spread for top tickers.
Most Frequently Mentioned Tickers: Bar chart showing mention counts.
Correlation Analysis: Bar chart of correlations between sentiment and stock prices.


# Dynamic Stock Selection Process
Source: Data from Reddit’s r/wallstreetbets community.


# Criteria:
Stocks frequently mentioned in trending discussions.
High sentiment volatility or volume.
Posts with significant engagement (e.g., comments, upvotes).


# Tools and Libraries
Data Collection: praw, requests
NLP Processing: vaderSentiment
Stock Price Data: yfinance
Visualization: matplotlib
Data Manipulation: pandas


# How to Run the Project
1. Clone the Repository
git clone https://github.com/tanzimozer/Market-Sentiment-Analysis.git
cd Market-Sentiment-Analysis
2. Create and Activate Virtual Environment
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On macOS/Linux
3. Install Dependencies
pip install praw vaderSentiment matplotlib pandas yfinance
4. Run the Scripts
Collect Data:python scripts/reddit_data_collection.py
Analyze Sentiment: python scripts/reddit_sentiment_analysis.py
Extract Stock Tickers:
python scripts/extract_stock_tickers.py
Fetch Stock Prices: python scripts/fetch_stock_prices.py
Perform Correlation Analysis: python scripts/correlation_analysis.py
5. View Results
Visualizations are saved in the visualization results/ folder.
Correlation results are in correlation_results.csv.


# Key Insights
Sentiment Trends vs. Stock Prices:
Stocks like [insert examples with high correlations] showed strong positive correlations between sentiment and closing prices.
Some tickers displayed negative or negligible correlations, suggesting market dynamics not driven by sentiment.
Most Frequently Mentioned Stocks:
[Insert examples] were the most mentioned stocks in r/wallstreetbets.
Actionable Visualizations:
Top-performing tickers by sentiment and correlation provide insights for potential trades.


# Learning Outcomes
Mastered the Reddit API for dynamic data collection.
Applied VADER for robust sentiment scoring.
Developed a correlation framework to analyze sentiment trends and stock price movements.
Created reusable workflows for sentiment-based stock analysis.
Produced visualizations to interpret and communicate findings effectively.


# Conclusion
This project demonstrates the powerful role of sentiment analysis in financial markets. By dynamically analyzing Reddit sentiment and correlating it with stock price movements, it provides actionable insights for traders and investors. The methodology is flexible and can be extended to other platforms or used for predictive modeling.
