from random import randint, sample, randrange


def display(balls):
    a = len(balls)
    for i in range(a):
        if i == a - 2:
            print('%.f |' % balls[i], end=' ')
        else:
            print('%02d' % balls[i], end=' ')
    print()



def random_select():
    x = [x for x in range(1, 34)]
    y = sample(x, 6)
    y.sort()
    y.append(randint(1, 16))
    return y

def main():
    a = int(input('选几注：'))
    for i in range(a):
        display(random_select())

main()