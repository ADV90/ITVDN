"""Создайте список товаров в интернет-магазине. Сериализуйте его при помощи pickle и сохраните в JSON."""

import json
import pickle

try:
    products = pickle.load(open('products.p', 'rb'))
except (EOFError, IOError):
    print('Can not open pickled file or file does not exist. Create new product list')
    products = []


def add_product(_name, _code, _description):
    product = dict(name=_name, code=_code, description=_description)
    products.append(product)


def print_products():
    print('-'*10 + 'Products' + '-'*10)
    for product in products:
        print(product['name'] + ' - ' + product['code'] + ' - ' + product['description'])
    print('-'*28)


def save():
    pickle.dump(products, open('products.p', 'w'))
    json.dump(products, open('products.json', 'w', encoding="utf8"))


def on_exit():
    choice = input('Do you want to save changes? (Y/N)\n>>').lower()
    if choice == 'y':
        save()
    else:
        pass


if __name__ == '__main__':
    while True:
        variant = input('1.Add new product''\n'
                        '2.Save''\n'
                        '3.Print products''\n'
                        '4.Exit''\n'
                        '>> ')
        if variant == '1':
            try:
                name = input('name: ')
                code = input('code: ')
                desc = input('description: ')
                add_product(name, code, desc)
            except Exception as e:
                print('Error occurred' + e)
        if variant == '2':
            save()
        if variant == '3':
            print_products()
        if variant == '4':
            on_exit()
            break
