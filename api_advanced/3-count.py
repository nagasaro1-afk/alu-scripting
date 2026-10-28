#!/usr/bin/python3
"""Recursively count keywords in the hot post titles of a subreddit."""
import json
import urllib.request


class NoRedirect(urllib.request.HTTPRedirectHandler):
    """Refuse to follow redirects."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        """Return None so a redirect raises an HTTPError."""
        return None


def print_counts(counts, words):
    """Print keyword totals sorted by count desc, then name asc."""
    totals = {}
    for word in set(words):
        total = counts.get(word, 0) * words.count(word)
        if total > 0:
            totals[word] = total
    for word, total in sorted(totals.items(), key=lambda i: (-i[1], i[0])):
        print("{}: {}".format(word, total))


def count_words(subreddit, word_list, after=None, counts=None):
    """Print a sorted count of keywords found in hot post titles."""
    if not subreddit or not isinstance(subreddit, str):
        return
    words = [word.lower() for word in word_list]
    if counts is None:
        counts = {}
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
        if after:
            print_counts(counts, words)
        return
    for child in children:
        for token in child["data"]["title"].lower().split():
            if token in words:
                counts[token] = counts.get(token, 0) + 1
    if next_after:
        return count_words(subreddit, word_list, next_after, counts)
    print_counts(counts, words)
