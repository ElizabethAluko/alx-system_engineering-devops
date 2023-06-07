#!/usr/bin/python3

"""
This module contains a recursive function that queries the Reddit API and returns a list of hot article titles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=None):
    """
    Recursively queries the Reddit API and returns a list of hot article titles for a given subreddit.
    If no results are found or the subreddit is invalid, None is returned.

    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list, optional): A list to store the hot article titles. Defaults to None.

    Returns:
        list or None: A list containing the hot article titles or None if no results are found.
    """
    if hot_list is None:
        hot_list = []
    
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        if data.get('data') and data['data'].get('children'):
            children = data['data']['children']
            for child in children:
                title = child['data'].get('title')
                if title:
                    hot_list.append(title)
            after = data['data'].get('after')
            if after:
                return recurse(subreddit, hot_list=hot_list)
            else:
                return hot_list
        else:
            return hot_list
    else:
        return None
