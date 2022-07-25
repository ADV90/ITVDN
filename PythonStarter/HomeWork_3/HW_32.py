"""Напишите программу, которая вычисляет значение функции в диапазоне значений x от -10 до 10 включительно с шагом,
равным 1. y = x^2 при -5 <= x <= 5; y = 2*|x|-1 при x < -5; y = 2x при x > 5. Вычисление значения функции оформить в
виде программной функции, которая принимает значение x, а возвращает полученное значение функции (y).
"""

x = int(input('Pick a number between -10 and 10: '))
if -5 <= x <= 5:
    y = x ** 2
    c = 'y = x\u00b2 = '
elif -5 > x >= -10:
    y = 2 * abs(x) - 1
    c = 'y = 2 * |x| - 1 = '
elif 5 < x <= 10:
    y = 2 * x
    c = 'y = 2 * x = '
else:
    y = 'Error. Picked number must be placed between -10 and 10'

print(c, y)
