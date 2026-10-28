# api_advanced

Python scripts that query the Reddit API (no authentication, custom
User-Agent, redirects are never followed).

- `0-subs.py`: `number_of_subscribers(subreddit)` returns total subscribers
- `1-top_ten.py`: `top_ten(subreddit)` prints the first 10 hot titles
- `2-recurse.py`: `recurse(subreddit, hot_list=None)` returns all hot titles
- `3-count.py`: `count_words(subreddit, word_list)` prints keyword counts
