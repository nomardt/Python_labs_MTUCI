import yaml

with open('yaml_int1.yml', 'r') as file_object:
    print(yaml.safe_load(file_object.read()))