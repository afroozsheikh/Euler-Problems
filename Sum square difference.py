def square(n):
    list_1 = [x*x for x in range(1, n+1)]
    list_2 = [x for x in range(1, n+1)]
    sum_1 = sum_2 = 0
    for i in range(len(list_1)):
        sum_1 += list_1[i]
    for it in range(len(list_2)):
        sum_2 += list_2[it]

    print((sum_2 * sum_2) - sum_1)


square(100)
