x = -5
l1 = 0 #Узнаем максимальную ширину ячейки со значением
c = 0
# l21 = []
# l22 = []
h11 = 'Formula'
a11 = 'y1 = x\u00b2 = '
b11 = 'y2 = 2 * x = '
l11 = int(max(len(str(a11)), len(str(b11)), len(str(h11))))
# print(l11)

def gc1(x):
    global l1
    global tc
    tc = 0 #Счетчик количества ячеек со значениями
    while x < 5.1:
        y1 = x ** 2
        y2 = 2 * x
        x += 0.5
        tc += 1
        l12 = max(len(str(y1)), len(str(y2)))
        if l1 < l12:
            l1 = l12
    # print(l1)
    # print(tc)

def func1(x):
    while x < 5.1:
        y1 = x ** 2
        x += 0.5
        pr1 = str(y1)
        print(pr1.center(l1), end=' | ')
        # l21.append(y1)

def func2(x):
    while x < 5.1:
        y2 = 2 * x
        x += 0.5
        pr2 = str(y2)
        print(pr2.center(l1), end=' | ')
        # l22.append(y2)

def r1(l1, l11, x):
    print('+', '-' * l11, '+', ramka * tc, sep='')
    print(h11.center(l11), end=' | ')
    while x < 5.1:
        print(str(x).center(l1), end=' | ')
        x += 0.5
    print()
    print('+', '-' * l11, '+', ramka * tc, sep='')

gc1(x)
ramka = str('-' * (l1+2) + '+')
r1(l1, l11, x)
print(a11.center(l11), end=' | ')
func1(x)
print()
print(b11.center(l11), end=' | ')
func2(x)
print()
print('+', '-' * l11, '+', ramka * tc, sep='')
