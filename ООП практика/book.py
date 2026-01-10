# Импорт модуля для работы с датами и временем
from datetime import datetime

# Определение класса Book (Книга)
class Book:
    # Конструктор класса, инициализирует объект при создании
    def __init__(self, title, year, author):
        self.title = title    # Название книги
        self.author = author  # Автор книги
        self.year = year      # Год издания

    # Метод для получения информации о книге
    def info(self):
        return f'Title: {self.title}, year: {self.year}, author: {self.author}'

    # Магический метод для строкового представления объекта (print(book))
    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.year})"

    # Магический метод для сравнения объектов (book1 == book2)
    def __eq__(self, other):
        # Книги считаются равными, если у них одинаковые названия
        return isinstance(other, Book) and self.title == other.title

    # Свойство (property) - вычисляемое поле "возраст книги"
    @property
    def age(self):
        # Возвращает разницу между текущим годом и годом издания
        return datetime.now().year - self.year

    # Классовый метод (classmethod) - альтернативный конструктор
    @classmethod
    def from_string(cls, data):
        # Создает объект из строки формата "название;год;автор"
        title, year_str, author = data.split(';')
        # cls ссылается на сам класс Book
        return cls(title, int(year_str), author)

# Создание объекта book (экземпляра класса Book)
book = Book('Война и мир', 1905, 'Лев Толстой')

# Вызов магического метода __str__ через print
print(book)
# Вызов обычного метода info
print(book.info())
# Использование свойства age (вычисляется динамически)
print(f"Возраст книги: {book.age} лет")

# Использование классового метода для создания объекта
another_book = Book.from_string("Преступление и наказание;1866;Федор Достоевский")
print(another_book.info())
