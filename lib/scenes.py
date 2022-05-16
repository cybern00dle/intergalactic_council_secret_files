#это функция, которая создает сцену взаимодействия с одним персонажем
def one_character_scene(Character, hello_text, player):
    result = 0
    Character.meet_the_character()
    Character.action(player)
    if player['player_is_dead'] == 1:
        print('конец игры. начать сначала?\n1. Да\n2. Нет')
        answer = input('->')
        if answer == '1':
            result = 2
        else:
            print('на этом всё.')
            result=1
    else:
        Character.farewell()
    return result