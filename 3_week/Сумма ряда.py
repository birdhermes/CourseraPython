n = int(input())
i = 0
result = 0
while i != n:
    i += 1
    result += (1 / i**2)
print('{0:.10}'.format(result))
