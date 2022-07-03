from math import sqrt

a = int(input('Enter a number "a": '))
b = int(input('Enter a number "b": '))
c = int(input('Enter a number "c": '))
print('a*x\u00b2 + b*x + c = 0')
d = b**2 - 4 * a * c

# math.sqrt
if d > 0:
    print('Discriminant D =', str(d))
    print('x\u2081 = (-b + \u221a(b\u00b2 - 4*a*c) ) / (2*a) =', (-b + sqrt(d)) / (2 * a))
    print('x\u2082 = (-b - \u221a(b\u00b2 - 4*a*c) ) / (2*a) =', (-b - sqrt(d)) / (2 * a))
elif d == 0:
    print('Discriminant D =', str(d))
    print('x\u2081 = x\u2082 = -b / (2*a) =', -b / (2 * a))
else:
    print('Discriminant D =', str(d), '< 0. The equation has no solution in real numbers')

input('Press any key')
