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
        self.clist = []

    def __eq__(self, other):
        return self.author == other.author and self.title == other.title

    def __ne__(self, other):
        return not self == other

    def add_review(self, user, review):
        review = str((Review(user, review)))
        self.clist.append(review)

    def __str__(self):
        return ("Автор: {} \nНаименование: {} \nГод: {} \nЖанр: {} \n".format(self.author, self.title, self.year,
                                                                              self.genre)
                + '\n'.join(str(review) for review in self.clist) + '\n')

    # def __repr__(self):
    #     return f"Автор: {self.author} \nНаименование: {self.title} \nГод: {self.year} \nЖанр: {self.genre} \n"


class Review:
    def __init__(self, user, review):
        self.user = user
        self.review = review

    def __str__(self):
        return f'{self.user}: {self.review}'


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

book1.add_review("user_11", "Великолепно!")
book1.add_review("user_12", "Тест 12")
book2.add_review("user_21", "Тест. Книга 2")
book3.add_review("user_31", "Тестовый отзыв к книге 3.")
book3.add_review("user_32", "Книга 3. Тест 3.2")
book4.add_review("user_41", "Тест. Книга 4.")

print(book1 == book2 == book3 == book4, '\n')

books = Book(book1, book2, book3, book4)

print(books)
# print(repr(books))
