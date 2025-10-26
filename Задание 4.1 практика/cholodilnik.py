from decimal import Decimal
import datetime

DATE_FORMAT = '%Y-%m-%d'

# Данные из образца
goods = {
    'Пельмени Универсальные': [
        {'amount': Decimal('0.5'), 'expiration_date': datetime.date(2023, 7, 15)},
        {'amount': Decimal('2'), 'expiration_date': datetime.date(2023, 8, 1)},
    ],
    'Вода': [
        {'amount': Decimal('1.5'), 'expiration_date': None}
    ],
}

# Функции
def add(title, amount, expiration_date=None):
    if title in goods:
        goods[title].append({'amount': Decimal(amount), 'expiration_date': expiration_date})
    else:
        goods[title] = [{'amount': Decimal(amount), 'expiration_date': expiration_date}]

def add_by_note(note):
    parts = note.split()
    amount = Decimal(parts[0])
    expiration_date = None
    if len(parts) > 2:
        try:
            expiration_date = datetime.datetime.strptime(parts[-1], DATE_FORMAT).date()
            name_parts = parts[1:-1]
        except:
            name_parts = parts[1:]
    else:
        name_parts = parts[1:]
    title = ' '.join(name_parts)
    add(title, amount, expiration_date)

def find(keyword):
    result = []
    for name in goods:
        if keyword.lower() in name.lower():
            result.append(name)
    return result

def total_amount(product_name):
    total = Decimal('0')
    for name in find(product_name):
        for batch in goods[name]:
            total += batch['amount']
    return total

def get_all_details(product_name):
    """Возвращает список строк с информацией о каждом продукте"""
    details = []
    for name in find(product_name):
        qty = sum(batch['amount'] for batch in goods[name])
        date_list = [batch['expiration_date'].strftime(DATE_FORMAT) for batch in goods[name] if batch['expiration_date']]
        dates_str = ', '.join(date_list) if date_list else 'неограниченно'
        details.append(f"{name}: {qty} шт., сроки: {dates_str}")
    return details

if __name__ == "__main__":
    while True:
        command = input("Введите команду ('поиск', 'добавить', 'выход'): ").strip().lower()
        if command == 'выход':
            break
        elif command == 'поиск':
            keyword = input("Введите название продукта для поиска: ")
            results = find(keyword)
            if results:
                details_list = get_all_details(keyword)
                for detail in details_list:
                    print(detail)
            else:
                print("Продукты не найдены.")
        elif command == 'добавить':
            note = input("Введите описание продукта (например: '3.0 Пельмени Универсальные 2023-09-01'): ")
            add_by_note(note)
            print("Продукт добавлен.")
        else:
            print("Неизвестная команда. Попробуйте снова.")
