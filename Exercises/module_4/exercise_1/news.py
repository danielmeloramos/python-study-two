#1- http
import requests

API_URL = "https://newsapi.org/v2/top-headlines?country=br&category=business&apiKey=05cbecbe23be44a6bb9f7f6358f3ca5e"

response = requests.get(API_URL)
data = response.json()
titles = []
for item in data["articles"]:
    titles.append(item['title'])

with open('titles.txt', 'w') as f:
    for title in titles:
        f.write(title)
        f.write('\n')
    