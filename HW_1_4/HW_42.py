x = int(input('Enter number: '))

factorial = 1
while x > 1:
    factorial *= x
    x -= 1

print(factorial)