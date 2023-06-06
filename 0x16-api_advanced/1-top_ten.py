#!/bin/usr/python3
"""Get top ten tiles"""
import requests


def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'YourBot/1.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            for post in data['data']['children']:
                if 'data' in post and 'title' in post['data']:
                    print(post['data']['title'])
        else:
            print("No posts found.")
    else:
        print("Invalid subreddit.")

# Example usage
subreddit = 'python'
top_ten(subreddit)
