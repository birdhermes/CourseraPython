numbers = []
sumlen = 0
maxlen = 0
i = True

while i:
    i = input()
    if i != '':
        numbers.append(i)

#def numones(numbers):
    for n in numbers:
        if n > 0:
            sumlen += 1
            maxlen = max(sumlen, maxlen)
        else:
            sumlen = 0
    return(maxlen)
#        if sumlen > maxlen:
#           maxlen = sumlen
print(maxlen)