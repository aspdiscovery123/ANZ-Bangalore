import requests
import json

url="http://127.0.0.1:8000/"
data=json.dumps({"ex":45})
r=requests.post(url,data)
print(r.content)


