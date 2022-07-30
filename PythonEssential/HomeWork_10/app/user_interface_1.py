"""Перепишите домашнее задание предыдущего урока (сервис для сокращения ссылок) таким образом, чтобы у него была
основная часть, которая отвечала бы за логику работы и предоставляла обобщённый интерфейс, и модуль представления,
который отвечал бы за взаимодействие с пользователем. При замене последнего на другой, взаимодействующий с
пользователем иным способом, программа должна продолжать корректно работать.
"""

from PythonEssential.HomeWork_10.app.rh import *


def main():
    ref_handler = ReferenceHandler()

    while True:
        print('1. Add link')
        print('2. Get link')
        print('3. Exit')

        choice = input('> ')
        if choice == '1':
            ref_handler.add_reference()
        elif choice == '2':
            ref_handler.get_reference()
        elif choice == '3':
            break
        else:
            print('Incorrect input')
        print()
