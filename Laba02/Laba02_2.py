# Задание 2. Задачи на многомерные списки
# Выберете одну из задач:
# 2.	Симметричная матрица.
# Дана квадратная матрица. Проверить, является ли она симметричной относительно главной диагонали.

import numpy
import random

print("Введите размер матрицы ")
n=int(input())

A = numpy.array([[random.randint(0, 1) for j in range(n)] for i in range(n)])

flag = True
for i in range(n):
    for j in range(n):
        if A[i][j] != A[j][i]:
            flag = False
            break

print(A)
if flag:
    print("Матрица симмметрична")
else:
    print("Матрица НЕ симмметрична")
