"""Используя ссылки в конце данного урока, ознакомьтесь с таким средством инкапсуляции как свойства. Ознакомьтесь с
декоратором property в Python. Создайте класс, описывающий температуру и позволяющий задавать и получать температуру
по шкале Цельсия и Фаренгейта, причём данные могут быть заданы в одной шкале, а получены в другой.
"""


class Temperature:
    def __init__(self):
        self.__temp = [0, 0]

    def celsius(self, t):
        self.__temp[0] = t
        self.__temp[1] = t * 9 / 5 + 32

    def farenheit(self, t):
        self.__temp[0] = (t - 32) * 5 / 9
        self.__temp[1] = t

    @property
    def get_celsius(self):
        return self.__temp[0]

    @property
    def get_farenheit(self):
        return self.__temp[1]


t = Temperature()

t.celsius(25)
print(t.get_celsius)
print(t.get_farenheit)

print()

t.farenheit(50)
print(t.get_celsius)
print(t.get_farenheit)
