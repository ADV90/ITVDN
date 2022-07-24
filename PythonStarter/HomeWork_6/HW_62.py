word = input('Введите слово: ').casefold()
if word == word[::-1]:
    print('Является палиндромом')
else:
    print('Не является палиндромом')
