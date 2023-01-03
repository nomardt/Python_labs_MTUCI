# Task 1
list_devices = []

with open("devices.txt", 'r+') as file:

    for item in file:
        item = item.rstrip()
        list_devices.append(item)

print(list_devices)

# Task 2
with open("devices.txt", 'r+') as file_2:
    old_text = file_2.readlines()

    file_2.seek(0)
    file_2.write("THE BEGINNING!!!\n")

    for line in old_text:
        file_2.write(line)

    file_2.write("\nTHE END!!!\n")

    # Printing the new file
    file_2.seek(0)
    for new_line in file_2:
        print(new_line.rstrip())
