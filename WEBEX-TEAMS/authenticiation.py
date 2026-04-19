import requests
import json

access_token = 'ZWI1NTBkYzktMzBmYy00ZmJmLTg5Y2UtMTU0ZmM0NmQ2YjkyOTUyYTZkMmItNDhk_P0A1_3053e3a2-13b5-4c1e-8fee-32c0000aec9d'
url = 'https://webexapis.com/v1/people/me'
headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}
res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))