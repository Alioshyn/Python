# Задача на рекурсию
#
# Реализуйте рекурсивную функцию нарезания прямоугольника с заданными пользователем сторонами a и b
# на квадраты с наибольшей возможной на каждом этапе стороной.
# Выведите длины ребер получаемых квадратов и кол-во полученных квадратов.

def squares(a, b):
    if a == b:
        count = 1
        print(f"Квадрат {a} x {a}")
    elif a<b:
        count = squares(a, b-a) + 1
        print(f"Квадрат {a} x {a}")
    else:
        count = squares(a-b, b) + 1
        print(f"Квадрат {b} x {b}")
    return count

a = int(input('Введите длину стороны a прямоугольника: '))
b = int(input('Введите длину стороны b прямоугольника: '))

print(f"В прямоугольник со сторонами {a} x {b} можно вписать квадраты:")
print(f"Всего квадратов: {squares(a, b)}")
