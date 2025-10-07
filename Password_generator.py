import random
import string

def generate_password(length, charset):
    return ''.join(random.choice(charset) for _ in range(length))

print("=== Генератор паролей (Приятный, понятный и красивый) ===")
length = int(input("Введите длину пароля: "))

use_lower = input("Включить строчные буквы? (y/n): ").lower() == 'y'
use_upper = input("Включить заглавные буквы? (y/n): ").lower() == 'y'
use_digits = input("Включить цифры? (y/n): ").lower() == 'y'
use_special = input("Включить спецсимволы? (y/n): ").lower() == 'y'

charset = ''
if use_lower:
    charset += string.ascii_lowercase
if use_upper:
    charset += string.ascii_uppercase
if use_digits:
    charset += string.digits
if use_special:
    charset += string.punctuation

if not charset:
    print("Вы не выбрали ни один тип символов, создание пароля невозможно.")
else:
    password = generate_password(length, charset)
    print("Ваш пароль:", password)