colS = int(input()) #количество селений (1 <= n <= 100000)
linS = int(input()) # i-е из этих чисел задает расстояние от начала дороги до i-го селения
#colB = int(input()) #количество бомбоубежищ (1 <= m <= 100000)
#linB = int(input()) # i-е из этих чисел задает расстояние от начала дороги до i-го бомбоубежища.

l = []
for i in range(colS):
    l.append(input())
print(' '.join(sorted(l, key=linS)))