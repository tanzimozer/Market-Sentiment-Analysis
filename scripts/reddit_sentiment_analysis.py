# reddit_sentiment_analysis.py

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Load the data
data = pd.read_csv("wallstreetbets_posts.csv")

# Initialize VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Add sentiment scores to the DataFrame
def analyze_sentiment(text):
    scores = analyzer.polarity_scores(str(text))
    return scores["compound"]

# Apply sentiment analysis to the "title" column
data["sentiment_score"] = data["title"].apply(analyze_sentiment)

# Save the updated DataFrame
data.to_csv("wallstreetbets_posts_with_sentiment.csv", index=False)
print("Sentiment analysis complete. Saved to wallstreetbets_posts_with_sentiment.csv")
