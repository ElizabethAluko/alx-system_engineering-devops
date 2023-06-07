#!/usr/bin/python3
"""
Recursive function that queries the Reddit API
"""


def recurse(subreddit, hot_list=None):
    """Return the titles of hot articles in Reddit API"""
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
