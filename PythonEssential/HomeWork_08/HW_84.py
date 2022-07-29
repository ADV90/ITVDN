dictionary = {'one': 1, 'two': 2, 'three': 3, 'ten': 10}


def kwh(**kwargs):
    for key in kwargs:
        print('Key = {0}, value = {1}'.format(key, kwargs[key]))


if __name__ == '__main__':
    kwh(**dictionary)
    kwh(twenty=20, seven=7)
