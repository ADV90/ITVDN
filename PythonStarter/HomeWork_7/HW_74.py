"""Создайте список, введите количество его элементов и сами значения, выведите эти значения на экран в обратном
порядке.
"""

l1 = []
n = int(input('Enter the number of entries in the list: '))

for i in range(0, n):
    x = input(f'Enter entries #{i+1}: ')
    l1.append(x)

print(l1[::-1])
