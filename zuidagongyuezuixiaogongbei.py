def zdgy(x, y):
    """求最大公约"""
    (x, y) = (y, x) if x > y else x, y
    for i in range(x, 0, -1):
        if y % i == 0 and x % i == 0:
            return i


def zgb(x, y):
    """求最小公倍"""
    return x * y / zdgy(x, y)


