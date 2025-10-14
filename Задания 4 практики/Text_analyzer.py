vowels = 'аеёиоуыэяюАЕЁИОУЫЭЮЯ'
consonants = 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ'
special_symbols = 'ьЬъЪ'

def analyzer(text: str):
    vowels_letters = sum(text.count(letter) for letter in vowels)
    total_letters = sum(text.count(letter) for letter in consonants)
    special_count = sum(text.count(s) for s in special_symbols)
    consonants_letters = total_letters
    space_count = text.count(' ')
    words_count = len(text.split())

    from collections import Counter
    count_letters = Counter(text)

    top_symbols = [item[0] for item in count_letters.most_common(3)]

    print(f'Количество гласных символов: {vowels_letters}')
    print(f'Количество согласных символов: {consonants_letters}')
    print(f'Количество специальных символов ("ь" и "ъ"): {special_count}')
    print(f'Количество пробелов: {space_count}')
    print(f'Топ 3 самых часто встречающихся символов: {top_symbols}')
    print(f'Количество слов: {words_count}')

text = input()
analyzer(text)