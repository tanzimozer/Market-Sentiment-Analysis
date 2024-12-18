# reddit_test_connection.py

import praw
from reddit_api_config import CLIENT_ID, CLIENT_SECRET, USER_AGENT

# Authenticate with Reddit API
reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    user_agent=USER_AGENT
)

# Test connection by fetching subreddit information
try:
    subreddit = reddit.subreddit("wallstreetbets")
    print(f"Connected to subreddit: {subreddit.display_name}")
except Exception as e:
    print(f"Error: {e}")
