def cesar_script(text, shift, alphabet):
    result = ''
    for symbol in text:
        index = alphabet.find(symbol)
        if index == -1:
            result += symbol
        else:
            next_index = (index + shift) % len(alphabet)
            result += alphabet[next_index]
    return result

russian_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
english_alphabet = 'abcdefghijklmnopqrstuvwxyz'

text = input('Введите пожалуйста вашу строку:\n')
lower_text = text.lower()

contains_russian = all(ch in russian_alphabet for ch in lower_text)
contains_english = all(ch in english_alphabet for ch in lower_text)

alphabet = ""
if contains_russian:
    alphabet = russian_alphabet
elif contains_english:
    alphabet = english_alphabet

shift = int(input('Введите сдвиг:\n'))
choice = input('Вы хотите зашифровать или дешифровать? (1 - зашифровать, 2 - дешифровать):\n')

if choice == '1':
    if alphabet != "":
        result = cesar_script(text, shift, alphabet)
        print(result)
    else:
        print('Вы что-то ввели не правильно')
elif choice == '2':
    if alphabet != "":
        result = cesar_script(text, -shift, alphabet)
        print(result)
    else:
        print('Вы что-то ввели не правильно')
else:
    print('Вы что-то ввели не правильно')