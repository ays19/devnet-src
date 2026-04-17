from ncclient import manager
import xml.dom.minidom
import sys

# Connection parameters for the Cisco Cat8kv Sandbox
# Note: device_params={'name': 'iosxe'} is CRITICAL for Cat8kv (IOS-XE 17.x)
m = manager.connect(
    host="10.10.20.48",
    port=830,
    username="developer",
    password="C1sco12345",
    hostkey_verify=False,
    device_params={'name': 'iosxe'}
)

# --- Part 3: Display Capabilities ---
print("#Supported Capabilities (YANG models):")
for capability in m.server_capabilities:
    print(capability)

# --- Part 4: Retrieve Full Configuration ---
print("\n# Retrieving Full Running Configuration...")
netconf_reply = m.get_config(source="running")
# Note: Full config can be very large, printing just a snippet or status
print("Full configuration retrieved successfully.")

# --- Part 4: Retrieve Filtered Configuration (Native) ---
print("\n# Retrieving Filtered (Native) Configuration...")
netconf_filter = """
<filter>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native" />
</filter>
"""
netconf_reply = m.get_config(source="running", filter=netconf_filter)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

# --- Part 5: Configure Hostname ---
# FIX: Added explicit namespaces to the <config> tag for Cat8kv compatibility
print("\n# Configuring Hostname...")
netconf_hostname = """
<config xmlns:xc="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <hostname>CAT8KV-LAB</hostname>
    </native>
</config>
"""
netconf_reply = m.edit_config(target="running", config=netconf_hostname)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

# --- Part 5: Create Loopback 1 ---
print("\n# Creating Loopback 1...")
netconf_loopback = """
<config xmlns:xc="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
            <Loopback>
                <name>1</name>
                <description>My NETCONF loopback</description>
                <ip>
                    <address>
                        <primary>
                            <address>10.1.1.1</address>
                            <mask>255.255.255.0</mask>
                        </primary>
                    </address>
                </ip>
            </Loopback>
        </interface>
    </native>
</config>
"""
netconf_reply = m.edit_config(target="running", config=netconf_loopback)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

# --- Part 5: Attempt Duplicate IP (Loopback 2) ---
print("\n# Attempting to create Loopback 2 with Duplicate IP (Expected to fail)...")
netconf_newloop = """
<config xmlns:xc="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
            <Loopback>
                <name>2</name>
                <description>My second NETCONF loopback</description>
                <ip>
                    <address>
                        <primary>
                            <address>10.1.1.1</address>
                            <mask>255.255.255.0</mask>
                        </primary>
                    </address>
                </ip>
            </Loopback>
        </interface>
    </native>
</config>
"""

try:
    netconf_reply = m.edit_config(target="running", config=netconf_newloop)
    print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
except Exception as e:
    print(f"Error as expected: {e}")

# --- Close Session ---
m.close_session()
print("\n# NETCONF Session Closed.")