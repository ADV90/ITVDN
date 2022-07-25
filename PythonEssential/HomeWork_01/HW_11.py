"""Создайте класс, описывающий книгу. Он должен содержать информацию об авторе, названии, годе издания и жанре.
Создайте несколько разных книг. Определите для него операции проверки на равенство и неравенство, методы repr и str.
"""


class Book:

    def __init__(
            self,
            author,
            title,
            year,
            genre
    ):
        self.author = author
        self.title = title
        self.year = year
        self.genre = genre

    def __eq__(self, other):
        return self.author == other.author and self.title == other.title

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return f"Автор: {self.author} \nНаименование: {self.title} \nГод: {self.year} \nЖанр: {self.genre} \n"

    def __repr__(self):
        return f"Автор: {self.author} \nНаименование: {self.title} \nГод: {self.year} \nЖанр: {self.genre} \n"


book1 = Book(
    'Федор Достоевский',
    'Преступление и наказание',
    1866,
    'Classic'
)
book2 = Book(
    'Николай Гоголь',
    'Мертвые души',
    1842,
    'Classic'
)
book3 = Book(
    'Лев Толстой',
    'Война и мир',
    '1865-1868',
    'Classic'
)
book4 = Book(
    'Николай Гоголь',
    'Вий',
    1835,
    'Classic'
)

print(book1 == book2 == book3 == book4, '\n')

books = Book(book1, book2, book3, book4)

print(books.__str__())
print(repr(books))
