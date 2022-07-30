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
