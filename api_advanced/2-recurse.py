#!/usr/bin/python3
"""Recursively collect the titles of all hot posts of a subreddit."""
import json
import urllib.request


class NoRedirect(urllib.request.HTTPRedirectHandler):
    """Refuse to follow redirects."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        """Return None so a redirect raises an HTTPError."""
        return None


def recurse(subreddit, hot_list=None, after=None):
    """Return a list of all hot post titles, or None if invalid."""
    if hot_list is None:
        hot_list = []
    if not subreddit or not isinstance(subreddit, str):
        return None
    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    if after:
        url += "&after={}".format(after)
    request = urllib.request.Request(
        url, headers={"User-Agent": "linux:alu.scripting.api:v1.0"})
    opener = urllib.request.build_opener(NoRedirect)
    try:
        with opener.open(request, timeout=10) as response:
            data = json.loads(response.read().decode("utf-8"))["data"]
        children = data["children"]
        next_after = data.get("after")
    except Exception:
        return hot_list if after else None
    hot_list.extend(child["data"]["title"] for child in children)
    if next_after:
        return recurse(subreddit, hot_list, next_after)
    return hot_list
