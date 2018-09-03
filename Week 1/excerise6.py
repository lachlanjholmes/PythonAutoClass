"""
Write a Python program that creates a list. 
One of the elements of the list should be a dictionary with at least two keys. 
Write this list out to a file using both YAML and JSON formats. 
The YAML file should be in the expanded form.
"""
import yaml
import json

def listie():

    my_dictionary = {
        'ip' : '1.1.1.1',
        'device' : 'cisco_ios'
    }

    my_list = []
    my_list.append(my_dictionary)
    my_list.append('random_string')
    my_list.append('Another one')

    # print(my_list[:])
    # yaml Dumping
    with open('yaml_list.yml','w') as f:
        f.write(yaml.dump(my_list, default_flow_style=False))
    # Json Dumping    
    with open('json_list.yml','w') as f:
        json.dump(my_list, f)

if __name__ == "__main__":
    listie()
