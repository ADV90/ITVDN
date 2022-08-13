"""Создайте XML файл с вложенными элементами и воспользуйтесь языком поиска XPATH. Попробуйте осуществить поиск
содержимого по созданному документу XML, усложняя свои запросы и добавляя новые элементы, если потребуется.
"""

from xml.etree import ElementTree as ET
from xml.dom import minidom

data = [
    {'Brand': 'Ferrari', 'Model': 'SF90', 'Price': 930000},
    {'Brand': 'Brabus', 'Model': 'G800', 'Price': 530000},
    {'Brand': 'KIA', 'Model': 'K8', 'Price': 63000},
    {'Brand': 'Mercedes', 'Model': 'S63 AMG Coupe', 'Price': 320000},
    {'Brand': 'Audi', 'Model': 'Q8', 'Price': 93000},
    {'Brand': 'Hyundai', 'Model': 'Staria', 'Price': 89000},
    {'Brand': 'Maserati', 'Model': 'Levante', 'Price': 74700}
]

root = ET.Element('cars')

idn = 0
for item in data:
    idn += 1
    record = ET.SubElement(root, 'car', id=str(idn))
    for key, value in item.items():
        e = ET.SubElement(record, key)
        e.text = str(value)

tree = ET.tostring(root).decode()

xml_prettyxml = minidom.parseString(tree).toprettyxml()
with open('HW_32.xml', 'w', encoding='utf-8') as xml_file:
    xml_file.write(xml_prettyxml)

tree = ET.parse('HW_32.xml')
root = tree.getroot()

try:
    fid = int(input('Введите id авто для получения информации: '))
    st = './car[@id="' + str(fid)

    brand = root.findall(st + '"]/Brand')
    model = root.findall(st + '"]/Model')
    price = root.findall(st + '"]/Price')
    # print(len(brand) + len(model) + len(price))
    if len(brand) or len(model) or len(price) >= 1:
        for values in zip(brand, model, price):
            row = {value.tag: value.text for value in values}
            print(row)

    else:
        print('Авто с таким id не существует')

except ValueError:
    print('Вы ввели неверное значение')

