import random

move = ['камень', 'ножницы', 'бумага']

def check_win(pm, cm):
    if pm == cm:
        return 'draw'
    if (pm == 'камень' and cm == 'ножницы') or (pm == 'ножницы' and cm == 'бумага') or (pm == 'бумага' and cm == 'камень'):
        return 'pm'
    else:
        return 'cm'

def game():
    print('Играем в камень, ножницы, бумагу до 3 побед. Начинай!\n')
    pm_score = 0
    cm_score = 0

    while pm_score < 3 and cm_score < 3:
        pm_move = input('Ваш ход (камень, ножницы, бумага):\n').lower()
        if pm_move not in move:
            print('Некорректный ход. Напиши "камень", "ножницы" или "бумага"\n')
            continue

        cm_move = random.choice(move)
        print(f'Я выбрал: {cm_move}\n')

        winner = check_win(pm_move, cm_move)

        if winner == 'draw':
            print('Ничья!\n')
        elif winner == 'pm':
            print('Ты выиграл этот раунд!\n')
            pm_score += 1
        else:
            print('Я выиграл этот раунд!\n')
            cm_score += 1

        print(f'Текущий счет — Игрок: {pm_score} | Компьютер: {cm_score}\n')

    if pm_score == 3:
        print('Поздравляю, ты победили!\n')
    else:
        print('Я победил! Попробуй ещё.\n')

game()