import json
import requests

# Disable SSL warnings for self-signed certificates
requests.packages.urllib3.disable_warnings()

# --- Step 2: Create variables for the request ---
# Router Details
api_url = "https://10.10.20.48/restconf/data/ietf-interfaces:interfaces/interface=Loopback2"
headers = { 
    "Accept": "application/yang-data+json",
    "Content-type": "application/yang-data+json"
}
basicauth = ("developer", "C1sco12345" )

# Step 2d: The YANG configuration dictionary (Note: 'True' is capitalized in Python)
yangConfig = {
    "ietf-interfaces:interface": {
        "name": "Loopback2",
        "description": "My second RESTCONF loopback",
        "type": "iana-if-type:softwareLoopback",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "10.2.1.1",
                    "netmask": "255.255.255.0"
                }
            ]
        },
        "ietf-ip:ipv6": {}
    }
}

# --- Step 3: Send the PUT request ---
print(f"Sending PUT request to create Loopback2 at {api_url}...")

resp = requests.put(
    api_url, 
    data=json.dumps(yangConfig), 
    auth=basicauth, 
    headers=headers, 
    verify=False
)

# --- Step 3b: Handle the response ---
if resp.status_code >= 200 and resp.status_code <= 299:
    print(f"STATUS OK: {resp.status_code}")
    print("Interface Loopback2 created successfully!")
else:
    print(f"Error. Status Code: {resp.status_code}")
    try:
        print(f"Error message: {json.dumps(resp.json(), indent=4)}")
    except:
        print(f"Raw Response: {resp.text}")

print("--- Script Finished ---")
