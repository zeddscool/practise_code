def ishuiwen(x):
    """判断是不是回文数"""
    temp = x
    y = 0
    while temp > 0:
        y = y * 10 + temp % 10
        temp //= 10
    return y == x