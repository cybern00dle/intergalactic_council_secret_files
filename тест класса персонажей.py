import random
from lib.character import Character
import lib.scenes as sc
from lib.characters import Captain, Emo_Janitor, The_Lost_Student, Sergeant_Peepers, Safety_Belt, The_clone, Talking_pie, The_lost_child, Wicket, Predatory_plant, Projector, Red_cat, Printer_station, Seagull_Charmer, Zhenya, FGN_student, Booklets, Cleaner, Timur, Strange_group

player = {'close_to_end_index': 1, 'player_is_dead': 0, 'artefacts': []}

hello_text = '''Добро пожаловать в текстовый квест "Белая Ворона"!
Чтобы выбрать действие, введите с клавиатуры цифру, под которой написано желаемое действие.
1. Начать.
2. Повторить правила'''
answer = ''
while answer != '1':
    print(hello_text)
    answer = input('-> ').lower().strip()

f = open('lib\\texts\\acts\\act1.txt', 'r', encoding='utf-8')
act1_text = f.read()
f.close()
f1 = open('lib\\texts\\acts\\act2.txt', 'r', encoding='utf-8')
act2_text = f1.read()
f1.close()
f2 = open('lib\\texts\\acts\\act3.txt', 'r', encoding='utf-8')
act3_text = f2.read()
f2.close()
f3 = open('lib\\texts\\acts\\act4.txt', 'r', encoding='utf-8')
act4_text = f3.read()
f3.close()
character_list_act1 = [Captain(), Emo_Janitor(), The_Lost_Student(), Sergeant_Peepers(), Safety_Belt(), act1_text]
character_list_act2 = [Wicket(), The_lost_child(), Predatory_plant(), Talking_pie(), The_clone(), act2_text]
character_list_act3 = [Projector(), Red_cat(), Printer_station(), Seagull_Charmer(), Zhenya(), act3_text]
character_list_act4 = [FGN_student(), Booklets(), Cleaner(), Timur(), Strange_group(), act4_text]
list_of_character_list = [character_list_act1, character_list_act2, character_list_act3, character_list_act4]
for character_list in list_of_character_list:
    print(character_list[5])
    stop = False
    while stop == False:
        for character in character_list:
            if character == character_list[-2]:
                stop = True
            #пока персонажи идут подряд, цикл прерывается, когда мы доходим до последнего персонажа(но предпоследнего элемента, потому что последний элемент - текст перед актом)
            if not isinstance(character, str):
                if character.have_we_met_before == 0:
                    res = sc.one_character_scene(character, hello_text, player)
                    if res == 1:
                        stop = True
                        break
                    elif res == 2:
                        stop = False
                        player['player_is_dead'] = 0
                        player['close_to_end_index'] = 1
                        character_list_act1 = [Captain(), Emo_Janitor(), The_Lost_Student(), Sergeant_Peepers(), Safety_Belt(), act1_text]
                        character_list_act2 = [Wicket(), The_lost_child(), Predatory_plant(), Talking_pie(), The_clone(), act2_text]
                        character_list_act3 = [Projector(), Red_cat(), Printer_station(), Seagull_Charmer(), Zhenya(), act3_text]
                        character_list_act4 = [FGN_student(), Booklets(), Cleaner(), Timur(), Strange_group(), act4_text]
                        break


def artefacts_collection(player):
    final_artefacts = [value for value in player['artefacts'] if value != '']
    artefacts_number = len(final_artefacts)
    if 'technical_artifact_2' in final_artefacts:
        final_artefacts.remove('technical_artifact_2')
    if 'technical_artifact_1' in final_artefacts:
        final_artefacts.remove('technical_artifact_1')
    i = input('''* Кажется, все разошлись по домам. В Вышке никого не осталось. Вы решаете собраться с мыслями и замечаете, что Ваша сумка стала очень тяжелой.
1. Открыть сумку и посмотреть, что внутри.
2. Выбросить сумку.
-> ''').lower().strip()
    if i == '1' and final_artefacts != []:
        print('* В Вашей сумке Вы находите: ', ", ".join(final_artefacts), '''
* Сохраните на будущее. Вдруг пригодится.''')
    elif i == '1' and final_artefacts == []:
        print('Это не сумка тяжелая, а Вы устали.')
    else:
        print('Странное решение. Но как хотите.')
        # ТУТ НАДО УДАЛИТЬ ВСЕ АРТЕФАКТЫ

    return(artefacts_number)


