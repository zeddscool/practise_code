from random import randint

money = 100
while money > 0:
    print("拥有赌资：", money)
    res = randint(1, 6) + randint(1, 6)
    if res == 7 or res == 11:
        money *= 2
        print('玩家胜!赌资变为：', money)
    elif res == 2 or res == 3 or res == 12:
        money = 0
        print('庄家胜!')
    else:
        print('之前摇的点数为：%.f,继续摇' %(res))
        while money > 0:
            res2 = randint(1, 6) + randint(1, 6)
            if res2 == res:
                money *= 2
                print('玩家胜，赌资为：', money)
            elif res2 == 7:
                money = 0
                print('庄家胜')
                break
            else:
                continue
else:
    print("输光！")

