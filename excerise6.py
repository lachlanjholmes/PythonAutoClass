"""
Write a Python program that creates a list. 
One of the elements of the list should be a dictionary with at least two keys. 
Write this list out to a file using both YAML and JSON formats. 
The YAML file should be in the expanded form.
"""

my_dictionary = {
    'ip' : '1.1.1.1',
    'device' : 'cisco_ios'
}

my_list = []

my_list.append(my_dictionary)

print(my_list)
