import collections
numbers = []
sumlen = 0
maxlen = 0
#i = True

#while i:
#    i = str(input())
 #   if i != '': numbers.append(i)

for j in numbers:
    if j > 0:
        sumlen += 1
        maxlen = max(sumlen, maxlen)
    else:
        sumlen = 0
print(sumlen)


#for j in J:
#    if j not in newJ: newJ.append(j)
#for s in S:
#    if s in newJ:
#        sumcnt += 1