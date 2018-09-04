"""
9. Find all of the crypto map entries that are using PFS group2
"""

from ciscoconfparse import CiscoConfParse

def main():
    cisco_file = 'cisco_ipsec.txt'

    output = CiscoConfParse(cisco_file)
    crypto_output = output.find_objects_w_child(parentspec=r'crypto map CRYPTO',childspec=r'set pfs group2')

    for child in crypto_output:
        print(child.text)

if __name__ == "__main__":
    main()