#!/usr/bin/python3
"""Module that queries the Reddit API for top 10 hot posts."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "python3:api_advanced:v1.0 (by /u/stephane_alu)"
    }
    params = {"limit": 10}
    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False,
        timeout=10
    )
    if response.status_code != 200:
        print(None)
        return
    data = response.json()
    posts = data.get("data", {}).get("children", [])
    if not post:
        print(None)
        return
    for post in posts:
        print(post.get("data", {}).get("title"))
        