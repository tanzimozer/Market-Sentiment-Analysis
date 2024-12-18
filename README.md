# Market-Sentiment-Analysis
Stock Sentiment Analysis Using Reddit Data

# Summary
The Market-Sentiment-Analysis project leverages Natural Language Processing (NLP) to analyze how public sentiment influences financial markets. Using Reddit as the primary data source, it dynamically identifies trending stocks based on sentiment scores, correlates sentiment trends with market activity, and provides actionable insights for traders and investors. This project demonstrates cutting-edge data science techniques, including:
   | Data scraping using the Reddit API.
   | Sentiment scoring with VADER.
   | Visualization of sentiment trends.
   | Workflow automation for dynamic stock analysis.


# Folder Structure
Market-Sentiment-Analysis/
├── README.md                     # Main project overview
├── scripts/                      # Python scripts for automation
│   ├── reddit_api_config.py      # API configuration for Reddit
│   ├── reddit_data_collection.py # Script for data collection
│   ├── reddit_sentiment_analysis.py # Sentiment analysis and visualization
├── visualization results/        # Saved visualizations (e.g., PNG images)
│   ├── sentiment_distribution.png
│   ├── top_posts_sentiment.png
│   ├── sentiment_vs_comments.png
│   ├── ...                       # Additional plots
└── venv/                         # Virtual environment (excluded via .gitignore)


# Project Goals
    Dynamically collect and analyze sentiment data from Reddit.
    Correlate sentiment trends with potential market activity.
    Visualize actionable insights for financial decision-making.
    Provide a reproducible workflow for sentiment-based analysis.


# Steps Taken
  1. Reddit Data Collection
     Tool: Python praw (Reddit API wrapper).
     Collected posts from r/wallstreetbets, focusing on titles and text bodies.
     Stored the data in wallstreetbets_posts.csv.
  2. Sentiment Analysis
     Tool: VADER Sentiment Analyzer.
     Assigned sentiment scores (positive, neutral, negative) to each post.
     Saved results to wallstreetbets_posts_with_sentiment.csv.
  3. Visualization
     Generated insights with matplotlib:
     Distribution of sentiment scores.
     Top/bottom posts by sentiment.
     Relationships between sentiment, post length, and comment counts.
     Sentiment trends over time.


# Dynamic Stock Selection Process
     Source: Data from Reddit’s r/wallstreetbets community.


# Criteria:
     Stocks frequently mentioned in trending discussions.
     High sentiment volatility or volume.
     Posts with significant engagement (e.g., comments, upvotes).


# Tools and Libraries
     Data Collection: praw, requests.
     NLP Processing: vaderSentiment.
     Visualization: matplotlib.


# How to Run the Project
     1. Clone the Repository
        git clone https://github.com/tanzimozer/Market-Sentiment-Analysis.git
        cd Market-Sentiment-Analysis
     2. Create a virtual environment: python -m venv venv
     3. Activate the virtual environment: venv\Scripts\activate  # On Windows
                                          venv/bin/activate  # On macOS/Linux
     4. Install dependencies:
        pip install praw vaderSentiment matplotlib pandas
     5. Run the Scripts
        Collect Data: python scripts/reddit_data_collection.py
        Analyze Sentiment: python scripts/reddit_sentiment_analysis.py


# View Results
     Visualizations will be saved in the visualization results/ folder.
     Processed sentiment data will be in wallstreetbets_posts_with_sentiment.csv.


# Key Insights
     Sentiment trends are a strong indicator of stock popularity.
     Posts with high sentiment shifts often correspond to spikes in stock discussion.
     Visualizations provide actionable insights for further financial analysis.


# Learning Outcomes
     Mastered Reddit API for real-time data collection.
     Applied VADER for robust sentiment scoring.
     Developed reusable workflows for sentiment-based analysis.
     Created professional visualizations to interpret market sentiment.


# Conclusion
     This project demonstrates how sentiment analysis of public forums like Reddit can 
     provide valuable insights into market trends. By dynamically analyzing trending 
     stocks, this framework can support traders, investors, and analysts in making data- 
     driven decisions.
