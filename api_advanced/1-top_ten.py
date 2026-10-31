#!/usr/bin/python3
"""Print the titles of the first 10 hot posts of a subreddit."""
import requests


def top_ten(subreddit):
    """Print the first 10 hot post titles, or None if invalid."""
    urls = [
        "https://www.reddit.com/r/{}/hot.json?limit=10",
        "https://old.reddit.com/r/{}/hot.json?limit=10",
        "https://api.reddit.com/r/{}/hot?limit=10",
    ]
    agents = [
        "linux:alu.scripting.api:v1.0 (by /u/nagasaro1)",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/120.0 Safari/537.36",
    ]
    for url in urls:
        for agent in agents:
            try:
                response = requests.get(
                    url.format(subreddit), headers={"User-Agent": agent},
                    allow_redirects=False, timeout=10)
                posts = response.json()["data"]["children"]
                titles = [post["data"]["title"] for post in posts[:10]]
            except Exception:
                continue
            for title in titles:
                print(title)
            return
    print(None)
