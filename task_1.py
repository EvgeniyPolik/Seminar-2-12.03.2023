"""
На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число
монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите
минимальное количество монет, которые нужно перевернуть
"""
user_input = input('Введите количетсво монет: ')
if user_input.isdigit():
    number_coins = int(user_input)
    number_reverse = number_coins
    for i in range(number_coins):
        number_reverse -= int(input(f'Введите положение монеты { i + 1} (0 - решка или 1 - герб): '))
    number_avers = number_coins - number_reverse
    print(f'Минимальное количестово монет для переворачивания:'
          f' {number_reverse if number_reverse < number_avers else number_avers}')
else:
    print('Неверный ввод')
