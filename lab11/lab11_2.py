import yaml
from pprint import pprint

with open('lab11_2_yaml.yml', 'r') as file_object:
    data = file_object.read()
    print(data)
    pprint(yaml.safe_load(data))