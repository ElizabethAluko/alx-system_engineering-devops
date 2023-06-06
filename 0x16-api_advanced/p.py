import requests

subreddit = 'ruby'
url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=1"
headers = {'User_Agent': 'Browser/1.0'}

response = requests.get(url, headers=headers, allow_redirects=False)
data = response.json()
print(data)
