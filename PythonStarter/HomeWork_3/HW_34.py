"""Напишите программу-калькулятор, в которой пользователь сможет ввести выбрать операцию, ввести необходимые числа и
получить результат. Операции, которые необходимо реализовать: сложение, вычитание, умножение, деление, возведение в
степень, синус, косинус и тангенс числа.
"""

import math
print('Choose what do you want to do', '\n', '+   -   *   /   x\u207f', '\n', 'sin   cos   tan')
oper = input(': ')
if oper in ('+', '-', '*', '/'):
    a = float(input('Enter a number a = '))
    b = float(input('Enter a number b = '))
    if oper == '+':
        print('a', oper, 'b = %.2f' % (a + b))
    elif oper == '-':
        print('a', oper, 'b = %.2f' % (a - b))
    elif oper == '*':
        print('a', oper, 'b = %.2f' % (a * b))
    elif oper == '/':
        if b != 0:
            print('a', oper, 'b = %.2f' % (a / b))
        else:
            print("Division by zero!")
elif oper in ('sin', 'cos', 'tan'):
    a = float(input('Enter a number a = '))
    if oper == 'sin':
        print(oper, 'a = %.2f' % math.sin(a))
    elif oper == 'cos':
        print(oper, 'a = %.2f' % math.cos(a))
    else:
        print(oper, 'a = %.2f' % math.tan(a))
elif oper.isdigit():
    a = float(input('Enter a number a = '))
    print(a, 'to the', oper, 'th = ', a ** float(oper))

else:
    print("Error!")
