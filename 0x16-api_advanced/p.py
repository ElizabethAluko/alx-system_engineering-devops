import requests

subreddit = 'ruby'
url = f"https://www.reddit.com/r/{subreddit}/about.json"
headers = {'User_Agent': 'Browser/1.0'}

response = requests.get(url, headers=headers, allow_redirects=False)
if response.status_code == 200:
    data = response.json()
    if 'data' in data and 'subscribers' in data['data']:
        print(data['data']['subscribers'])
    else:
        print(0)
else:
    print(0)
