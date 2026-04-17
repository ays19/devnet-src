import json
import requests

# Disable SSL warnings for self-signed certificates
requests.packages.urllib3.disable_warnings()

# Step 2a: Create the api_url variable (Using YOUR router IP)
api_url = "https://10.10.20.48/restconf/data/ietf-interfaces:interfaces"

# Step 2b: Create the headers dictionary
headers = { 
    "Accept": "application/yang-data+json",
    "Content-type": "application/yang-data+json"
}

# Step 2c: Create the basicauth tuple (Using YOUR credentials )
basicauth = ("developer", "C1sco12345")

# Step 3: Send the GET request
print(f"Fetching interface data from {api_url}...")
resp = requests.get(api_url, auth=basicauth, headers=headers, verify=False)

# Step 4: Format and display the JSON data
print(f"Status Code: {resp.status_code}")
response_json = resp.json()
print(json.dumps(response_json, indent=4))
