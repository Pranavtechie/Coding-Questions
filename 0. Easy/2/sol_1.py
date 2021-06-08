def return_factorial(number):
    sum = 1
    for i in range(1, number+1):
        sum *= i
    return sum


val = return_factorial(5)
print(val)
