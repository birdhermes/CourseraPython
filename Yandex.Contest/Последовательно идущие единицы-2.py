def numones(numbers):
    sumlen = 0
    maxlen = 0
    for j in numbers:
        if j > 0:
            sumlen += 1
            maxlen = max(maxlen, sumlen)
        else:
            sumlen = 0
    return maxlen
