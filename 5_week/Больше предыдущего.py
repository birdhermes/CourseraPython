# Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.
# Формат ввода
# Вводится список чисел. Все числа списка находятся на одной строке.
# Формат вывода
# Выведите ответ на задачу.

a = list(map(int, input().split()))
l = []
for i in range(len(a)):
    i = int(i)
    if a[i] > a[i-1] and i > 0:
        l.append(int(a[i]))
for x in l:
    print(x, end=' ')
