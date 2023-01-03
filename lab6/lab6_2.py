import ipaddress

def get_ip_address():
    ip_address = input("Please enter IP address in format 'decimal with point': ")
    
    try:
        ipaddress.ip_address(ip_address)
        return ip_address
    except ValueError:
        print("Please try again!")
        return get_ip_address()

if __name__ == '__main__':
    ip_address = get_ip_address()
    
    # The header
    print(f"\n{'Octet1':^20}{'Octet2':^20}{'Octet3':^20}{'Octet4':^20}")
    print('-' * 80)

    # The main content
    octet_list = list(map(int, ip_address.split('.')))
    print(f"{octet_list[0]:^20}{octet_list[1]:^20}{octet_list[2]:^20}{octet_list[3]:^20}")
    print(f"{octet_list[0]:^#20b}{octet_list[1]:^#20b}{octet_list[2]:^#20b}{octet_list[3]:^#20b}")
    print(f"{octet_list[0]:^#20x}{octet_list[1]:^#20x}{octet_list[2]:^#20x}{octet_list[3]:^#20x}")    

    # The footer
    print('-' * 80)