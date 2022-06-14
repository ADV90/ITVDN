def fib(n):
    if n==1 or n==2 or n==3:
        return n
    return fib(n-1) + fib(n-2)

n = int(input('Введите ступеньку: '))
print(fib(n))
