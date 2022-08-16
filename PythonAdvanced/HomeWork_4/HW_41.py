import sqlite3
import datetime
from prettytable import PrettyTable

flag = False
db = sqlite3.connect('test.sqlite3')


def create_table():
    try:
        c = db.cursor()
        print("База данных подключена к SQLite")
        c.execute('''CREATE TABLE IF NOT EXISTS bank (
        id INTEGER AUTO_INCREMENT PRIMARY KEY,
        Назначение TEXT,
        Сумма REAL,
        Дата и Время DATETIME
        
        )''')
        db.commit()
        # print("Таблица SQLite создана")

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    # finally:
    #     if (db):
    #         db.close()
    #         print("Соединение с SQLite закрыто\n")


def add_record():
    print("\nAdding...")
    db = sqlite3.connect('test.sqlite3')
    c = db.cursor()
    id = c.execute(f"SELECT max(id) FROM bank ORDER BY id DESC LIMIT 1").fetchone()[0]
    if id == None:
        id = 1
    else:
        id = id + 1
    try:
        purpose = input("Назначение: ")
        s = input("Сумма(UAH): ")
        if flag == True:
            sum = format(float(s), '.2f')
        else:
            sum = format(-float(s), '.2f')

        x = input('Введите дату и время в формате "Год, месяц, число, часы, минуты, секунды" \n'
                  'Например: " 2022, 01, 10, 7, 15, 37 " для "10 Января 2022 07:15:37" \n-> ')
        year, month, day, hour, minute, second = map(int, x.split(','))
        t = datetime.datetime(year, month, day, hour, minute, second)
        # print(t.strftime("%d %B %Y %H:%M:%S"))
        c.execute(f'INSERT INTO bank VALUES ({id}, "{purpose}", {sum}, "{t}"'
                  f')')
        db.commit()
        print("Added!".center(20, "_"), "\n")
    except ValueError or KeyboardInterrupt:
        print('Получены некорректные данные!')


def inc_money():
    global flag
    flag = True
    add_record()
    flag = False


def view_records():
    def view_cycle(sqlite_list):
        my_table = PrettyTable()
        my_table.field_names = ["id", "Назначение", "Сумма", "Date and Time"]
        total_income = 0.00
        total_expense = 0.00

        for operation in sqlite_list:
            if operation[2] > 0:
                total_income = total_income + operation[2]
                aop = [f'\033[32m{el}\033[0m' for el in operation]
                my_table.add_row(aop)
            elif operation[2] <= 0:
                total_expense = total_expense + operation[2]
                aop = [f'\033[31m{el}\033[0m' for el in operation]
                my_table.add_row(aop)

        total = total_income + total_expense
        total = '\033[34m'+str(total)+'\033[0m'
        my_table.add_row([' ', 'Суммарный доход', total_income, ' '])
        my_table.add_row([' ', 'Суммарные расходы', total_expense, ' '])
        my_table.add_row([' ', '\033[34mВсего\033[0m', total, ' '])
        print(my_table)
        print()

    print('\nВведите "m" или "a" чтоб увидеть расходы за месяц или за все время:')
    choose_view = input('>')
    if choose_view == "m":
        print("\nВведите год и месяц в формате YYYY-mm: ")
        datex = input('> ')
        try:
            datex = '"' + str(datex) + '%"'
            # print(datex)
            month_view = db.execute(f'SELECT * FROM bank WHERE Время LIKE {datex}').fetchall()
            view_cycle(month_view)
        except sqlite3.Error as error:
            print("Ошибка при подключении к sqlite", error)
        except ValueError or KeyboardInterrupt:
            print("Вы выбрали некорректное значение...")
    elif choose_view == "a":
        all_view = db.execute(f'SELECT * FROM bank').fetchall()
        view_cycle(all_view)
    else:
        print("Вы выбрали некорректное значение... Попробуйте еще")
        view_records()


def main():
    create_table()
    print('In this program you can control your finance. This code using sqlite3 database. You can use function: \n'
          'add - for add your expense operation; \ninc - for add your income operation; \n'
          'view - for see completed operations per moth or day; \nclose - simple, will closing a code.\n')

    dict_operations = {
        'add': add_record,
        'inc': inc_money,
        'view': view_records
    }

    def initial():
        print('Доступные операции: \n add\n inc\n view\n close')
        try:
            dict_operations[input("> ")]()
            initial()
        except KeyError:
            print('Завершение работы...')
            pass

    initial()
    db.close()


if __name__ == "__main__":
    main()


