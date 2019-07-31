from math import floor, ceil

a = float(input())
b = round(a)
c = ceil((a - b)*100)
print(b, ' ', c)
