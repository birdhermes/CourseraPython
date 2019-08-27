num = int(input())
maxi = num
i = 0

while num != 0:

    if num >= maxi:
        if num > maxi:
            maxi = num
            i = 1
        elif num == maxi:
            maxi = num
            i += 1
        maxi = num
    num = int(input())
print(i)
