#!/usr/bin/python3
"""Print the titles of the first 10 hot posts of a subreddit."""
import requests


def top_ten(subreddit):
    """Print the first 10 hot post titles, or None if invalid."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "linux:alu.scripting.api:v1.0 (by /u/nagasaro1)"}
    try:
        response = requests.get(url, headers=headers,
                                allow_redirects=False)
        posts = response.json()["data"]["children"]
        titles = [post["data"]["title"] for post in posts[:10]]
    except Exception:
        print(None)
        return
    for title in titles:
        print(title)
