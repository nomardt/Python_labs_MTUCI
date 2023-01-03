show_version = " *0 CISCO881-SEC-K9 FTX0000038X   "
show_version = show_version.strip()
show_version = show_version.split()
print(show_version[1], show_version[2], '\n')

for element in show_version:
    element = element.lower()
    
    if 'cisco' in element:
        print('It is a cisco device!')

    if str(881) in element:
        print('"881" found!')

print('The serial number of the device is ' + show_version[1])