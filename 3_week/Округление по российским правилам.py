from math import ceil, floor

a = float(input())
b = floor(a)
c = a - b
if c >= 0.5:
    b += 1
    print(b)
else:
    print(b)
