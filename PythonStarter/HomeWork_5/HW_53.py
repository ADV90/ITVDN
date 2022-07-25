"""Создайте программу-калькулятор, которая поддерживает четыре операции: сложение, вычитание, умножение, деление. Все
данные должны вводиться в цикле, пока пользователь не укажет, что хочет завершить выполнение программы. Каждая операция
должна быть реализована в виде отдельной функции. Функция деления должна проверять данные на корректность и выдавать
сообщение об ошибке в случае попытки деления на ноль.
"""

import operator
a = None
oper = None
ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}


def calc(a, oper):
    global answer
    try:
        b = input(': ')
        try:
            int(b)
            b = int(b)
        except ValueError:
            try:
                float(b)
                b = float(b)
            except ValueError:
                print('Error')
        if b == 0 and oper == '/':
            print('Division by zero')
            answer = 'Error'
        else:
            answer = ops[oper](a, b)
    except ValueError:
        raise Warning('Error')
    print(answer, ' ', end='')


while oper != '=':
    if a == None:
        a = input(': ')
        try:
            int(a)
            a = int(a)
        except ValueError:
            try:
                float(a)
                a = float(a)
            except ValueError:
                print('Error')
    else:
        a = answer
        if a == 'Error':
            break
    try:
        oper = input('operation: ')
        if oper == '=':
            break
        elif oper == 'c':
            a = None
        elif oper in ('+', '-', '*', '/'):
            calc(a, oper)
        else:
            print('Error, try again')
    except ValueError:
        raise Warning('Error')
