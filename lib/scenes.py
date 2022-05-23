#это функция, которая создает сцену взаимодействия с одним персонажем
def one_character_scene(Character, hello_text, player):
    result = 0
    Character.meet_the_character()
    Character.action(player)
    if player['player_is_dead'] == 1:
        print('''Конец игры. Начать сначала?
1. Да
2. Нет''')
        answer = input('-> ').lower().strip()
        if answer == '1':
            result = 2
        else:
            print('На этом всё.')
            result = 1
    else:
        Character.farewell()
    return result
