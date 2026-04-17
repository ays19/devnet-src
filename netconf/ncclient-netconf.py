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

# XML for the duplicate IP test (Loopback 2 with IP 10.1.1.1)
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
    # Send the configuration (this is expected to raise an error )
    netconf_reply = m.edit_config(target="running", config=netconf_newloop)
except Exception as e:
    # Print the error as per lab instructions
    print(f"An error occurred: {e}")
finally:
    # Close the session
    m.close_session()
