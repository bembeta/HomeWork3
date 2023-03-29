# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5
import random

n = int(input("Введите кол-во элементов списка: "))
list = []

for i in range(n):
    list.append(random.randint(0, 20))

x = int(input("Введите искомое число: "))

temp = list[0]

difference = abs(x - list[0])

for i in range(n):
    if (abs(x - list[i])) < difference:
        difference = abs(x - list[i])
        temp = list[i]
print(list)
print(f"->{temp}")