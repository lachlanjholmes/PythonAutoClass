"""
Write a Python program that reads both the YAML file and the JSON file created in exercise6 and pretty prints the data structure that is returned.
"""
import yaml
import json
from pprint import pprint


with open('yaml_list.yml','r') as f:
    yaml_output = yaml.load(f)

with open('json_list.json' ,'r') as f:
    json_output = json.load(f)


pprint(yaml_output)

pprint(json_output)


