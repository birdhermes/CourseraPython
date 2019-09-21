a = int(input())
b = int(input())

if a < b:
    list1 = list(range(a, b + 1))
    for i in list1:
        print(list1)
elif a > b:
    list2 = list(range(a, b - 1, -1))
    for i in list2:
        print(list2)
elif a == b:
    print(a)
