"""Простым называется число, которое делится нацело только на единицу и само себя. Число 1 не считается простым.
Напишите программу, которая находит все простые числа в заданном промежутке, выводит их на экран, а затем по требованию
пользователя выводит их сумму либо произведение.
"""


def prnum(a, b):
    prime = [True] * (b + 1)
    res = set()
    if a < 3:
        res = {2}
    for j in range(4, b + 1, 2):
        prime[j] = False
    for i in range(3, b + 1, 2):
        if not prime[i]:
            continue
        if i >= a:
            res.add(i)
        for j in range(i * i, b + 1, i):
            prime[j] = False
    return sorted(list(res))


print(prnum(int(input('Enter start of range: ')), int(input('Enter end of range: '))))
