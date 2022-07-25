"""Создайте класс, описывающий автомобиль. Какие атрибуты и методы должны быть полностью инкапсулированы? Доступ к
таким атрибутам и изменение данных реализуйте через специальные методы (get, set).
"""


class Car:
    def __init__(self, brand, model, engine):
        self.brand = brand
        self.model = model
        self.__engine = engine

    @property
    def engine(self):
        return self.__engine

    @engine.setter
    def engine(self, value):
        self.__engine = value


car = Car('KIA', 'K8', 'V6')
print(car.engine)
car.engine = 'LPI'
print(car.engine)
