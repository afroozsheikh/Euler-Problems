import math


def largest_prime(n):
    while n % 2 == 0:
        n /= 2

    max_prime = 0
    for i in range(3, int(math.sqrt(n)), 2):
        if n % i == 0:
            n /= i
            if i > max_prime:
                max_prime = i

    print(max_prime)


largest_prime(600851475143)
