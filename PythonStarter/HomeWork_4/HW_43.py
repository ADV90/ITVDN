# for i in range(int(input('x= ')) + 1):
#     print('* ' * i)


a = int(input('Enter side a size: '))

for i in range(1, a + 1):
    print('* ' * i, end ='')
    for j in range(1, a):
        print(' ', end ='')
    print()

