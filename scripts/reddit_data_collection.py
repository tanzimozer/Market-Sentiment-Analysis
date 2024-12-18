# reddit_data_collection.py

import praw
from reddit_api_config import CLIENT_ID, CLIENT_SECRET, USER_AGENT
import pandas as pd

# Authenticate with Reddit API
reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    user_agent=USER_AGENT
)

# Define the subreddit and fetch top posts
def fetch_posts(subreddit_name, limit=1000):
    subreddit = reddit.subreddit(subreddit_name)
    posts = []

    for post in subreddit.hot(limit=limit):
        posts.append({
            "title": post.title,
            "score": post.score,
            "id": post.id,
            "url": post.url,
            "created": post.created_utc,
            "num_comments": post.num_comments,
            "body": post.selftext
        })

    return pd.DataFrame(posts)

# Fetch data and save to CSV
if __name__ == "__main__":
    subreddit_name = "wallstreetbets"  # Change this to any subreddit
    data = fetch_posts(subreddit_name)
    data.to_csv(f"{subreddit_name}_posts.csv", index=False)
    print(f"Fetched {len(data)} posts from r/{subreddit_name}")
