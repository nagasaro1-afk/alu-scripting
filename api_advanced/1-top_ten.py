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
    headers = {"User-Agent": "linux:alu.scripting.api:v1.0 (by /u/nagasaro1)"}
    for url in urls:
        try:
            response = requests.get(url.format(subreddit), headers=headers,
                                    allow_redirects=False)
            code = getattr(response, "status_code", 200)
            if isinstance(code, int) and code != 200:
                continue
            posts = response.json()["data"]["children"]
            titles = [post["data"]["title"] for post in posts[:10]]
        except Exception:
            continue
        if titles:
            for title in titles:
                print(title)
            return
    print(None)
