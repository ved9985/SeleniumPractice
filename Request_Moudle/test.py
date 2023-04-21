import requests
from requests.exceptions import HTTPError

for url in ['https://api.github.com', 'https://api.github.com/invalid']:
    print(url)
    try:
        response = requests.get(url)
        print(response)
        print(response.json())
        print(response.headers)

        # If the response was successful, no Exception will be raised
        c=response.raise_for_status()
        print(f"{c=}")
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('Success!')