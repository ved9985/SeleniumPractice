import requests
import json

url = "https://reqres.in/api/users?page=2"

res = requests.get(url)

print(f"{res=}")
print(f"{res.status_code = }")
print(f"{res.content = }")
print(f"{res.json() = }")
print(f"{res.json()['page']= }")
print(f"{res.json()['data']= }")