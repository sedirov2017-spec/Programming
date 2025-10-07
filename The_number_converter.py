def roman_convert(s):
    roman_map = {'i': 1, 'v': 5, 'x': 10, 'l': 50,'c': 100, 'd': 500, 'm': 1000}
    s = s.lower()
    if s.isdigit():
        num = int(s)
        if 1 <= num <= 3999:
            val_map = [(1000,'M'), (900,'CM'), (500,'D'), (400,'CD'), (100,'C'), (90,'XC'), (50,'L'), (40,'XL'), (10,'X'), (9,'IX'), (5,'V'), (4,'IV'), (1,'I')]
            roman = ""
            for val, sym in val_map:
                while num >= val:
                    roman += sym
                    num -= val
            return roman
        else:
            return "Число вне диапазона (1-4000)."
    elif all(ch in 'ivxlcdm' for ch in s):
        total = 0
        prev = 0
        for ch in reversed(s):
            val = roman_map[ch]
            if val < prev:
                total -= val
            else:
                total += val
            prev = val
        if 1 <= total <= 3999:
            return str(total)
        else:
            return "Римское число вне диапазона (1-3999)."
    else:
        return "Неверный ввод."

text = input('Введите число для преобразования от 1 до 3999 (обычное) или от i до mmmcmxcix (римское в нижнем регистре)):\n')
print("Результат:", roman_convert(text))