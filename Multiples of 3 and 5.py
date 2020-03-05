def multi(n):
    sum3 = 0
    sum5 = 0
    for i in range(n):
        if i % 3 == 0:
            sum3 += i
        elif i % 5 == 0:
            sum5 += i
    print(sum3 + sum5)


multi(1000)

