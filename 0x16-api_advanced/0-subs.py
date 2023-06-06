#!/usr/bin/python3
"""Use Reddit API to get the number of a subscribbers"""

import requests


def number_of_subscribers(subreddit):
    """Return number of subscribers"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User_Agent': 'custom-agent/0.0.1'}

    response = requests.request(
            "GET", url, headers=headers,
            allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        if "data" in data and "subscribers" in data['data']:
            return data["data"]["subscribers"]
        else:
            return 0
    else:
        return 0
