# reddit_sentiment_visualization.py

import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv("wallstreetbets_posts_with_sentiment.csv")

# Plot sentiment distribution
plt.figure(figsize=(10, 6))
plt.hist(data["sentiment_score"], bins=20, edgecolor="black", alpha=0.7)
plt.title("Distribution of Sentiment Scores", fontsize=16)
plt.xlabel("Sentiment Score", fontsize=14)
plt.ylabel("Frequency", fontsize=14)
plt.grid(True)
plt.savefig("sentiment_distribution.png")
plt.show()

# Plot average sentiment score over time (if a 'created' column exists)
if "created" in data.columns:
    data["created"] = pd.to_datetime(data["created"], unit="s")
    data.set_index("created", inplace=True)
    sentiment_over_time = data["sentiment_score"].resample("D").mean()

    plt.figure(figsize=(10, 6))
    sentiment_over_time.plot()
    plt.title("Average Sentiment Score Over Time", fontsize=16)
    plt.xlabel("Date", fontsize=14)
    plt.ylabel("Average Sentiment Score", fontsize=14)
    plt.grid(True)
    plt.savefig("sentiment_over_time.png")
    plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv("wallstreetbets_posts_with_sentiment.csv")

# Top Posts by Sentiment Score
top_posts = data.nlargest(10, "sentiment_score")
plt.figure(figsize=(10, 6))
plt.barh(top_posts["title"], top_posts["sentiment_score"], color="green")
plt.title("Top 10 Posts by Sentiment Score", fontsize=16)
plt.xlabel("Sentiment Score", fontsize=14)
plt.ylabel("Post Title", fontsize=14)
plt.tight_layout()
plt.savefig("top_posts_sentiment.png")
plt.show()

# Bottom Posts by Sentiment Score
bottom_posts = data.nsmallest(10, "sentiment_score")
plt.figure(figsize=(10, 6))
plt.barh(bottom_posts["title"], bottom_posts["sentiment_score"], color="red")
plt.title("Bottom 10 Posts by Sentiment Score", fontsize=16)
plt.xlabel("Sentiment Score", fontsize=14)
plt.ylabel("Post Title", fontsize=14)
plt.tight_layout()
plt.savefig("bottom_posts_sentiment.png")
plt.show()

# Sentiment vs. Post Score
plt.figure(figsize=(10, 6))
plt.scatter(data["sentiment_score"], data["score"], alpha=0.7, edgecolor="k")
plt.title("Sentiment Score vs. Post Score", fontsize=16)
plt.xlabel("Sentiment Score", fontsize=14)
plt.ylabel("Post Score", fontsize=14)
plt.grid(True)
plt.savefig("sentiment_vs_score.png")
plt.show()

# Sentiment by Number of Comments
plt.figure(figsize=(10, 6))
plt.scatter(data["sentiment_score"], data["num_comments"], alpha=0.7, edgecolor="k", color="purple")
plt.title("Sentiment Score vs. Number of Comments", fontsize=16)
plt.xlabel("Sentiment Score", fontsize=14)
plt.ylabel("Number of Comments", fontsize=14)
plt.grid(True)
plt.savefig("sentiment_vs_comments.png")
plt.show()

# Boxplot of Sentiment Scores
plt.figure(figsize=(8, 6))
plt.boxplot(data["sentiment_score"], vert=False, patch_artist=True, boxprops=dict(facecolor="orange"))
plt.title("Boxplot of Sentiment Scores", fontsize=16)
plt.xlabel("Sentiment Score", fontsize=14)
plt.savefig("boxplot_sentiment.png")
plt.show()

# Post Length vs. Sentiment
data["post_length"] = data["body"].apply(lambda x: len(str(x)))
plt.figure(figsize=(10, 6))
plt.scatter(data["post_length"], data["sentiment_score"], alpha=0.7, edgecolor="k", color="blue")
plt.title("Post Length vs. Sentiment Score", fontsize=16)
plt.xlabel("Post Length (characters)", fontsize=14)
plt.ylabel("Sentiment Score", fontsize=14)
plt.grid(True)
plt.savefig("post_length_vs_sentiment.png")
plt.show()

# Average Sentiment by Post Score Buckets
data["score_bucket"] = pd.cut(data["score"], bins=5)
average_sentiment_by_bucket = data.groupby("score_bucket")["sentiment_score"].mean()
average_sentiment_by_bucket.plot(kind="bar", figsize=(10, 6), color="cyan", edgecolor="black")
plt.title("Average Sentiment by Post Score Buckets", fontsize=16)
plt.xlabel("Post Score Buckets", fontsize=14)
plt.ylabel("Average Sentiment Score", fontsize=14)
plt.tight_layout()
plt.savefig("sentiment_by_score_buckets.png")
plt.show()

# Average Sentiment by Number of Comments Buckets
data["comments_bucket"] = pd.cut(data["num_comments"], bins=5)
average_sentiment_by_comments = data.groupby("comments_bucket")["sentiment_score"].mean()
average_sentiment_by_comments.plot(kind="bar", figsize=(10, 6), color="magenta", edgecolor="black")
plt.title("Average Sentiment by Number of Comments Buckets", fontsize=16)
plt.xlabel("Number of Comments Buckets", fontsize=14)
plt.ylabel("Average Sentiment Score", fontsize=14)
plt.tight_layout()
plt.savefig("sentiment_by_comments_buckets.png")
plt.show()
