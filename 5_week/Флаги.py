import sys

n = int(input())
m = 0
a = "+___ \n" +\
      "|" + str(m) +" / \n" +\
      "|__\ \n"+ \
      "|"

for i in range(n):
    for j in a:
        a += 1
        m += 1
        print(a[j], sep = ' ', end= '')
