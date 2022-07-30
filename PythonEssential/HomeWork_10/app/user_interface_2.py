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
