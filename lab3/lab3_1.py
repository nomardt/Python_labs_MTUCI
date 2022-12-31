ip_list = [
    '10.1.1.1',
    '10.1.1.2',
    '10.1.1.3',
    '10.1.1.2',
    '10.1.1.3',
    '10.1.1.1',
    '10.1.1.1',
    '10.1.1.2'
]

ip_list = list(set(ip_list))

def bubble_sorted(lst: list) -> list:
    """
    My implementation of the bubble sort algorithm
    """
    swaps_occured = True
    while swaps_occured:
        swaps_occured = False

        for i, val in enumerate(lst):
            try:
                if lst[i] > lst[i + 1]:
                    lst.insert(i + 2, val)
                    lst.pop(i)

                    swaps_occured = True
                    
            except IndexError:
                pass
            
    return lst

ip_sorted = bubble_sorted(ip_list)
print(ip_sorted)

len_iplist = len(ip_sorted)
print(len_iplist)