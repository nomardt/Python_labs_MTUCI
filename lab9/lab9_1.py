# Task 1
list_devices = []

with open("devices.txt", 'r+') as file_object:

    for item in file_object:
        item = item.rstrip()
        list_devices.append(item)

print(list_devices)

# Task 2
with open("devices.txt", 'r+') as data_2:
    old_text = data_2.readlines()

    data_2.seek(0)
    data_2.write("THE BEGINNING!!!\n")

    for line in old_text:
        data_2.write(line)

    data_2.write("\nTHE END!!!\n")

    # Printing the new file
    data_2.seek(0)
    for new_line in data_2:
        print(new_line.rstrip())
