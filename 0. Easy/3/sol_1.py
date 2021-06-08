def check_nondec(list):
    num = 0
    for i in range(len(list)-1):
        if list[i] > list[i+1]:
            num += 1
    if num > 1:
        return 'Not Possible'
    else:
        return 'Possible'


return_val = check_nondec([4, 2, 1])
print(return_val)
