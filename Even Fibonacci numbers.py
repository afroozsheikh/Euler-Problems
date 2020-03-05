def fibonacci(n):
    list_first = [1, 2]
    i = 0
    while int(list_first[i]) < int(n):
        list_first.append(list_first[i] + list_first[i+1])
        i += 1

    sum_num = 0
    for i in range(len(list_first)):
        if int(list_first[i]) % 2 == 0:
            sum_num += list_first[i]

    print(sum_num)


fibonacci(4000000)




