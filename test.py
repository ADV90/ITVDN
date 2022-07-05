# class Car:
#     def __init__(
#             self,
#             color,
#             brand,
#             model,
#             v,
#             type_of_car
#     ):
#         self.color = color
#         self.brand = brand
#         self.model = model
#         self.__v = v
#         self.__type_of_car = type_of_car
#
#     def get(self):
#         return self.color
#
#     def set(self, new_color):
#         self.color = new_color
#
#
# car1 = Car(
#     'blue',
#     'Mercedes',
#     'S-class',
#     'v8',
#     'sedan'
# )
#
# print(car1.get())
# car1.set('green')
# print(car1.get())

import base64
import hashlib
password = 'maks123456'
h = hashlib.sha256(password.encode())
print(base64.b64encode(h.digest()))