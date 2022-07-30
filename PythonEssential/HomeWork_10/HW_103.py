import mod
from numbers import *


def main():
    print(" -- number1 from numbers.py -- ")
    result = mod.simple(number1)
    print(*result)
    print(" -- number2 from numbers.py -- ")
    result = mod.simple(number2)
    print(*result)
    print(" -- number3 from numbers.py -- ")
    result = mod.simple(number3)
    print(*result)
    print(" -- number4 from numbers.py -- ")
    result = mod.simple(number4)
    print(*result)


if __name__ == "__main__":
    main()
