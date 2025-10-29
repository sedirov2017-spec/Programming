from datetime import datetime

class Book:
    def __init__(self, title, year, author):
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        return f'Title: {self.title}, year: {self.year}, author: {self.author}'

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.year})"

    def __eq__(self, other):
        return isinstance(other, Book) and self.title == other.title

    @property
    def age(self):
        return datetime.now().year - self.year

    @classmethod
    def from_string(cls, data):
        title, year_str, author = data.split(';')
        return cls(title, int(year_str), author)

book = Book('Война и мир', 1905, 'Лев Толстой')

print(book)
print(book.info())
print(f"Возраст книги: {book.age} лет")

another_book = Book.from_string("Преступление и наказание;1866;Федор Достоевский")
print(another_book.info())
