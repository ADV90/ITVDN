"""Создайте программу, которая состоит из функции, которая принимает три числа и возвращает их среднее арифметическое,
и главного цикла, спрашивающего у пользователя числа и вычисляющего их средние значения при помощи созданной функции.
"""

import statistics
n = 3
l1 = []


def f_mean(l1):
    print('%.2f' % statistics.mean(l1))


for i in range(n):
    x = input('Enter number: ')
    try:
        int(x)
        x = int(x)
    except ValueError:
        try:
            float(x)
            x = float(x)
        except ValueError:
            print('Error')
    l1.append(x)

f_mean(l1)
