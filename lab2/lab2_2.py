import random

acl_list = [random.randint(1, 199) for i in range(10)]
acl_list.sort()
print(acl_list)

first_acl_el = acl_list.pop(0)
acl_list.insert(-1, first_acl_el)
last_acl_el = acl_list.pop(-1)
acl_list.insert(0, last_acl_el)
print(acl_list)

acl_list.reverse()
acl_list = acl_list[::-1]
print(acl_list)

acl_list1 = acl_list[:5]
acl_list2 = acl_list[5:]
print(acl_list1)
print(acl_list2)