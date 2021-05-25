h = eval(input('Enter the list of numbers in Hand: '))  # [1,2,3,6,2,3,4,7,8]
w = int(input('Enter the value of W: '))  # 3
wgroups = []
for n in h:
    group = []
    for i in range(0, w):  # Check for consecutive w integers.
        if n + i in h:
            group.append(n + i)
        elif n + i not in h:
            break
    else:
        if group not in wgroups:
            wgroups.append(group)
if len(wgroups) >= w:
    print('true')
else:
    print('false')
