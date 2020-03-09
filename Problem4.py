def is_reverse(n):
    n1 = n
    m = 0
    while n > 0:
        r = n % 10
        m = m * 10 + r
        n = n // 10

    if m == n1:
        return True
    else:
        return False


def palindrome():
    max_num = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            if is_reverse(i * j):
                if i * j > max_num:
                    max_num = i * j
    print(max_num)


palindrome()



