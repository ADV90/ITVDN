def function(a, b):
    if b == a:
        return b
    return b + function(a, b - 1)


n1 = int(input('Number 1: '))
n2 = int(input('Number 2: '))
if n1 < n2:
    a = n1
    b = n2
else:
    a = n2
    b = n1

print(function(a, b))
