#!/usr/bin/python3
"""Print the titles of the first 10 hot posts of a subreddit."""
import json
import urllib.request


class NoRedirect(urllib.request.HTTPRedirectHandler):
    """Refuse to follow redirects."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        """Return None so a redirect raises an HTTPError."""
        return None


def top_ten(subreddit):
    """Print the first 10 hot post titles, or None if invalid."""
    if not subreddit or not isinstance(subreddit, str):
        print(None)
        return
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    request = urllib.request.Request(
        url, headers={"User-Agent": "linux:alu.scripting.api:v1.0"})
    opener = urllib.request.build_opener(NoRedirect)
    try:
        with opener.open(request, timeout=10) as response:
            data = json.loads(response.read().decode("utf-8"))
        posts = data["data"]["children"]
    except Exception:
        print(None)
        return
    for post in posts[:10]:
        print(post["data"]["title"])
