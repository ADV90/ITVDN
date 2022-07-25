# ITVDN / CyberBionic Systematics
____
1. [Python Starter](#PythonStarter)
    - [1. Введение в Python](#11)
    - [2. Переменные и типы данных](#12)
    - [3. Условные конструкции](#13)
    - [4. Циклические конструкции](#14)
    - [5. Функции (часть 1)](#15)
    - [6. Функции (часть 2)](#16)
    - [7. Списки](#17)
    - [8. Спецификация PEP8](#18)

2. [Python Essential](#PythonEssential)
    - [1. ООП - Классы, атрибуты, методы, конструктор](#21)
    - [2. ООП - Наследование](#22)
    - [3. ООП – Инкапсуляция и полиморфизм](#23)
    - [4. Исключения и оператор assert](#24)
    - [5. Итераторы](#25)
    - [6. Генераторы](#26)
    - [7. Последовательности (list, tuple)](#27)
    - [8. Множества и отображения (set, dict)](#28)
    - [9. Работа с файлами](#29)
    - [10. Модули и пакеты](#210)

3. [Python Advanced 2022](#PythonAdvanced)
    - [1. Элементы функционального программирования](#31)
    - [2. Работа с сетью](#32)
    - [3. Хранилища данных](#33)
    - [4. SQLite. Синтаксис и запросы](#34)
    - [5. Асинхронное программирование в Python](#35)
    - [6. Многопоточное программирование в Python](#36)
    - [7. Типизированный Python. Модульное тестирование](#37)

4. [Django](#Django)



<a name="PythonStarter"></a>
# Python Starter 

<a name="11"></a>
## 1. Введение в Python

***Задание 1***

Установите Python и PyCharm (или другую IDE с поддержкой Python, которая вам удобна). Исследуйте настройки, настройте среду разработки для себя: подберите цветовую схему и шрифт редактора, которые вам нравятся, включите или отключите отображение номеров строк, подсветку текущей строки, отображение разделителей между участками кода и т.п.

***Задание 2***

Создайте скрипт на языке Python, используя обычный текстовый редактор (можно использовать редактор кода, такой как, например, Sublime Text). Запустите его при помощи консоли. Запустите его двойным щелчком в проводнике Windows. Придумайте, как, используя то, что вы уже выучили, сделать так, чтобы окно консоли не закрывалось сразу же после запуска скрипта двойным щелчком.

***Задание 3***

Откройте IDLE (под Windows и OS X это приложение устанавливается вместе с Python). Поэкспериментируйте с обычными арифметическими выражениями. Попробуйте задать имя значению какого-либо выражения. Попробуйте вывести значение выражения с поясняющим текстом при помощи функции print, используя как имена, так и непосредственно выражения в качестве параметров функции.

***Задание 4***

Создайте новый проект в интегрированной среде разработки PyCharm. Создайте файл исходного кода и напишите программу, которая выводит ваше имя. Запустите его. Создайте второй файл с кодом и напишите программу, которая спрашивает у пользователя, как его зовут, и здоровается с ним. Запустите его. Переключитесь на первый скрипт и запустите его. Переключитесь обратно на второй скрипт.

<a name="12"></a>
## 2. Переменные и типы данных

***Задание 1***

Напишите программу, которая спрашивает у пользователя два слова и выводит их разделёнными запятой.

***Задание 2***

Напишите программу, которая запрашивает три целых числа a, b и x и выводит True, если x лежит между a и b, иначе – False.

***Задание 3***

Напишите программу, которая решает квадратное уравнение ax^2 + bx + c = 0 по формулам x1,2 = (-b ± √(b^2-4ac)) / 2a. Значения a, b и c вводятся с клавиатуры. Для извлечения корня используйте оператор возведения в степень, а не функцию math.sqrt, чтобы получить комплексные числа в случае, если подкоренное выражение отрицательно.

***Задание 4***

Напишите программу, которая запрашивает у пользователя радиус круга и выводит его площадь. Формула площади круга S = πr^2

<a name="13"></a>
## 3. Условные конструкции

***Задание 1***

Напишите программу, которая спрашивает у пользователя его имя, и если оно совпадает с вашим, выдаёт определённое сообщение.

***Задание 2***

Напишите программу, которая вычисляет значение функции в диапазоне значений x от -10 до 10 включительно с шагом, равным 1.

y = x^2 при -5 <= x <= 5;
y = 2*|x|-1 при x < -5;
y = 2x при x > 5.
Вычисление значения функции оформить в виде программной функции, которая принимает значение x, а возвращает полученное значение функции (y).

***Задание 3***

Напишите программу, которая решает квадратное уравнение ax^2 + bx + c = 0 в действительных числах. В отличие от аналогичного упражнения из прошлого урока, программа должна выдавать сообщение об отсутствии действительных корней, если значение дискриминанта D = b^2-4ac отрицательно, единственное решение x = -b/2a если он равен нулю, или два корня x1,2 = (-b ± √D) / 2a, если он положителен.

***Задание 4***

Напишите программу-калькулятор, в которой пользователь сможет ввести выбрать операцию, ввести необходимые числа и получить результат. Операции, которые необходимо реализовать: сложение, вычитание, умножение, деление, возведение в степень, синус, косинус и тангенс числа.

<a name="14"></a>
## 4. Циклические конструкции

***Задание 1***

Даны числа a и b (a < b). Выведите сумму всех натуральных чисел от a до b (включительно). 

***Задание 2***

Факториалом числа n называется число 𝑛! = 1 ∙ 2 ∙ 3 ∙ … ∙ 𝑛. Создайте программу, которая вычисляет факториал введённого пользователем числа.

***Задание 3*** 

Используя вложенные циклы и функции print(‘*’, end=’’), print(‘ ‘, end=’’) и print() выведите на экран прямоугольный треугольник.

***Задание 4***

Создайте программу, которая рисует на экране прямоугольник из звёздочек заданной пользователем ширины и высоты.

<a name="15"></a>
## 5. Функции (часть 1)

***Задание 1***

Создайте функцию, которая выводит приветствие для пользователя с заданным именем. Если имя не указано, она должна выводить приветствие для пользователя с Вашим именем. 

***Задание 2***

Создайте две функции, вычисляющие значения определённых алгебраических выражений. Выведите на экран таблицу значений этих функций от -5 до 5 с шагом 0.5. 

***Задание 3***

Создайте программу-калькулятор, которая поддерживает четыре операции: сложение, вычитание, умножение, деление. Все данные должны вводиться в цикле, пока пользователь не укажет, что хочет завершить выполнение программы. Каждая операция должна быть реализована в виде отдельной функции. Функция деления должна проверять данные на корректность и выдавать сообщение об ошибке в случае попытки деления на ноль.

***Задание 4***

Создайте программу, которая состоит из функции, которая принимает три числа и возвращает их среднее арифметическое, и главного цикла, спрашивающего у пользователя числа и вычисляющего их средние значения при помощи созданной функции.

<a name="16"></a>
## 6. Функции (часть 2)

***Задание 1***

Прочитайте в документации по языку Python информацию о перечисленных в резюме данного урока стандартных функциях. Проверьте их на практике. 

***Задание 2***

Создайте программу, которая проверяет, является ли палиндромом введённая фраза. 

***Задание 3***

Пусть на каждую ступеньку лестницы можно стать с предыдущей или переступив через одну. Определите, сколькими способами можно подняться на заданную ступеньку.

***Задание 4***

Напишите рекурсивную функцию, которая вычисляет сумму натуральных чисел, которые входят в заданный промежуток.

<a name="17"></a>
## 7. Списки

***Задание 1*** 

Создайте список и введите его значения. Найдите наибольший и наименьший элемент списка, а также сумму и среднее арифметическое его значений. 

***Задание 2*** 

Перепишите решение последней задачи из шестого урока так, чтобы она не использовала рекурсию и не вычисляла все промежуточные количества вариантов путей множество раз (что крайне неэффективно), а сохраняла их в списке. 

***Задание 3*** 

Простым называется число, которое делится нацело только на единицу и само себя. Число 1 не считается простым. Напишите программу, которая находит все простые числа в заданном промежутке, выводит их на экран, а затем по требованию пользователя выводит их сумму либо произведение.

***Задание 4***

Создайте список, введите количество его элементов и сами значения, выведите эти значения на экран в обратном порядке.

<a name="18"></a>
## 8. Спецификация PEP8

Откройте файл fix_me.py из папки homework. Используя обычный текстовый редактор (Notepad), исправьте все ошибки оформления кода согласно PEP 8.

____

<a name="PythonEssential"></a>
# Python Essential

<a name="21"></a>
## 1. ООП - Классы, атрибуты, методы, конструктор

***Задание 1***

Создайте класс, описывающий книгу. Он должен содержать информацию об авторе, названии, годе издания и жанре. Создайте несколько разных книг. Определите для него операции проверки на равенство и неравенство, методы __repr__ и __str__. 

***Задание 2*** 

Создайте класс, описывающий отзыв к книге. Добавьте в класс книги поле – список отзывов. Сделайте так, что при выводе книги на экран при помощи функции print также будут выводиться отзывы к ней. 

***Задание 3*** 

Ознакомьтесь со специальными методами в Python, используя ссылки в конце урока, и научитесь использовать те из них, назначение которых вы можете понять. Возвращайтесь к этой теме на протяжении всего курса и изучайте специальные методы, соответствующие темам каждого урока.

***Задание 4***

Создайте класс, описывающий автомобиль. Создайте класс автосалона, содержащий в себе список автомобилей, доступных для продажи, и функцию продажи заданного автомобиля.

<a name="22"></a>
## 2. ООП - Наследование

***Задание 1*** 

Создайте класс Editor, который содержит методы view_document и edit_document. Пусть метод edit_document выводит на экран информацию о том, что редактирование документов недоступно для бесплатной версии. Создайте подкласс ProEditor, в котором данный метод будет переопределён. Введите с клавиатуры лицензионный ключ и, если он корректный, создайте экземпляр класса ProEditor, иначе Editor. Вызовите методы просмотра и редактирования документов. 

***Задание 2*** 

Опишите классы графического объекта, прямоугольника и объекта, который может обрабатывать нажатия мыши. Опишите класс кнопки. Создайте объект кнопки и обычного прямоугольника. Вызовите метод нажатия на кнопку. 

***Задание 3*** 

Создайте иерархию классов с использованием множественного наследования. Выведите на экран порядок разрешения методов для каждого из классов. Объясните, почему линеаризации данных классов выглядят именно так.

***Задание 4***

Создайте иерархию классов транспортных средств. В общем классе опишите общие для всех транспортных средств поля, в наследниках – специфичные для них. Создайте несколько экземпляров. Выведите информацию о каждом транспортном средстве.

<a name="23"></a>
## 3. ООП – Инкапсуляция и полиморфизм

***Задание 1*** 

Создайте класс, описывающий автомобиль. Какие атрибуты и методы должны быть полностью инкапсулированы? Доступ к таким атрибутам и изменение данных реализуйте через специальные методы (get, set). 

***Задание 2*** 

Создайте 2 класса – языка, например, английский и испанский. У обоих классов должен быть метод greeting(). Оба создают разные приветствия. Создайте два соответствующих объекта из двух классов выше и вызовите действия этих двух объектов в одной функции (функция hello_friend). 

***Задание 3*** 

Используя ссылки в конце данного урока, ознакомьтесь с таким средством инкапсуляции как свойства. Ознакомьтесь с декоратором property в Python. Создайте класс, описывающий температуру и позволяющий задавать и получать температуру по шкале Цельсия и Фаренгейта, причём данные могут быть заданы в одной шкале, а получены в другой.

***Задание 4***

Опишите два класса Base и его наследника Child с методами method(), который выводит на консоль фразы соответственно "Hello from Base" и "Hello from Child".

<a name="24"></a>
## 4. Исключения и оператор assert

***Задание 1*** 

Выучите основные стандартные исключения, которые перечислены в данном уроке. 

***Задание 2*** 

Напишите программу-калькулятор, которая поддерживает следующие операции: сложение, вычитание, умножение, деление и возведение в степень. Программа должна выдавать сообщения об ошибке и продолжать работу при вводе некорректных данных, делении на ноль и возведении нуля в отрицательную степень. 

***Задание 3*** 

Опишите класс сотрудника, который включает в себя такие поля, как имя, фамилия, отдел и год поступления на работу. Конструктор должен генерировать исключение, если заданы неправильные данные. Введите список работников с клавиатуры. Выведите всех сотрудников, которые были приняты после заданного года.

***Задание 4***

Опишите свой класс исключения. Напишите функцию, которая будет выбрасывать данное исключение, если пользователь введёт определённое значение, и перехватите это исключение при вызове функции.

<a name="25"></a>
## 5. Итераторы

***Задание 1*** 

Реализуйте цикл, который будет перебирать все значения итерабельного объекта iterable.

***Задание 2*** 

Взяв за основу код примера example_5.py, расширьте функциональность класса MyList, добавив методы для очистки списка, добавления элемента в произвольное место списка, удаления элемента из конца и произвольного места списка.

***Задание 3***

Напишите итератор, который возвращает элементы заданного списка в обратном порядке (аналог reversed).

<a name="26"></a>
## 6. Генераторы

***Задание 1*** 

Напишите генератор, который возвращает элементы заданного списка в обратном порядке (аналог reversed). 

***Задание 2*** 

Выведите из списка чисел список квадратов четных чисел. Используйте 2 варианта решения: генератор и цикл.

***Задание 3***

Напишите функцию-генератор для получения n первых простых чисел.

<a name="27"></a>
## 7. Последовательности (list, tuple)

***Задание 1*** 

Создайте функцию от произвольного количества аргументов, которая вычисляет среднее арифметическое данных чисел. Вычислите при помощи неё среднее арифметическое двух заданных чисел и среднее арифметическое чисел из заданного диапазона. 

***Задание 2***

Используя документацию, ознакомьтесь с методами класса str. 

***Задание 3*** 

Напишите программу, которая вводит с клавиатуры текст и выводит отсортированные по алфавиту слова данного текста. 

***Задание 4*** 

Ознакомьтесь при помощи документации с классами namedtuple и deque модуля collections.

***Задание 5***

Напишите программу, которая вводит с клавиатуры последовательность чисел и выводит её отсортированной в порядке возрастания.

<a name="28"></a>
## 8. Множества и отображения (set, dict)

***Задание 1*** 

Даны две строки. Выведите на экран символы, которые есть в обоих строках. 

***Задание 2*** 

Создайте программу, которая эмулирует работу сервиса по сокращению ссылок. Должна быть реализована возможность ввода изначальной ссылки и короткого названия и получения изначальной ссылки по её названию. 

***Задание 3*** 

Ознакомьтесь при помощи документации с классами OrderedDict, defaultdict и ChainMap модуля collections.

***Задание 4***

Создайте словарь с ключами-строками и значениями-числами. Создайте функцию, которая принимает произвольное количество именованных параметров. Вызовите её с созданным словарём и явно указывая параметры.

<a name="29"></a>
## 9. Работа с файлами

***Задание 1*** 

Напишите скрипт, который создаёт текстовый файл и записывает в него 10000 случайных действительных чисел. Создайте ещё один скрипт, который читает числа из файла и выводит на экран их сумму. 

***Задание 2*** 

Модифицируйте исходный код сервиса по сокращению ссылок из предыдущих двух уроков так, чтобы он сохранял базу ссылок на диске и не «забывал» при перезапуске. При желании можете ознакомиться с модулем shelve (https://docs.python.org/3/library/shelve.html), который в данном случае будет весьма удобен и упростит выполнение задания.

***Задание 3***

Создайте список товаров в интернет-магазине. Сериализуйте его при помощи pickle и сохраните в JSON.

<a name="210"></a>
## 10. Модули и пакеты

***Задание 1***

Перепишите домашнее задание предыдущего урока (сервис для сокращения ссылок) таким образом, чтобы у него была основная часть, которая отвечала бы за логику работы и предоставляла обобщённый интерфейс, и модуль представления, который отвечал бы за взаимодействие с пользователем. При замене последнего на другой, взаимодействующий с пользователем иным способом, программа должна продолжать корректно работать. 

***Задание 2*** 

Повторите информацию о рассмотренных на уроке стандартных модулях. Ознакомьтесь также с модулями calendar, heapq, bisect, array, enum.

***Задание 3***

Создайте модуль для получения простых чисел. Импортируйте его из другого модуля. Импортируйте отдельные его имена.

----

<a name="PythonAdvanced"></a>
# Python Advanced 2022

<a name="31"></a>
## 1. Элементы функционального программирования

***Задание 1***

Ещё раз разберите все примеры к уроку, повторите теорию и ознакомьтесь с документацией по рассмотренным модулям.

***Задание 2***

Создайте список целых чисел. Получите список квадратов нечётных чисел из этого списка.

***Задание 3***

Создайте функцию-генератор чисел Фибоначчи. Примените к ней декоратор, который будет оставлять в последовательности только чётные числа.

<a name="32"></a>
## 2. Работа с сетью

***Задание 1***

Создайте UDP сервер, который ожидает сообщения о новых устройствах в сети. Он принимает сообщения определенного формата, в котором будет идентификатор устройства и печатает новые подключения в консоль. Создайте UDP клиента, который будет отправлять уникальный идентификатор устройства на сервер, уведомляя о своем присутствии.

***Задание 2***

Создайте UNIX сокет, который принимает сообщение с двумя числами, разделенными запятой. Сервер должен конвертировать строковое сообщения в два числа и вычислять его сумму. После успешного вычисления возвращать ответ клиенту.

***Задание 3***

Изучите более подробно и попробуйте возможности настройки, pull-а соединений и его режимов. Используя утилиту ab протестируйте ваши наработки (https://ru.wikipedia.org/wiki/ApacheBench).

***Задание 4***

Используя сервис https://jsonplaceholder.typicode.com/ попробуйте построить различные типы запросов и обработать ответы. Необходимо попрактиковаться с urllib и библиотекой requests. Рекомендуется сначала попробовать выполнить запросы, используя urllib, а затем попробовать реализовать то же самое используя requests

<a name="33"></a>
## 3. Хранилища данных

***Задание 1***

Создайте простые словари и сконвертируйте их в JSON. Сохраните JSON в файл и попробуйте загрузить данные из файла.

***Задание 2***

Создайте XML файл с вложенными элементами и воспользуйтесь языком поиска XPATH. Попробуйте осуществить поиск содержимого по созданному документу XML, усложняя свои запросы и добавляя новые элементы, если потребуется.

***Задание 3***

Поработайте с созданием собственных диалектов, произвольно выбирая правила для CSV файлов. Зарегистрируйте созданные диалекты и поработайте, используя их, с созданием/чтением файлом. 

***Задание 4***

Для таблицы «материала» из дополнительного задания создайте пользовательскую агрегатную функцию, которая считает среднее значение весов всех материалов результирующей выборки и округляет данной значение до целого. 

***Задание 5***

Для таблицы «материала» из дополнительного задания создайте пользовательскую функцию, которая принимает неограниченное количество полей и возвращает их конкатенацию.

<a name="34"></a>
## 4. SQLite. Синтаксис и запросы

***Задание 1***

Сделать таблицу для подсчёта личных расходов со следующими полями: id, назначение, сумма, время.

***Задание 2***

Создать консольный интерфейс (CLI) на Python для добавления новых записей в базу данных

***Задание 3***

Создать агрегатные функции для подсчёта общего количества расходов и расходов за месяц. Обеспечить соответствующий интерфейс для пользователя.

***Задание 4***

Измените таблиц так, чтобы можно было добавить не только расходы, а и доходы

***Задание 5***

Замените назначение на MCC и используйте его для определения назначения платежа

***Задание 6***

Настройте интеграцию с API своего банка для автоматической загрузки операций по карте

<a name="35"></a>
## 5. Асинхронное программирование в Python

***Задание 1***

Создайте функцию по вычислению факториала числа. Запустите несколько задач, используя ThreadPoolExecutor и замерьте скорость их выполнения, а затем замерьте скорость вычисления, используя тот же самый набор задач на ProcessPoolExecutor. В качестве примеров, используйте крайние значения, начиная от минимальных и заканчивая максимально возможными, чтобы увидеть прирост или потерю производительности. 

***Задание 2***

Создайте три функции, одна из которых читает файл на диске с заданным именем и проверяет наличие строку “Wow! ”. В случае, если файла нет, то засыпает на 5 секунд, а затем снова продолжает поиск по файлу. В случае, если файл есть, то открывает его и ищет строку “Wow!”. При наличии данной строки закрывает файл и генерирует событие, а другая функция ожидает данное событие и в случае его возникновения выполняет удаление этого файла. В случае если строки «Wow!» не было найдено в файле, то засыпать на 5 секунд. Создайте файл руками и проверьте выполнение программы. 

***Задание 3***

Разработайте сокет сервер на основе библиотеки asyncio. Сокет сервер должен выполнять сложение двух чисел, как из предыдущего примера по многопоточности.

<a name="36"></a>
## 6. Многопоточное программирование в Python

***Задание 1***

Создайте функцию по вычислению факториала числа. Запустите несколько задач, используя ThreadPoolExecutor и замерьте скорость их выполнения, а затем замерьте скорость вычисления, используя тот же самый набор задач на ProcessPoolExecutor. В качестве примеров, используйте крайние значения, начиная от минимальных и заканчивая максимально возможными, чтобы увидеть прирост или потерю производительности.

***Задание 2***

Создайте три функции, одна из которых читает файл на диске с заданным именем и проверяет наличие строку “Wow! ”. В случае, если файла нет, то засыпает на 5 секунд, а затем снова продолжает поиск по файлу. В случае, если файл есть, то открывает его и ищет строку “Wow!”. При наличии данной строки закрывает файл и генерирует событие, а другая функция ожидает  данное событие и в случае его возникновения выполняет удаление этого файла. В случае если строки «Wow!» не было найдено в файле, то засыпать на 5 секунд. Создайте файл руками и проверьте выполнение программы.

<a name="37"></a>
## 7. Типизированный Python. Модульное тестирование

***Задание 1*** 

Создать функцию, которая принимает список из элементов типа int, а возвращает новый список из строковых значений исходного массива. Добавить аннотацию типов для входных и результирующих значений функции.

## 

<a name="Django"></a>
# Django 

## 

## 

## 