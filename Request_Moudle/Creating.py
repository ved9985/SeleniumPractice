import requests
import json
#import jsonpath


url = "https://reqres.in/api/users"
res = requests.get(url)
file = open("C:\\Users\\HI\\Desktop\\post.json", 'r')
json_input= file.read()
res_json= json.loads(json_input)
print(f"{res_json=}")

response= requests.post(url,res_json)

print(f"{response.status_code = }")
assert response.status_code == 201
