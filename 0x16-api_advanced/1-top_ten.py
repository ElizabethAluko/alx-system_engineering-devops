#!/usr/bin/python3
"""Use Reddit API to get the top 10 titles of hot posts"""
import requests


def top_ten(subreddit):
    """Gets top 10 titles of hot post"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User_Agent': 'YourBot/1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    data = response.json()
    for post in data['data']['children']:
        print(post['data']['title'])
