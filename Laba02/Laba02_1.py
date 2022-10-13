# Задание 1. Задачи на одномерные списки
# Вариант 2
# Введите одномерный целочисленный список.
# Найдите наибольший нечетный элемент.
# Найдите минимальный по модулю элемент списка.
import random

print("Введите размер одномерного списка ")
n=int(input())

A = [random.randint(-100, 100) for i in range(n)]
print(A)
minAbs = 100
maxOdd = 0

for i in range(n):
    if abs(A[i]) < abs(minAbs):
        minAbs = abs(A[i])
    if A[i] > maxOdd and A[i] % 2 != 0:
        maxOdd = A[i]

print("Наибольший нечетный элемент - ", maxOdd)
print("Минимальный по модулю элемент списка - ", minAbs)