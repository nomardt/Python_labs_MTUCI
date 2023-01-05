def ssh_conn(ip_address: str, username: str, password: str):
    print(f"\nIP: {ip_address}\nUsername: {username}\nPassword: {password}")

if __name__ == '__main__':
    ssh_conn('0.0.0.0', 'null', 'null')
    ssh_conn(ip_address='192.168.0.1', password='Hleb', username='Gleb')
    ssh_conn('192.168.0.2', 'Admin', password='admin')