from time import sleep


def generate_prime_factors(x):
    prime_factors = set()
    divisor = 2
    while divisor <= x:
        if x % divisor == 0:
            prime_factors.add(divisor)
            x = x/divisor
        else:
            divisor += 1
    return prime_factors


def nth_super_ugly(number, primes):
    ugly_list = [1]
    natural_number = 2
    while len(ugly_list) < number:
        sleep(1)
        prime_list = list(generate_prime_factors(natural_number))
        print(f"{natural_number} gives prime factors of {prime_list}")
        for i in prime_list:
            if i not in primes:
                break
        else:
            print(f"{natural_number} has been append to the {ugly_list}")
            ugly_list.append(natural_number)

        natural_number += 1

    return None


nth_super_ugly(12, [2, 7, 13, 19])
