"""Создайте модуль для получения простых чисел. Импортируйте его из другого модуля. Импортируйте отдельные его имена."""

def simple(n):
    try:
        lst = []
        for i in range(2, n+1):
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                lst.append(i)
        return lst
    except TypeError:
        return None
