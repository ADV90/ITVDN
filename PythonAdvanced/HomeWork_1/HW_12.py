"""Создайте список целых чисел. Получите список квадратов нечётных чисел из этого списка."""

import random

numbers = [random.randint(1, 100) for n in range(0, 100)]
print(numbers)
print()
# print(len(numbers))
# print()
filtered = filter(lambda x: x % 2 != 0, numbers)
nfn = list(filtered)
# print(nfn)
# print()
num_sq = map(lambda y: y**2, nfn)
ns = list(num_sq)
print(ns)

