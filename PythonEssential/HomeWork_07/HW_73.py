"""Напишите программу, которая вводит с клавиатуры текст и выводит отсортированные по алфавиту слова данного текста."""

import string


def sort(text):
    text = text.casefold()
    text = text.translate({ord(i): None for i in string.punctuation})
    # print(text)
    text = text.split()
    text.sort()
    print(text)


text = input('Введите ваш текст: ')
sorted(text)
