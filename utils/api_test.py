
import requests


url = "http://35.234.147.205:80"

data = {"start_url": "https://www.businessinsider.com/peter-thiel-facebook-trump-biography-2018-2?r=US&IR=T",
        "article": "article9",
        "jumpdist": 0.5}

res = requests.get(url, data)

print(res.json())