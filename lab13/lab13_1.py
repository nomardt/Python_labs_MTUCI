try:
    file_object = open('lab13_1.txt', 'r')

    print("The file has been found!\n")
    print(file_object.read())

    file_object.close()

except FileNotFoundError:
    print("The file doesn't exist, let's create it!")
    filename = input("Enter the name of the file you'd like to create: ")
    if filename != 'lab13_1.txt':
        print("Something went wrong...")
        quit()
    
    file_object = open(filename, 'w')

    config_acl = 'acl 3001 \nrule 5 permit tcp source 10.1.4.1 0 destination-port eq telnet \nrule 10 deny tcp'
    file_object.write(config_acl)

    file_object.close()

    with open(filename, 'r') as new_file_object:
        print('\n' + new_file_object.read())

except:
    print("Unknown error!")