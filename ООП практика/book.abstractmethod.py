from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def print_info(self):
        pass

class Book(Printable):
    def __init__(self, title, year, author):
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        return f"Title: {self.title}, Year: {self.year}, Author: {self.author}"

    def print_info(self):
        print(self.info())

book = Book('Война и мир', 1905, 'Лев Толстой')
print(book.info())
