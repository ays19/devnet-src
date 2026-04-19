import requests

access_token = 'ZWI1NTBkYzktMzBmYy00ZmJmLTg5Y2UtMTU0ZmM0NmQ2YjkyOTUyYTZkMmItNDhk_P0A1_3053e3a2-13b5-4c1e-8fee-32c0000aec9d'
url = 'https://webexapis.com/v1/rooms'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params={'title': 'DevNet Associate Training!'}
res = requests.post(url, headers=headers, json=params)
print(res.json())