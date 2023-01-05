nums = [45, 36, 39, 37, 130, 105, 220, 169]
new_nums = []

fun = lambda x: not x % 13
print([num for num in nums if fun(num)])