for i in range(0, 1001):
    count = 0
    for j in range(1, i):
        if i % j == 0:
           count += j
    if i == count:
        print(i)