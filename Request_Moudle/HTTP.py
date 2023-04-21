import requests
import json
#import jsonpath

payload = {'username':'corey', 'password': 'testing'}
url = "http://httpbin.org/basic-auth/corey/testing"
response = requests.get(url, auth=('coreysd','testing'))
print(response.text)