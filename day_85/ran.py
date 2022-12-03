import requests

data = requests.get("https://api.spaceflightnewsapi.net/v3/articles")

data =data.json()
print(data)