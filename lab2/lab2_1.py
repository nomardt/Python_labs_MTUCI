# Task 1
ip_list = [
    '10.1.1.1',
    '10.1.1.2',
    '10.1.1.3',
    '10.1.1.4',
    '10.1.1.5'
]

print(ip_list[0], ip_list[-1])

# Task 2
ip_list.append('10.2.1.1')
ip_list.extend(['10.3.1.1', '10.3.1.2'])
ip_list = ip_list + ['172.16.1.1', '172.16.1.2', '172.16.1.3']
print(ip_list)
print(ip_list[1], ip_list[-2])
ip_list.pop(0); ip_list.pop(-1)
ip_list[0] = '2.2.2.2'
print(ip_list[0])
print(ip_list)