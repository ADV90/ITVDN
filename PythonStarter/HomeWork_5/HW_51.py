"""Создайте функцию, которая выводит приветствие для пользователя с заданным именем. Если имя не указано, она должна
выводить приветствие для пользователя с Вашим именем.
"""

def hello(name='Dima'):
    print('Hello, ', name, '!', sep='')


hello('Test')
hello()

# def listgen(ame):
#     for i in range(1, 3):
#         nameask = str(input("Name list: "))
#         ame.append(nameask)
#     print(ame)
#     return ame
#
# def simple_Hello():
#     name = input('Enter your name: ')
#     if name in ame:
#         print('Hello,', name + '.')
#     else:
#         print("Hello, Dima")
#
#
# if __name__ == '__main__':
#     ame = []
#     listgen(ame)
#     simple_Hello()
