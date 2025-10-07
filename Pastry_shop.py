quantity = int(input("Введите количество пирожных (больше 1):\n"))

for i in range(quantity, 0, -1):
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i} - расфасуем по 3 или по 5")
    elif i % 5 == 0:
        print(f"{i} - расфасуем по 5")
    elif i % 3 == 0:
        print(f"{i} - расфасуем по 3")
    else:
        print(f"{i} - не заказываем!")