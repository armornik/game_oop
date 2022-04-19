import random

# Константы карт
SUIT_TUPLE = ('Пики', 'Червы', 'Трефы', 'Бубны')
RANK_TUPLE = ('Туз', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Валет', 'Дама', 'Король')

# Сколько карт раздается
N_CARDS = 8


def get_card(deck_list_in: list) -> dict:
    """Функция получает колоду, и возвращает верхнюю карту из неё"""
    this_card = deck_list_in.pop()  # получает верхнюю карту из колоды
    return this_card


def shuffle(deck_list_in: list) -> list:
    """Функция получает колоду, и перемешивает её"""
    deck_list_ut = deck_list_in.copy()  # копирует стартовую колоду
    random.shuffle(deck_list_ut)
    return deck_list_ut


if __name__ == '__main__':
    print('Добро пожаловать в игру "Больше или меньше".')
    print('Вы должны сделать выбор, и указать больше или меньше следующая карта.    ')
    print('В случае правильного выбора вы получаете 20 очков, при неправильном - теряете 15.')
    print('Вы начинаете с 50 очками.')
    print()

    starting_deck_list = []

    for suit in SUIT_TUPLE:
        for this_value, rank in enumerate(RANK_TUPLE):
            card_dict = {'rank': rank, 'suit': suit, 'value': this_value + 1}
            starting_deck_list.append(card_dict)

    score = 50

    while True:
        print()
        game_deck_list = shuffle(starting_deck_list)
        current_card_dict = get_card(game_deck_list)
        current_card_rank = current_card_dict['rank']
        current_card_value = current_card_dict['value']
        current_card_suit = current_card_dict['suit']
        print(f'Начальная карта: {current_card_rank} {current_card_suit}')
        print()

        for card_number in range(0, N_CARDS):  # играем одну игру
            answer = input(f'Следующая карта будет выше или ниже, чем {current_card_rank} {current_card_suit}?  '
                           f'(нажмите h или l): ')
            answer = answer.casefold()  # force lower case
            next_card_dict = get_card(game_deck_list)
            next_card_rank = next_card_dict['rank']
            next_card_suit = next_card_dict['suit']
            next_card_value = next_card_dict['value']
            print(f'Следующая карта: {next_card_rank} {next_card_suit}')

            if answer == 'h':
                if next_card_value > current_card_value:
                    print('Вы правы, она выше')
                    score = score + 20
                else:
                    print('Извините, карта была ниже')
                    score = score - 15

            elif answer == 'l':
                if next_card_value < current_card_value:
                    score = score + 20
                    print('Вы правы, карта ниже')

                else:
                    score = score - 15
                    print('Извините, карта выше')

            print('Количество Ваших очков:', score)
            print()
            current_card_rank = next_card_rank
            current_card_value = next_card_value

        goAgain = input('Чтобы сыграть снова, нажмите ENTER, или "q" чтобы выйти: ')
        if goAgain == 'q':
            break

    print('Пока')
