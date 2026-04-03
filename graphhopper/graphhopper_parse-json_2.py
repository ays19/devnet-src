import requests
import urllib.parse

geocode_url = "https://graphhopper.com/api/1/geocode?"
route_url = "https://graphhopper.com/api/1/route?"
loc1 = "Washington, D.C."
loc2 = "Baltimore, Maryland"
key = "63c82c8f-f0ce-4edd-95fa-70b5c1133f69"

url = geocode_url + urllib.parse.urlencode({"q":loc1, "limit": "1", "key":key})

replydata = requests.get(url)
json_data = replydata.json()
json_status = replydata.status_code

json_status = replydata.status_code

if json_status == 200:
    print("Geocoding API URL for " + loc1 + ":\n" + url)