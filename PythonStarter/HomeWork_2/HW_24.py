"""Напишите программу, которая запрашивает у пользователя радиус круга и выводит его площадь.
Формула площади круга S = πr^2
"""

from math import pi

r = int(input('Enter a radius "r": '))
s = round(pi, 2) * r**2
print('Area of a circle "S = \u03c0 * r\u00b2" = ', s)

input('Press any key')
