"""Напишите функцию-генератор для получения n первых простых чисел."""


def simple_number_generator(amount):
    n = amount * 10
    num = []
    r = range(1, n+1)
    for i in range(1, n):
        for j in range(i, n):
            a = i+j+2*i*j
            if a <= n and a not in num:
                num.append(a)
    m = set(num).symmetric_difference(set(r))
    l1 = list(m)
    for v in range(amount):
        yield 2*l1[v] + 1


def _simple_number_generator(n):
    num = []
    r = range(1, n+1)
    for i in range(1, n):
        for j in range(i, n):
            a = i + j + 2 * i * j
            if a <= n and a not in num:
                num.append(a)
    m = set(num).symmetric_difference(set(r))
    l1 = list(m)
    for v in l1:
        yield 2 * v + 1


if __name__ == '__main__':
    h = simple_number_generator(5)
    for b in h:
        print(b)
    print(40 * '~')
    lk = _simple_number_generator(10)
    for b in lk:
        print(b)
