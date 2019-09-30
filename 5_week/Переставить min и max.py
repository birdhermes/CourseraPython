# В списке все элементы попарно различны. Поменяйте местами минимальный и максимальный элемент этого списка.
# Формат ввода
# Вводится список целых чисел. Все числа списка находятся на одной строке.
# Формат вывода
# Выведите ответ на задачу

intList = list(map(int, input().split()))

kk = intList.index(min(intList))
mm = intList.index(max(intList))
intList[kk], intList[mm] = intList[mm], intList[kk]
for i in intList:
    print(i, end=' ')
