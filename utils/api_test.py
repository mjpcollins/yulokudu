
import requests


url = "http://35.234.147.205:5000"
# url = "http://127.0.0.1:5000"

data = {"start_url": "https://www.businessinsider.com/peter-thiel-facebook-trump-biography-2018-2?r=US&IR=T",
        "article": "article9",
        "jumpdist": 0.5}

print("send")

res = requests.get(url, data)

print(res.json())

