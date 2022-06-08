import os

from os.path import getsize, join, basename, splitext
path = input('Enter path to dir: ')
c_file = input('Enter output file name:')
c_file = splitext(c_file)[0]+".txt"

with open(c_file, 'w', encoding='utf-8') as file:
    for root, dirs, files in os.walk(path):
        total_size = sum(getsize(join(root, name)) / 1024 / 1024 / 1024 for name in files)
        catalog = basename(root)
        spoiler = str('[spoiler="') + catalog + ' // ' '%.2f' % total_size + 'Gb' + str('"]')
        print(spoiler)
        print('  ')
        file.writelines(f'{spoiler}\n')
        for filename in files:
            fname = splitext(filename)[0]
            print(fname)
            file.writelines(f'{fname}\n')
        endspoiler = str('[/spoiler]')
        print(endspoiler)
        print('  ')
        file.writelines(f'{endspoiler} \n')
        # file.writelines(f' \n')

print('Список файлов смотрим здесь - ', c_file)
