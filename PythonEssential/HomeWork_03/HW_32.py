"""Создайте 2 класса – языка, например, английский и испанский. У обоих классов должен быть метод greeting(). Оба
создают разные приветствия. Создайте два соответствующих объекта из двух классов выше и вызовите действия этих двух
объектов в одной функции (функция hello_friend).
"""


class English:
    def greeting(self):
        return 'Hello'


class Espanol:
    def greeting(self):
        return 'Ola!'


friend = English()
amigo = Espanol()


def hello_friend():
    p = friend
    print(p.greeting())
    p = amigo
    print(p.greeting())


hello_friend()
