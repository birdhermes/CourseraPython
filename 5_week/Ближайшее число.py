n = int(input())
listq = list(map(int, input().split()))
num = int(input())
res1, res2 = [], []

for i in range(int(n)):

    for i in listq:
        if i > num:
            res1.append(i)

        else:
           res2.append(i)
print((*min(res1) or *max(res2))
