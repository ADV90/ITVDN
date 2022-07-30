"""Перепишите домашнее задание предыдущего урока (сервис для сокращения ссылок) таким образом, чтобы у него была
основная часть, которая отвечала бы за логику работы и предоставляла обобщённый интерфейс, и модуль представления,
который отвечал бы за взаимодействие с пользователем. При замене последнего на другой, взаимодействующий с
пользователем иным способом, программа должна продолжать корректно работать.
"""

from PythonEssential.HomeWork_10.app.rh import *


def run():
    ref_handler = ReferenceHandler()

    while True:
        print('A. Add link')
        print('G. Get link')
        print('E. Exit')

        choice = input('> ')
        if choice == 'A':
            ref_handler.add_reference()
        elif choice == 'G':
            ref_handler.get_reference()
        elif choice == 'E':
            break
        else:
            print('Incorrect input')
        print()
