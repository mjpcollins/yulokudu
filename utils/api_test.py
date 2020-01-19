
import requests
import json


url = "http://35.246.63.255:5000"
# url = "http://0.0.0.0:5000"

data = {
    "start_url": "https://www.businessinsider.com/peter-thiel-facebook-trump-biography-2018-2?r=US&IR=T",
    "jumpdist": 0.5
}

print("send")

res = requests.get(url, data)



print(res.json())

