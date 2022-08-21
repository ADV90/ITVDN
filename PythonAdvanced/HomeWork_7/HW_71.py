"""Создать функцию, которая принимает список из элементов типа int, а возвращает новый список из строковых значений
исходного массива. Добавить аннотацию типов для входных и результирующих значений функции.
"""

from typing import List


def its(some_value: List[int]) -> List[str]:
    res = []
    for i in some_value:
        elem = str(i)
        res.append(elem)
    return res


print(its([1, 2, 3]))
print(its([1, 3, 'test']))
