"""Даны числа a и b (a < b). Выведите сумму всех натуральных чисел от a до b (включительно)."""

a = 1
b = 4
x = 0
while a <= b:
    x += a
    a += 1

print(x)
