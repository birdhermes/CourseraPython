# Выведите все четные элементы списка.
# Формат ввода
# Вводится список чисел. Все числа списка находятся на одной строке.
# Формат вывода
# Выведите ответ на задачу.

intList = list(map(int, input().split()))

for i in intList:
    if i % 2 == 0:
        print(i, end=' ')
