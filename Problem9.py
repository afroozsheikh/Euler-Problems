for i in range(1000):
    for j in range(1000):
        a = i
        b = j
        c = 1000 - (i + j)
        if pow(a, 2) + pow(b, 2) == pow(c, 2):
            print(a*b*c)

