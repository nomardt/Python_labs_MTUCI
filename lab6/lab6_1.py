mac1 = "Internet 10.220.88.29 94 5254.abbe.5b7b ARPA FastEthernet4"
mac2 = "Internet 10.220.88.30 3 5254.ab71.e119 ARPA FastEthernet4"
mac3 = "Internet 10.220.88.32 231 5254.abc7.26aa ARPA FastEthernet4"

# Following PEP3101 guidelines

# Header
print(f"{'IP ADDRESS':>20} {'MAC ADDRESS':>20}\n{' ':-^41}")
# Main Body
for data_element in map(lambda x: x.split(), (mac1, mac2, mac3)):
    print(f"{data_element[1]:>20} {data_element[3]:>20}")