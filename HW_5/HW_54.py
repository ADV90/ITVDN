import statistics
n = 3
l1 = []

def f_mean(l1):
    print('%.2f' % statistics.mean(l1))

for i in range(n):
    i = input('Enter number: ')
    try:
        int(i)
        i = int(i)
    except ValueError:
        try:
            float(i)
            i = float(i)
        except ValueError:
            print('Error')
    l1.append(i)

f_mean(l1)
