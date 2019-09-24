# Найдите наибольшее значение в списке и индекс последнего элемента, который имеет данное значение за один проход по
# списку, не модифицируя этот список и не используя дополнительного списка. Выведите два значения.

intList = list(map(int, input().split()))
value, ind = 0, 0

for i in range(len(intList)):
    if intList[i] == max(intList):
        value, ind = intList[i], i

print(value, ind)
