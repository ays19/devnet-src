import requests

access_token = 'ZWI1NTBkYzktMzBmYy00ZmJmLTg5Y2UtMTU0ZmM0NmQ2YjkyOTUyYTZkMmItNDhk_P0A1_3053e3a2-13b5-4c1e-8fee-32c0000aec9d'
room_id = 'Y2lzY29zcGFyazovL3VzL1BFT1BMRS85YzYwZDc4Mi1lNjY3LTQ0ZGItOWM4My03ZGY3ZDdlMGRhYmU'
url = 'https://webexapis.com/v1/rooms/{}/meetingInfo'.format(room_id)
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
res = requests.get(url, headers=headers)
print(res.json())