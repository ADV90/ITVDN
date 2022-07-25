"""Создайте программу, которая рисует на экране прямоугольник из звёздочек заданной пользователем ширины и высоты."""

a = int(input('Enter side a size: '))
b = int(input('Enter side b size: '))
for i in range(a):
    for j in range(b):
        print(' * ', end='')
    print()
