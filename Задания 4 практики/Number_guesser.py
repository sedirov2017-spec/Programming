import random

def guess():
    num = random.randint(1, 100)
    print('Я загадал число от 1 до 100, попробуй отгадать')

    for attempt in range(3):
        try:
            guess = int(input('Угадай число: '))
        except:
            print('Писать нужно только числа')
            return

        if guess == num:
            print('Окак. Ладно ты угадал')
            return
        elif guess > num:
            print('Загаданное число меньше.')
        else:
            print('Загаданное число больше.')

        if attempt == 0:
            continue
        elif attempt == 1:
            if num % 2 == 0:
                print('а ещё загаданное число нечётное.')
            else:
                print('а ещё загаданное число нечётное.')

    print(f'Хорошая попытка, но загаданным числом было {num}')

guess()