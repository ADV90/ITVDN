"""Напишите программу, которая вводит с клавиатуры последовательность чисел и выводит её отсортированной в порядке
возрастания.
"""

l1 = []
n = 3
x = None

if __name__ == '__main__':
    for i in range(0, n):
        try:
            x = int(input('Введите число: '))
        except ValueError:
            print('Ошибка ввода. ')

        l1.append(x)

    y = sorted(l1)
    print(y)