result_for_final_fight = artefacts_collection(player)
artefacts_number = result_for_final_fight
artefacts_result = ''
if artefacts_number == 18:
    artefacts_result = 'excellent'
elif artefacts_number > 10 or artefacts_number == 10:
    artefacts_result = 'good'
elif 10 > artefacts_number > 5:
    artefacts_result = 'bad'
else:
    artefacts_result = 'verybad'

print(artefacts_number)
health_bar = 5000


def conversation():
    with open('lib\\texts\\bossfight\\convo.txt', 'r', encoding='utf-8') as f:
        convo = f.read()
        print(convo)


def leave_boss():
    print('''
* Вас убеждает тон голоса Максима Михайловича. Вы разворачиваетесь и выходите из комнаты.
* Должно быть, культ прикрывается детским факультативом, думаете Вы. Возможно, организации даже не знают о существовании друг друга - дедушка-профессор не дал никаких наводок.''')
    with open('lib\\texts\\bossfight\\endings\\leave.txt', 'r', encoding='utf-8') as f:
        leave_boss = f.read()
        print(leave_boss)


def fighting(health_bar, artefacts_result, player):
    crow_index = 0
    with open('lib\\texts\\bossfight\\fight_beg.txt', 'r', encoding='utf-8') as f:
        fight_beg = f.read()
        print(fight_beg)
    user_bar = 1000
    superweapon = 0
    if artefacts_result == 'excellent':
        print('''* Книжечка "Тайны ФГН" в Вашем сумкоподобном Бездонном Хранилище начинает светиться.
* На артефактах начинают проступать светящиеся латинские буквы. Буквы складываются в слоги и буквосочетания. 
* Отдельные "gau", "juve", "moles" напоминают Вам об обведённом красным пункте книжки. Вы же помните первый куплет "Gaudeamus"?''')
        gaud = input('-> ').lower().strip()
        if gaud == 'gaudeamus igitur juvenes dum sumus post jucundam juventutem post molestam senectutem nos habebit humus':
            print('''* Артефакты в Ваших руках складываются в Вороний Клинок.
* Усиление атаки: 300 единиц урона.
* Шанс уклонения от атаки: +40%.
''')
            superweapon = 1
        else:
            print('''* Вам не удалось собрать Вороний Клинок. Возможно, Вам стоило лучше учить латынь.
''')
    else:
        print('''* Артефактов недостаточно для сбора Вороньего Клинка. Возможно, Вам стоило быть внимательнее при общении с персонажами.
''')
    print(f'''* Ваше здоровье: {user_bar}.
* Здоровье Максима Михайловича: {health_bar}.
''')
    while True:
        hit_us = random.randint(50, 125)
        if hit_us <= 100:
            if superweapon == 1:
                hit_us += 300
            hit_us += player['close_to_end_index'] * 10
            health_bar -= hit_us
            print(f'''* Вы нанесли точный удар! 
* Урон, нанесённый Максиму Михайловичу: {hit_us}.
* Ваше здоровье: {user_bar}.
* Здоровье Максима Михайловича: {health_bar}.
''')
            if health_bar <= 0:
                with open('lib\\texts\\bossfight\\fight_end.txt', 'r', encoding='utf-8') as f:
                    fight_end = f.read()
                    print(fight_end)
                crow_index = 1
                break
        else:
            print('''* Максим Михайлович отразил атаку.
''')
        hit_mm = random.randint(1, 125)
        dodge_chance = 0
        if superweapon == 1:
            dodge_chance = random.randint(1, 10)
        if hit_mm <= 100 and dodge_chance <= 6:
            user_bar -= hit_mm
            print(f'''* Максим Михайлович нанёс точный удар! 
* Урон, нанесённый Вам: {hit_mm}.
* Ваше здоровье: {user_bar}.
* Здоровье Максима Михайловича: {health_bar}.
''')
            if user_bar <= 0:
                with open('lib\\texts\\bossfight\\endings\\fight_death.txt', 'r', encoding='utf-8') as f:
                    fight_death = f.read()
                    print(fight_death)
                break
        else:
            print('''* Вы отразили атаку.
''')
    return crow_index


