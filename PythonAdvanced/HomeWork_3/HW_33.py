"""Поработайте с созданием собственных диалектов, произвольно выбирая правила для CSV файлов. Зарегистрируйте созданные
диалекты и поработайте, используя их, с созданием/чтением файлом.
"""

import csv
from functools import reduce

header = ['Марка', 'Модель', 'Цена']
a = []


class CustomDialect(csv.Dialect):
    quoting = csv.QUOTE_ALL
    quotechar = '"'
    delimiter = "|"
    lineterminator = '\n'


# регистрация диалекта, чтобы он был доступен во время создания reader/writer.
csv.register_dialect('tester', CustomDialect)


def action():
    while True:
        try:
            x = input('Что вы желаете сделать? add/del/clear/exit: ')
            if x.casefold() == 'exit':
                break
            if x.casefold() == 'add':
                add()
            elif x.casefold() == 'clear':
                results = yes_no_dialog('Вы действительно желаете очистить список')
                # print(results)
                if results == 1:
                    clear()
                else:
                    print('Очистка списка отменена!')
            elif x.casefold() == 'del':
                delete()
            else:
                print('Неверно указано действие')
        except ValueError or KeyboardInterrupt:
            print('Неверно указано действие')
    print('Выполнение операции окончено!')


def yes_no_dialog(question, default_answer="yes"):
    answers = {"yes": 1, "y": 1, "ye": 1, "no": 0, "n": 0}
    if default_answer == None:
        tip = " [y/n] "
    elif default_answer == "yes":
        tip = " [Y/n] "
    elif default_answer == "no":
        tip = " [y/N] "
    else:
        raise ValueError(f'Неверное значение: {default_answer = }')
    while True:
        print(question + tip + ": ", end="")
        user_answer = input().casefold()
        if default_answer is not None and user_answer == '':
            return answers[default_answer]
        elif user_answer in answers:
            return answers[user_answer]
        else:
            print("Пожалуйста, введите yes/y или no/n\n")


def add():
    if row_count > 1:
        with open('HW_33.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f, dialect='tester')
            idn = []
            for row in reader:
                idn.append(row[0])
            idn = [int(x) if x.isdigit() else x for x in idn]
            idn = list(filter(lambda x: type(x) is int, idn))
            idn = max(idn) + 1
            print('id авто после добавления в базу: ', idn)
    else:
        idn = row_count
        print('id авто после добавления в базу: ', idn)
    with open('HW_33.csv', 'a', newline='', encoding='utf-8') as f:
        a.append(idn)
        for i in header:
            try:
                i = input(f'Введите {i} авто: ')
                a.append(i)
            except ValueError or KeyboardInterrupt:
                print('Ошибка добавления авто')
        # print(a)
        writer = csv.writer(f, dialect='tester')
        writer.writerow(a)
        a.clear()
        f.close()
        show()


def delete():
    try:
        if row_count > 1:
            x = int(input('Выберите id авто которое вы хотите удалить: '))
            with open('HW_33.csv', 'r', encoding='utf-8') as f:
                reader = csv.reader(f, dialect='tester')
                c = 0
                for row in reader:
                    # print(row[0])
                    c += 1
                    if str(x) == row[0]:
                        # print(row)
                        # print('c=', c)
                        if 1 < c <= row_count:
                            with open('HW_33.csv', 'r+', encoding='utf-8') as f:
                                for i in range(c):
                                    pos = f.tell()
                                    f.readline()
                                rest = f.read()
                                f.seek(pos)
                                f.truncate()
                                f.write(rest)
                                f.close()

                else:
                    print('Неверно указан id авто или из списка были удалены все авто')
        else:
            print('Нет авто для удаления')
    except ValueError or KeyboardInterrupt:
        print('Ошибка удаления авто!')
    finally:
        show()


def clear():
    with open('HW_33.csv', 'w', encoding='utf-8') as f:
        writer = csv.writer(f, dialect='tester')
        id = ['id']
        writer.writerow(id + header)

    show()


def show():
    global row_count
    with open('HW_33.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f, dialect='tester')
        row_count = sum(1 for row in reader)
        # print('Line nums', row_count)
        if row_count > 1:
            with open('HW_33.csv', 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f, dialect='tester')
                for row in reader:
                    print(row)
            print()

        elif row_count == 1:
            with open('HW_33.csv', 'r', encoding='utf-8') as f:
                reader = csv.reader(f, dialect='tester')
                for row in reader:
                    print(row)
            print()
        else:
            print('Ошибка доступа к файлу или файл не существует')
        f.close()


if __name__ == '__main__':
    with open('HW_33.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        row_count = sum(1 for row in reader)
        print('В таблице содержится ', row_count, ' строк')
        if row_count == 0:
            clear()
            action()
        else:
            show()
            action()

        f.close()
