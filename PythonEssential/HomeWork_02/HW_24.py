"""Создайте иерархию классов транспортных средств. В общем классе опишите общие для всех транспортных средств поля, в
наследниках – специфичные для них. Создайте несколько экземпляров. Выведите информацию о каждом транспортном средстве.
"""


class Transport:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color


class Helicopter(Transport):
    def __init__(self, brand, model, color, range, time_in_flight, max_height, service_life):
        self.range = range
        self.time_in_flight = time_in_flight
        self.max_height = max_height
        self.service_life = service_life
        Transport.__init__(self, brand, model, color)

    def h_info(self):
        print("{} {} in {} color has {} km range or {} hours maximum flight time on {} ft maximum operating altitude. "
              "Overhaul resource - {} hours.".format(self.brand, self.model, self.color, self.range,
                                                     self.time_in_flight, self.max_height, self.service_life))


class Car(Transport):
    def __init__(self, brand, model, color, type, fuel, power):
        self.type = type
        self.fuel = fuel
        self.power = power
        Transport.__init__(self, brand, model, color)

    def c_info(self):
        print("{} {} in {} color it's a {} with {} hp {} engine.".format(self.brand, self.model, self.color, self.type,
                                                                         self.power, self.fuel))


helicopter = Helicopter('Robinson', 'R44', 'white', 555, 3, 14000, 2200)
helicopter.h_info()
car = Car('Ferrari', 'SF90 Spider', 'Giallo Montecarlo', 'hypercar', 'hybrid', 1000)
car.c_info()
