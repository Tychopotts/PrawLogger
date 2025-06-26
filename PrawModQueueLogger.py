import yaml
import praw
import json

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

reddit = praw.Reddit(
    client_id=config["client_id"],
    client_secret=config["client_secret"],
    user_agent=config["user_agent"],
    username=config["user_name"],
    password=config["user_pass"]
)

print("Logged in as:", reddit.user.me())

subreddit = reddit.subreddit(config["subreddit"])  # Use subreddit from config

modqueue_items = []
for item in subreddit.mod.modqueue(limit=10):  # Adjust limit as needed
    modqueue_items.append({
        "id": item.id,
        "type": item.__class__.__name__,
        "author": str(item.author),
        "title": getattr(item, "title", None),
        "body": getattr(item, "selftext", None),
        "permalink": item.permalink,
        "created_utc": item.created_utc
    })

print(json.dumps(modqueue_items, indent=2))