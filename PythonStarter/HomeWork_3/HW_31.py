"""Напишите программу, которая спрашивает у пользователя его имя, и если оно совпадает с вашим,
выдаёт определённое сообщение.
"""

a = ['Dima', 'Dmitry', 'Dmytry', 'Dmitryi', 'Dmitriy', 'Dmytryi', 'Dmytriy', 'Dmytro',  'Dmitro']
b = input('Input your name: ')
if b.casefold() in map(str.casefold, a):
    print('I have the same name...')
else:
    print('Sorry, try again!')

input('Press any key')
