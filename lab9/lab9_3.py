with open('show_arp.txt', 'r') as data:
    sh_vlan = data.readlines()

    for line in sh_vlan:
        line_elements = line.split()

        default_found = False
        arista3_found = False

        if line_elements[0] == 'Internet':
            ip_addr = line_elements[1]
            mac_addr = line_elements[3]

            if ip_addr == '10.220.88.1':
                print("Default IP/MAC of router:", ip_addr, mac_addr)
                default_found = True
            elif ip_addr == '10.220.88.30':
                print("Arista 3 IP/MAC is", ip_addr, mac_addr)
                arista3_found = True

            if default_found and arista3_found:
                break
            
