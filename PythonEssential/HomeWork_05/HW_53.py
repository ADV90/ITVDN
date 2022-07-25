"""Напишите итератор, который возвращает элементы заданного списка в обратном порядке (аналог reversed)."""


class ReversedList:
    def __init__(self, list_to_reverse):
        self.list_to_reverse = list_to_reverse
        self.last_element = len(list_to_reverse) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.last_element < 0:
            raise StopIteration
        element = self.list_to_reverse[self.last_element]
        self.last_element -= 1
        return element


if __name__ == '__main__':
    b = range(10, 100, 5)
    a = ReversedList(b)
    c = iter(a)
    for u in c:
        print(u)
