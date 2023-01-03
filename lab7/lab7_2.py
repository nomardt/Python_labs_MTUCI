def count_binary_1s(octet: int) -> int:
    octet_binary = format(octet, 'b')
    return octet_binary.count('1')

if __name__ == '__main__':
    mask = input("Please enter mask in format 'decimal with point': ")

    mask_list = mask.split('.')
    mask_1s_counter = 0

    for octet in mask_list:
        mask_1s_counter += count_binary_1s(int(octet))

    print('\\' + str(mask_1s_counter))