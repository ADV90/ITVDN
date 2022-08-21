"""Создайте три функции, одна из которых читает файл на диске с заданным именем и проверяет наличие строку “Wow! ”. В
случае, если файла нет, то засыпает на 5 секунд, а затем снова продолжает поиск по файлу. В случае, если файл есть, то
открывает его и ищет строку “Wow!”. При наличии данной строки закрывает файл и генерирует событие, а другая функция
ожидает данное событие и в случае его возникновения выполняет удаление этого файла. В случае если строки «Wow!» не было
найдено в файле, то засыпать на 5 секунд. Создайте файл руками и проверьте выполнение программы.
"""

import threading
import os
import time

params = {"path_to_file": "wow_file.txt"}


def read_file(path_to_file):
    if not os.path.exists(path_to_file):
        print(f"File {path_to_file} is not found")
        time.sleep(5)
        read_file(path_to_file)
    else:
        print(f"File {path_to_file} is found")
        with open(path_to_file, "r") as f:
            wow_str = f.read()
            if wow_str.casefold() == 'wow!':
                print(f"The string 'Wow! ' is found")
                f.close()
                event.set()
            else:
                print(f"The string 'Wow! ' is not found")
                time.sleep(5)
                read_file(path_to_file)


def delete_file(path_to_file):
    event.wait()
    os.remove(path_to_file)
    print("File is deleted")


# def check_file(path_to_file):
#     if not os.path.exists(path_to_file):
#         time.sleep(5)
#         read_file(path_to_file)


event = threading.Event()

task1 = threading.Thread(target=read_file, kwargs=params)
task2 = threading.Thread(target=delete_file, kwargs=params)

task1.start()
task2.start()

task1.join()
task2.join()
