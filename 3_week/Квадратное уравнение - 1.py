import numpy as np

a = float(input())
b = float(input())
c = float(input())

if a != 0:
    d = b**2 - 4*a*c
    if d > 0:
        x1 = ((-b + np.sqrt(d)) / (2 * a))
        x2 = ((-b - np.sqrt(d)) / (2 * a))
        if x2 >= x1:
            print(round(x1, 4), round(x2, 4))
        else:
            print(round(x2, 4), round(x1, 4))
    elif d == 0:
        x0 = (-b / (2 * a))
        print(round(x0, 4))
