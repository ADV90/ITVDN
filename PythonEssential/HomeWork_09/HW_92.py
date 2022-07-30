"""Модифицируйте исходный код сервиса по сокращению ссылок из предыдущих двух уроков так, чтобы он сохранял базу
ссылок на диске и не «забывал» при перезапуске. При желании можете ознакомиться с модулем shelve
(https://docs.python.org/3/library/shelve.html), который в данном случае будет весьма удобен и упростит выполнение
задания.
"""

import shelve


class ReferenceHandler:
    def __init__(self):
        self.storage = 'ref'
        d = shelve.open(self.storage)
        # d['init'] = 'initial name'
        d.close()

    def add_reference(self):
        original_ref = input("Enter original reference : ")
        short_ref = None
        storage = shelve.open(self.storage)
        while not short_ref or short_ref in storage:
            s = original_ref

            if "/" in s.split('.')[-1]:
                s1 = '.'.join(s.split('.')[:-1])
                s1 += '/'

                # s2 = ""
                # flag = False
                #
                # for i in s.split('.')[-1]: # com/ADV90/ITVDN -> com/ ->
                #     if i == "/" and not flag:
                #         flag = True
                #     elif flag and i != "/":
                #         s2 += i

                s4 = s.split('.')[-1].split('/')[1:]
                s5 = '.'.join(s4)
                s3 = s5[::2]

                s1 += s3
            else:
                print('You write short or incorrect link')

            print(s1)

            short_ref = s1
            if short_ref in self.storage:
                print('This name already exist \n (url: {})'.format(storage[short_ref]))
        storage[short_ref] = original_ref
        storage.close()

    def get_reference(self):
        name = input('Enter reference name: ')
        storage = shelve.open(self.storage)
        url = storage[name]
        if url:
            print(url)
        else:
            print('Link does not exist')
        storage.close()


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


if __name__ == '__main__':
    main()
