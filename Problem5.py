from math import gcd


def lcm_of_2(x, y):
    return x * y // gcd(x, y)


def function(n):
    lcm_num = 1
    for i in range(2, n):
        lcm_num = lcm_of_2(i, lcm_num)

    return lcm_num


print(function(20))
