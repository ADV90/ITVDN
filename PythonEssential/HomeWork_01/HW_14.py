class Car:
    def __init__(self, brand, model, year, color, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.price = price


class Saloon:
    def __init__(self, cars):
        self.cars = cars

        self.show()

    def show(self):
        global flag

        flag = False

        for car in self.cars:
            print(f"{self.cars.index(car) + 1}. {car.brand} {car.model} {car.year} in {car.color} color have price "
                  f"{car.price} USD")
            flag = True

    def sell(self, quantity):
        car = self.cars[quantity - 1]

        print(f"The car {car.brand} {car.model} was sold!")

        del self.cars[quantity - 1]


car1 = Car('Ferrari', 'SF90 Spider', 2022, 'Rosso Scuderia', 1020000)
car2 = Car('Brabus', 'G900 Rocket', 2021, 'Black', 970000)
car3 = Car('Maserati', 'MC20', 2021, 'Blue', 291000)
car4 = Car('KIA', 'K8', 2022, 'Green', 52000)
car5 = Car('Genesis', 'G90', 2022, 'Beige', 97000)

flag = True

salon = Saloon([car1, car2, car3, car4, car5])

while(flag):
    try:
        buy = int(input('\nWhich car number do you want to buy?: '))
        salon.sell(buy)
    except:
        print('Chose correct number')
    finally:
        salon.show()
