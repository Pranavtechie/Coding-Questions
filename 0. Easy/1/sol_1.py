def out_max_1(list_zero, list_one):
    count_zero = list_zero.split().count('1')
    count_one = list_one.split().count('1')
    if count_one > count_zero:
        return 1
    else:
        return 0


return_val = out_max_1("2 2", "0 1 1 1")
print(return_val)
