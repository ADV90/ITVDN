class Book:

    def __init__(self, author, name, year_of_publishing, genre):
        self.author = author
        self.name = name
        self.year_of_publishing = year_of_publishing
        self.genre = genre
        self.reviews = []

    def add_review(self, user, review):
        self.reviews.append(Review(user, review))

    def info_book(self):
        for info in (self.author, self.name, self.year_of_publishing, self.genre):
            print(info)
        for review in self.reviews:
            print(review)


class Review:

    def __init__(self, user, review):
        self.user = user
        self.review = review

    def __str__(self):
        return f'пользователь - {self.user} \n отзыв - {self.review}'


book_1 = Book("Э.М.Ремарк", "Три товарища", 1936, "роман")
book_1.add_review("art_077", "Великолепно! Сразу позвонил своим друзьям")
book_1.add_review("Valera_03", "Не сразу проникся смыслом, но под конец книги всё стало ясно.")
book_1.info_book()
print()

book_2 = Book("Ли Куан Ю", "Из третьего мира в первый", 2012, "биография")
book_2.add_review("Oxana_097", "Очень познавательно и увлекательно! Про настоящих людей")
book_2.add_review("Kostya_0099", "Слишком длинная. Я бы уместил в 100 страниц.")
book_2.info_book()