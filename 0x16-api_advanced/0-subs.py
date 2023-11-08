#!/usr/bin/python3
"""
number of subscribers for a given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """
    A function that queries the Reddit API 
    and returns the number of subscribers.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-agent': 'Microsoft Edge Version 119.0.2151.44'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json()
    return results.get('data').get('subscribers')
