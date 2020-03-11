def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def prime_n(n):
    count = 3
    i = 3
    while count != n+1:
        i += 2
        if is_prime(i):
            count += 1
    return i


print(prime_n(10001))




