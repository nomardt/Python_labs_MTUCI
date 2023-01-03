device = {
    'ip': '10.10.10.12',
    'username': 'user',
    'password': 'pass',
}
print('The value at password is ' + device['password'])

device_key = device.keys()
device_value = device.values()

add_config = {
    'device_type': 'huawei',
        'session_log': 'output.txt'
}

device.update(add_config)
print(device)