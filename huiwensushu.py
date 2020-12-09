import huiwen as hw
import sushupanduan as sspd

def huiwensushu(x):
    return hw.ishuiwen(x) and sspd.sushu(x)


print(huiwensushu(313))