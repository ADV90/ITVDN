"""Создайте простые словари и сконвертируйте их в JSON. Сохраните JSON в файл и попробуйте загрузить данные из файла"""

import json

data = {
    'Cars': [{'id': 1, 'Brand': 'Ferrari', 'Model': 'SF90', 'Price': 930000},
             {'id': 2, 'Brand': 'Brabus', 'Model': 'G800', 'Price': 540000},
             {'id': 3, 'Brand': 'KIA', 'Model': 'K8', 'Price': 65000},
             {'id': 4, 'Brand': 'Mercedes', 'Model': 'S63 AMG', 'Price': 320000},
             {'id': 5, 'Brand': 'Audi', 'Model': 'Q8', 'Price': 93000},
             {'id': 6, 'Brand': 'Hyundai', 'Model': 'Staria', 'Price': 89000},
             {'id': 7, 'Brand': 'Maserati', 'Model': 'Levante', 'Price': 74700}]
}

# конвертация словаря в строку формата JSON
# json_data = json.dumps(data)
# print(json_data)

# конвертация словаря в строку формата JSON и записью данного текста в файл.
with open('HW_31.json', 'w') as f:
    json.dump(data, f, indent=4)

# Чтение и показ цены по запросу
with open('HW_31.json', 'r') as f:
    data = json.load(f)

c = []
for txt in data['Cars']:
    c.append(txt['id'])
    print(txt['id'], '|', txt['Brand'], txt['Model'])

print()

try:
    fid = int(input('Введите id авто для получения цены: '))

    if 0 < fid <= max(c):
        for txt in data['Cars']:
            if txt['id'] == fid:
                print(txt['id'], '|', txt['Brand'], txt['Model'], ':', txt['Price'], '$')
    else:
        print('Неверно указан id авто!')

except ValueError:
    print('Вы ввели неверное значение')
