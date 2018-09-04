"""
10. Using ciscoconfparse find the crypto maps that are not using AES (based-on the transform set name). 
Print these entries and their corresponding transform set name.
"""

from ciscoconfparse import CiscoConfParse

def main():
    cisco_file = 'cisco_ipsec.txt'

    output = CiscoConfParse(cisco_file)
    crypto_output = output.find_objects_wo_child(parentspec=r'crypto map CRYPTO',childspec=r'AES')

for i in crypto_output:
    for child in i.children:
        if 'transform' in child.text:
                match = re.search(r'set transform-set (\S*)', child.text)
                # print(match)
                encryption = match.group(1)
    print(i.text.strip(),">", encryption)

if __name__ == "__main__":
    main()