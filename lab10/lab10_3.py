import json
from pprint import pprint

with open('interfaces.json', 'r') as data:
    json_data = json.loads(data.read())
    pprint(json_data)

    for interface in json_data["ietf-interfaces:interfaces"]["interface"]:
        # Printing name
        print(interface["name"], ":", sep='', end=' ')
        # Printing IP address
        print(f"""{interface["ietf-ip:ipv4"]["address"][0]["ip"]}""", end=' ')
        # Printing netmask
        print(f"""{interface["ietf-ip:ipv4"]["address"][0]["netmask"]}""")