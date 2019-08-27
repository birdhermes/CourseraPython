import numpy as np

n = int(input())

def MinDivisor(n):
    mindelit = np.sqrt(n)
    return mindelit

if MinDivisor(n) % 2 == 0:
    print(mindelit)
else:
    print(n)
