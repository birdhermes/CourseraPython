n = float(input())
m = float(input())

def ReduceFraction(a, b):
    if a % b == 0:
        return n // b, m // b
    else:
        ReduceFraction(b, a % b)
p, q = ReduceFraction(n, m)
print(p, q)
