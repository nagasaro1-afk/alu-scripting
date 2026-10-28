#!/usr/bin/python3
"""Query the Reddit API for the number of subscribers of a subreddit."""
import json
import urllib.request


class NoRedirect(urllib.request.HTTPRedirectHandler):
    """Refuse to follow redirects."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        """Return None so a redirect raises an HTTPError."""
        return None


def number_of_subscribers(subreddit):
    """Return the total subscribers of subreddit, or 0 if invalid."""
    if not subreddit or not isinstance(subreddit, str):
        return 0
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    request = urllib.request.Request(
        url, headers={"User-Agent": "linux:alu.scripting.api:v1.0"})
    opener = urllib.request.build_opener(NoRedirect)
    try:
        with opener.open(request, timeout=10) as response:
            data = json.loads(response.read().decode("utf-8"))
        return data.get("data", {}).get("subscribers", 0) or 0
    except Exception:
        return 0
