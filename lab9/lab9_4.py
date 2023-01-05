with open('show_lldp_neighbors_detail.txt', 'r') as file_object:
    lines = file_object.readlines()

    port_id_found     = False
    system_name_found = False

    for line in lines:
    
        if "Port id" in line:
            words = line.split()
            print("Port id found, yay!", words[2])
            port_id_found = True
        elif "System Name" in line:
            words = line.split()
            print("System name found, yay!", words[2])
            system_name_found = True

        if port_id_found and system_name_found:
            break