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

def ending_scene(Boss, player, artefacts_result):
    if artefacts_result == 'verybad':
        with open('texts\\bossfight\\endings\\kidnap.txt', 'r', encoding='utf-8') as f:
            kidnap = f.read()
            print(kidnap)
    else:
        if 'Вязаный воронёнок' in player['artefacts'] and 'Бумажный кинжал' in player['artefacts']:
            print('''
* Вы уже выполнили свою работу, собрав некоторое количество артефактов, являющихся зацепками, необходимыми Совету для поимки культа.
* С другой стороны, Вам известно, в какой день, в какое время и в каком кабинете культ собирается на Печёрке.
* Что Вы будете делать?
1. отправиться домой
2. остаться и попытаться нейтрализовать культ самостоятельно''')
            answer_leave = input('-> ').lower().strip()
            if answer_leave == '1':
                print('''
* Вы решаете, что сейчас не время геройствовать. Возможно, Вы бы и остались, чтобы продолжить расследование, но усталость и нежелание рисковать здоровьем (или даже жизнью) берут верх.''')
                with open('texts\\bossfight\\endings\\leave.txt', 'r', encoding='utf-8') as f:
                    leave = f.read()
                    print(leave)
            elif answer_leave == '2':
                print('''
* Вы знаете, как долго разбирают дела в Межгалактическом Совете. Бюрократия, что тут скажешь.
* Вы решаете взять расследование в свои руки и довести дело до конца.
''')
                Boss.conversation()
                if 'technical_artefact_1' in player['artefacts'] and 'technical_artefact_1' in player['artefacts']:
                    Boss.fighting(artefacts_result, player)
                    Boss.crow_summon(player)
                else:
                    Boss.leave()

            else:
                print('''
* Кажется, Вы ввели что-то не то. Скорее всего, Вы устали настолько, что тело Вас не слушается. Это может значить только одно: пора собираться домой.''')
                with open('texts\\bossfight\\endings\\leave.txt', 'r', encoding='utf-8') as f:
                    leave = f.read()
                    print(leave)
        elif 'Вязаный воронёнок' in player['artefacts'] and 'Бумажный кинжал' not in player['artefacts']:
            print('''
* Вы знаете, что культ собирается на Печёрке по воскресеньям, но не знаете, в каком кабинете и в какое время. Может, Вы бы и хотели заняться культом самостоятельно, но у Вас недостаточно сведений для его поимки.''')
            with open('texts\\bossfight\\endings\\leave.txt', 'r', encoding='utf-8') as f:
                leave = f.read()
                print(leave)
        elif 'Вязаный воронёнок' not in player['artefacts'] and 'Бумажный кинжал' in player['artefacts']:
            print('''
* Вы знаете, что культ собирается на Печёрке в кабинете 125 в 10:00, но не знаете день сбора. Может, Вы бы и хотели заняться культом самостоятельно, но у Вас недостаточно сведений для его поимки.''')
            with open('texts\\bossfight\\endings\\leave.txt', 'r', encoding='utf-8') as f:
                leave = f.read()
                print(leave)
        else:
            print('''
* К сожалению (или к счастью), Вам неизвестно, в какой день, в какое время и в каком кабинете культ собирается на Печёрке. Может, Вы бы и хотели заняться культом самостоятельно, но у Вас недостаточно сведений для его поимки.''')
            with open('texts\\bossfight\\endings\\leave.txt', 'r', encoding='utf-8') as f:
                leave = f.read()
                print(leave)
