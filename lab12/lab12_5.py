def receive_input():
    while(inputted := input()) != 'end':
        yield inputted

if __name__ == '__main__':
    all_user_input = list(receive_input())
    
    filtered_received_input = []
    for item in all_user_input:
        if item.isalpha():
            filtered_received_input.append(item)

    print(filtered_received_input)