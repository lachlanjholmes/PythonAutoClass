"""
10. Using ciscoconfparse find the crypto maps that are not using AES (based-on the transform set name). 
Print these entries and their corresponding transform set name.
"""

from ciscoconfparse import CiscoConfParse

def main():
    cisco_file = 'cisco_ipsec.txt'

    output = CiscoConfParse(cisco_file)
    crypto_output = output.find_objects_wo_child(parentspec=r'crypto map CRYPTO',childspec=r'set transform-set AES-SHA')

    for child in crypto_output:
        print(child.text)

if __name__ == "__main__":
    main()