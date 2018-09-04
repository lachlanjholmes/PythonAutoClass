"""
8. Write a Python program using ciscoconfparse that parses this config file. 
Note, this config file is not fully valid (i.e. parts of the configuration are missing). 
The script should find all of the crypto map entries in the file (lines that begin with 'crypto map CRYPTO')
and for each crypto map entry print out its children.
"""

from ciscoconfparse import CiscoConfParse

def main():
    cisco_file = 'cisco_ipsec.txt'

    output = CiscoConfParse(cisco_file)
    crypto_output = output.find_children(r'crypto map CRYPTO')

    for child in crypto_output:
        print(child)

if __name__ == "__main__":
    main()
