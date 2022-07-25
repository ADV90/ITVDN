"""Напишите генератор, который возвращает элементы заданного списка в обратном порядке (аналог reversed)."""


def reverse(rlist):
    last = len(rlist) - 1
    while last >= 0:
        element = rlist[last]
        last -= 1
        yield element


if __name__ == '__main__':
    l1 = range(2, 8)
    a = reverse(l1)
    for n in a:
        print(n)
