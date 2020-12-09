def yanghu(rows):
    for i in range(rows):
        if i == 0:
            x1 = [1]
            print(x1)
        elif i == 1:
            x1 = [1, 1]
            print(x1)
        else:
            x = [f for f in range(i + 1)]
            for j in range(i + 1):
                if j == 0 or j == i:
                    x[j] = 1
                else:
                    x[j] = x1[j - 1] + x1[j]
            print(x)
            x1 = x








