l1 = []
n1 = int(input('Number 1: '))
n2 = int(input('Number 2: '))

if n1 <= n2:
    while n1 <= n2:
        l1.append(n1)
        n1 += 1
else:
    while n2 <= n1:
        l1.append(n2)
        n2 += 1

print(sum(l1))
