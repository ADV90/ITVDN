"""Напишите скрипт, который создаёт текстовый файл и записывает в него 10000 случайных действительных чисел. Создайте
ещё один скрипт, который читает числа из файла и выводит на экран их сумму.
"""

with open('numbers.txt', 'r') as numbers:
    total = 0
    for n in numbers:
        total += int(n)
    print('Sum of numbers from file {} : {} '.format(numbers.name, total))
