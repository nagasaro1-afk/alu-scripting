#!/usr/bin/python3
"""Prints the titles of the first 10 hot posts of a subreddit"""
import requests


def top_ten(subreddit):
    """Prints 10 hot post titles, or None if the subreddit is invalid"""
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/120.0 Safari/537.36"
    }
    hosts = ["www.reddit.com", "old.reddit.com"]
    for host in hosts:
        url = "https://{}/r/{}/hot.json?limit=10".format(host, subreddit)
        try:
            res = requests.get(url, headers=headers,
                               allow_redirects=False, timeout=10)
        except requests.RequestException:
            continue
        if res.status_code == 200:
            try:
                posts = res.json().get("data", {}).get("children", [])
            except ValueError:
                print(None)
                return
            if not posts:
                print(None)
                return
            for post in posts:
                print(post.get("data", {}).get("title"))
            return
        if res.status_code != 403:
            print(None)
            return
    print(None)
