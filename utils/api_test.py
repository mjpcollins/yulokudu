
import requests


url = "http://127.0.0.1:5000"

data = {"start_url": "https://en.wikipedia.org/wiki/Battle_of_Gala%C8%9Bi"}

res = requests.get(url, data)

print(res.json())