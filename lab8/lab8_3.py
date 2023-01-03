ip_addr_list = [f"10.10.100.{i}" for i in range(1, 255)]

for c, el in enumerate(ip_addr_list):
    print(str(c) + " ---> " + el)

new_ip_addr_list = ip_addr_list[2:6]
for ip_addr in new_ip_addr_list:
    print(ip_addr)