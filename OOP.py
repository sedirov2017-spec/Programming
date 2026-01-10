# Класс - шаблон для создания объектов
class Animal:
    def __init__(self, name, age):
        self.name = name  # атрибут
        self.age = age    # атрибут
    
    def speak(self):      # метод
        print(f"{self.name} издает звук")

# Наследование
class Dog(Animal):
    def speak(self):      # полиморфизм
        print(f"{self.name} гавкает")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} мяукает")

# Создание объектов
dog = Dog("Шарик", 3)
cat = Cat("Мурка", 2)

# Использование полиморфизма
animals = [dog, cat]
for animal in animals:
    animal.speak()
    # Вывод:
    # Шарик гавкает
    # Мурка мяукает


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # инкапсуляция
    
    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return amount
        return 0
    
    def get_balance(self):
        return self.__balance

# Использование
account = BankAccount("Иван", 1000)
account.deposit(500)
print(account.get_balance())  # 1500
account.withdraw(200)
print(account.get_balance())  # 1300
