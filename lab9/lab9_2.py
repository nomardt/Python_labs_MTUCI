from pprint import pprint

with open('show_vlan.txt', 'r') as data:
    sh_vlan = data.readlines()
    vlans = []

    for line_number, line in enumerate(sh_vlan):
        characteristics = line.split()

        if len(characteristics) > 2 and line_number > 1:
            characteristics = line.split()
            id_and_name = (characteristics[0], characteristics[1])
            vlans.append(id_and_name)

    pprint(vlans)

