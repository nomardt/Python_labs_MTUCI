import json
from pprint import pprint

with open('interface_config.json', 'r') as data:
    json_text = data.read()
    print("The type of the variable is", type(json_text))
    print("The content of the variable json_text is\n", json_text)

    json_data = json.loads(json_text)
    print("The type of the variable is", type(json_data))
    print("The content of the variable json_data is")
    pprint(json_data)