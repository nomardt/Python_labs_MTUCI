ip_address = input("Please enter IP address in format 'decimal with point': ")
network_octet = int(ip_address.split('.')[0])

if network_octet < 127:
    print("Class A network")
elif network_octet < 192:
    print("Class B network")
elif network_octet < 224:
    print("Class C network")
elif network_octet < 240:
    print("Class D network")
elif network_octet < 256:
    print("Class E network")