"""
Write a Python program that reads both the YAML file and the JSON file created in exercise6 and pretty prints the data structure that is returned.
"""
import yaml
import json
# import os
from pprint import pprint

# path = os.getcwd()
# print(path)

def output_format(my_list, my_str):
    """Make the output format easier to read."""
    print('\n')
    print('#'*30,'{my_str:}'.format(my_str=my_str),'#'*30)
    pprint(my_list)
    print('#'*66)

def main():
    with open('yaml_list.yml','r') as f:
        yaml_output = yaml.load(f)

    with open('json_list.json','r') as f:
        json_output = json.load(f)

    output_format(yaml_output,'YAML')
    output_format(json_output,'JSON')
    # print('#'*66)

if __name__ == "__main__":
    main()
