#!/usr/bin/python3
"""Print the titles of the first 10 hot posts of a subreddit."""
import requests


def top_ten(subreddit):
    """DEBUG: show what the request does."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "linux:alu.scripting.api:v1.0 (by /u/nagasaro1)"}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        print("DEBUG status:", getattr(response, "status_code", "n/a"))
        print("DEBUG type:", type(response).__name__)
        print("DEBUG text:", str(getattr(response, "text", ""))[:150])
    except Exception as err:
        print("DEBUG error:", type(err).__name__, str(err)[:150])
