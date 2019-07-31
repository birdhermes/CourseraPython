num = int(input())
i = 0
step = 0
while i != num:
    if num < 0:
        continue
    i += 1
    step += i ** 2
print(step)
