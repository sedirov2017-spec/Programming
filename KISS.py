# Излишне сложное решение для фильтрации четных чисел
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Сложный однострочник с лямбда-функцией и фильтром
result = list(filter(lambda x: x % 2 == 0, numbers))

# Простой цикл с понятной логикой
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)


# Пример по куче условий:

# Избыточная вложенность и сложные условия
def process_data(data):
    if data is not None:
        if isinstance(data, list):
            if len(data) > 0:
                if all(isinstance(item, (int, float)) for item in data):
                    return sum([x**2 for x in data if x > 0 and x % 2 == 0 or x % 3 == 0])
    return None

# Упрощенная версия с лучшей читаемостью
def process_data(data):
    if not data or not isinstance(data, list):
        return None
    
    for item in data:
        if not isinstance(item, (int, float)):
            return None
    
    total = 0
    for num in data:
        if num > 0 and (num % 2 == 0 or num % 3 == 0):
            total += num ** 2
    
    return total


# Задача: получить список квадратов положительных чисел
data = [-2, -1, 0, 1, 2, 3, 4]

# Сложный однострочник (хотя и рабочий)
result = [x**2 for x in data if x > 0]

# Простое решение с обычным циклом
result = []
for number in data:
    if number > 0:
        result.append(number ** 2)