def crow_summon(crow_sum):
    if crow_sum == 1:
        with open('lib\\texts\\bossfight\\crow_beg.txt', 'r', encoding='utf-8') as f:
            crow_beg = f.read()
            print(crow_beg)
        password = input('-> ').lower().strip()
        if password == 'non scholae sed vitae discimus':
            with open('lib\\texts\\bossfight\\endings\\win.txt', 'r', encoding='utf-8') as f:
                win = f.read()
                print(win)
        else:
            with open('lib\\texts\\bossfight\\endings\\crow_death.txt', 'r', encoding='utf-8') as f:
                crow_death = f.read()
                print(crow_death)


def ending_scene(health_bar, player, artefacts_result):
    if artefacts_result == 'verybad':
        with open('lib\\texts\\bossfight\\endings\\kidnap.txt', 'r', encoding='utf-8') as f:
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
                with open('lib\\texts\\bossfight\\endings\\leave.txt', 'r', encoding='utf-8') as f:
                    leave = f.read()
                    print(leave)
            elif answer_leave == '2':
                print('''
* Вы знаете, как долго разбирают дела в Межгалактическом Совете. Бюрократия, что тут скажешь.
* Вы решаете взять расследование в свои руки и довести дело до конца.
''')
                conversation()
                if 'technical_artifact_1' in player['artefacts'] and 'technical_artifact_2' in player['artefacts']:
                    crow_sum = fighting(health_bar, artefacts_result, player)
                    crow_summon(crow_sum)
                else:
                    leave_boss()

            else:
                print('''
* Кажется, Вы ввели что-то не то. Скорее всего, Вы устали настолько, что тело Вас не слушается. Это может значить только одно: пора собираться домой.''')
                with open('lib\\texts\\bossfight\\endings\\leave.txt', 'r', encoding='utf-8') as f:
                    leave = f.read()
                    print(leave)
        elif 'Вязаный воронёнок' in player['artefacts'] and 'Бумажный кинжал' not in player['artefacts']:
            print('''
* Вы знаете, что культ собирается на Печёрке по воскресеньям, но не знаете, в каком кабинете и в какое время. Может, Вы бы и хотели заняться культом самостоятельно, но у Вас недостаточно сведений для его поимки.''')
            with open('lib\\texts\\bossfight\\endings\\leave.txt', 'r', encoding='utf-8') as f:
                leave = f.read()
                print(leave)
        elif 'Вязаный воронёнок' not in player['artefacts'] and 'Бумажный кинжал' in player['artefacts']:
            print('''
* Вы знаете, что культ собирается на Печёрке в кабинете 125 в 10:00, но не знаете день сбора. Может, Вы бы и хотели заняться культом самостоятельно, но у Вас недостаточно сведений для его поимки.''')
            with open('lib\\texts\\bossfight\\endings\\leave.txt', 'r', encoding='utf-8') as f:
                leave = f.read()
                print(leave)
        else:
            print('''
* К сожалению (или к счастью), Вам неизвестно, в какой день, в какое время и в каком кабинете культ собирается на Печёрке. Может, Вы бы и хотели заняться культом самостоятельно, но у Вас недостаточно сведений для его поимки.''')
            with open('lib\\texts\\bossfight\\endings\\leave.txt', 'r', encoding='utf-8') as f:
                leave = f.read()
                print(leave)


ending_scene(health_bar, player, artefacts_result)
