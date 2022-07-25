"""Опишите свой класс исключения. Напишите функцию, которая будет выбрасывать данное исключение, если пользователь
введёт определённое значение, и перехватите это исключение при вызове функции.
"""


class MyError(Exception):
    def __init__(self, text):
        self.text = text


a = input("Input positive integer: ")

try:
    a = int(a)
    if a < 0:
        raise MyError("You give negative!")
except ValueError:
    print("Error type of value!")
except MyError as mr:
    print(mr)
else:
    print(a)
