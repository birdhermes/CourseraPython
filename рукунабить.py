<<<<<<< HEAD
a = list(map(int, input().split()))
b = []
i = 0
for now in a:
    if now % 2 == 0:
        b.append(now)
print(*b)
=======
<<<<<<< HEAD
for i in range(1, 11):
    for j in range(1,11):
        print(i*j, end=' ')
    print()
=======
def rec():
    n = int(input())
    if n != 0:
        rec()
        print(n)
rec()
>>>>>>> 5ba6489d1712144f6befbf6488084323521f5012
>>>>>>> 93fdf581b07c285a1c0d9cbc39723710c9eae186
