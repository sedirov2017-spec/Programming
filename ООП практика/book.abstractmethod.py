# Импортируем модуль для создания абстрактных классов
from abc import ABC, abstractmethod

# Создаем абстрактный класс Printable
# ABC означает Abstract Base Class - абстрактный базовый класс
class Printable(ABC):
    # Абстрактный метод - должен быть реализован в дочерних классах
    @abstractmethod
    def print_info(self):
        pass  # Абстрактный метод не имеет реализации

# Класс Book наследуется от Printable
# Теперь Book должен реализовать все абстрактные методы родителя
class Book(Printable):
    # Конструктор класса
    def __init__(self, title, year, author):
        self.title = title    # Название книги
        self.author = author  # Автор
        self.year = year      # Год издания

    # Метод для получения информации о книге в виде строки
    def info(self):
        return f"Title: {self.title}, Year: {self.year}, Author: {self.author}"

    # Обязательная реализация абстрактного метода из Printable
    def print_info(self):
        print(self.info())  # Выводит информацию на печать

# Создаем объект (экземпляр) класса Book
book = Book('Война и мир', 1905, 'Лев Толстой')

# Вызываем метод info() и печатаем возвращаемую строку
print(book.info())

# Можем также вызвать print_info() для непосредственной печати
book.print_info()
