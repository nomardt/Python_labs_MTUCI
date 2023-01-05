def ssh_conn2(ip_address: str, username: str, password: str, device_type: str = 'huawei_vrp') -> None:
    print(f"\nIP: {ip_address}\nUsername: {username}\nPassword: {password}")
    print(f"Device: {device_type}")

if __name__ == '__main__':
    ssh_conn2('0.0.0.0', 'null', 'null', 'null')
    ssh_conn2('10.0.1.0', 'admin', 'admin')

    my_node = {
        'ip_address': '10.0.0.1',
        'username': 'me',
        'password': '123secure'
    }
    ssh_conn2(**my_node)