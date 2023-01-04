import json
from pprint import pprint

with open('interface_config.json', 'r') as data:
    json_data = json.loads(data.read())
    pprint(json_data["ietf-interfaces:interface"])

    print("\nInterface's IP address:")
    pprint(json_data["ietf-interfaces:interface"]["ietf-ip:ipv4"]["address"][0]["ip"])