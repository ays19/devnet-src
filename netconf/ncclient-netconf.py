from ncclient import manager
import xml.dom.minidom

# Connection parameters
m = manager.connect(
    host="10.10.20.48",
    port=830,
    username="developer",
    password="C1sco12345",
    hostkey_verify=False,
    device_params={'name': 'iosxe'}  # Crucial for Cat8kv/IOS-XE 17.x
)

# XML with explicit NETCONF namespaces
netconf_hostname = """
<config xmlns:xc="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <hostname>CAT8KV-NEW</hostname>
    </native>
</config>
"""

try:
    netconf_reply = m.edit_config(target="running", config=netconf_hostname )
    print("NETCONF Reply for Hostname Change:")
    print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
finally:
    m.close_session()
