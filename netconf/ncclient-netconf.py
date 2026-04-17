from ncclient import manager
import xml.dom.minidom

# Connection parameters for the Cisco Cat8kv Sandbox
m = manager.connect(
    host="10.10.20.48",
    port=830,
    username="developer",
    password="C1sco12345",
    hostkey_verify=False,
    device_params={'name': 'iosxe'}
)

# Define the loopback configuration XML
netconf_loopback = """
<config xmlns:xc="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
            <Loopback>
                <name>1</name>
                <description>My first NETCONF loopback</description>
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
    # Send the configuration and store the results
    netconf_reply = m.edit_config(target="running", config=netconf_loopback )

    # Print the prettified XML response
    print("NETCONF Reply for Loopback Configuration:")
    print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Gracefully close the session
    m.close_session()
