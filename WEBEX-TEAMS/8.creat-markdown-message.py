import requests

access_token = 'ZWI1NTBkYzktMzBmYy00ZmJmLTg5Y2UtMTU0ZmM0NmQ2YjkyOTUyYTZkMmItNDhk_P0A1_3053e3a2-13b5-4c1e-8fee-32c0000aec9d'
room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vMzY1MGEzODAtM2JlNS0xMWYxLWFhYjQtNTVkMDZkYmFiN2E0'
message = 'Hello **DevNet Associates**!!'
url = 'https://webexapis.com/v1/messages'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {'roomId': room_id, 'markdown': message}
res = requests.post(url, headers=headers, json=params)
print(res.json())