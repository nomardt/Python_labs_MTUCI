import ipaddress

def get_ip(ip_number: int) -> string:
    raw_input = input('Enter the IP address number ' + str(ip_number) + ':')

    try:
        return ipaddress.ip_address(raw_input)
    except ValueError:
        print('Try again!')
        return get_ip(ip_number)

if __name__ == '__main__':
    ip_1 = get_ip(1)
    ip_2 = get_ip(2)
    ip_3 = get_ip(3)

    print('\nIP nu 1: {}\nIP nu 2: {}\nIP nu 3: {}'.format(ip_1, ip_2, ip_3))