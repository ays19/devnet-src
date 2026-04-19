import requests

access_token = 'ZWI1NTBkYzktMzBmYy00ZmJmLTg5Y2UtMTU0ZmM0NmQ2YjkyOTUyYTZkMmItNDhk_P0A1_3053e3a2-13b5-4c1e-8fee-32c0000aec9d'
url = 'https://webexapis.com/v1/rooms'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params={'max': '100'}
res = requests.get(url, headers=headers, params=params)
print(res.json())