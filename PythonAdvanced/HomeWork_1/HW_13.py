"""Создайте функцию-генератор чисел Фибоначчи. Примените к ней декоратор, который будет оставлять в последовательности
только чётные числа.
"""


def even_numbers(func):
    def new_seq(*args):
        seq = func(*args)
        return filter(lambda x: x % 2 == 0, seq)
    return new_seq


@even_numbers
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
        yield b


print(list(fibonacci(20)))
