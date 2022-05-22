import random


class Boss:
    def __init__(self):
        self.name = "Максим Михайлович"
        self.picture = ''
        self.crow_index = 0
        self.health_bar = 5000

    def __str__(self):
        return self.name

    def conversation(self):
        with open('texts\\bossfight\\convo.txt', 'r', encoding='utf-8') as f:
            convo = f.read()
            print(convo)

    def leave(self):
        print('''
* Вас убеждает тон голоса Максима Михайловича. Вы разворачиваетесь и выходите из комнаты.
* Должно быть, культ прикрывается детским факультативом, думаете Вы. Возможно, организации даже не знают о существовании друг друга - дедушка-профессор не дал никаких наводок.''')
        with open('texts\\bossfight\\endings\\leave.txt', 'r', encoding='utf-8') as f:
            leave = f.read()
            print(leave)

    def fighting(self, artefacts_result, player):
        with open('texts\\bossfight\\fight_beg.txt', 'r', encoding='utf-8') as f:
            fight_beg = f.read()
            print(fight_beg)
        # вступительная речь к бою
        user_bar = 1000
        superweapon = 0
        if artefacts_result == 'excellent':
            print('''* Книжечка "Тайны ФГН" в Вашем сумкоподобном Бездонном Хранилище начинает светиться.
* На артефактах начинают проступать светящиеся латинские буквы. Буквы складываются в слоги и буквосочетания. 
* Отдельные "gau", "juve", "moles" напоминают Вам об обведённом красным пункте книжки. Вы же помните первый куплет "Gaudeamus"?''')
            # текст просит гаудеамус
            gaud = input('-> ').lower().strip()
            if gaud == 'gaudeamus igitur juvenes dum sumus post jucundam juventutem post molestam senectutem nos habebit humus':
                print('''* Артефакты в Ваших руках складываются в Вороний Клинок.
* Усиление атаки: 300 единиц урона.
* Шанс уклонения от атаки: +40%.
''')
                # успешный сбор оружия
                superweapon = 1
            else:
                print('''* Вам не удалось собрать Вороний Клинок. Возможно, Вам стоило лучше учить латынь.
''')
                # неуспешный сбор оружия
        else:
            print('''* Артефактов недостаточно для сбора Вороньего Клинка. Возможно, Вам стоило быть внимательнее при общении с персонажами.
''')
        print(f'''* Ваше здоровье: {user_bar}.
* Здоровье Максима Михайловича: {self.health_bar}.
''')
        while True:
            hit_us = random.randint(50, 125)
            if hit_us <= 100:
                if superweapon == 1:
                    hit_us += 300
                hit_us += player['close_to_end_index'] * 10
                # доп. очки за уровень
                self.health_bar -= hit_us
                print(f'''* Вы нанесли точный удар! 
* Урон, нанесённый Максиму Михайловичу: {hit_us}.
* Ваше здоровье: {user_bar}.
* Здоровье Максима Михайловича: {self.health_bar}.
''')
                if self.health_bar <= 0:
                    with open('texts\\bossfight\\fight_end.txt', 'r', encoding='utf-8') as f:
                        fight_end = f.read()
                        print(fight_end)
                    self.crow_index = 1
                    break
            else:
                print('''* Максим Михайлович отразил атаку.
''')
            hit_mm = random.randint(1, 125)
            dodge_chance = 0
            if superweapon == 1:
                dodge_chance = random.randint(1, 10)
            if hit_mm <= 100 and dodge_chance > 6:
                user_bar -= hit_mm
                print(f'''* Максим Михайлович нанёс точный удар! 
* Урон, нанесённый Вам: {hit_us}.
* Ваше здоровье: {user_bar}.
* Здоровье Максима Михайловича: {self.health_bar}.
''')
                if user_bar <= 0:
                    with open('texts\\bossfight\\endings\\fight_death.txt', 'r', encoding='utf-8') as f:
                        fight_death = f.read()
                        print(fight_death)
                    break
            else:
                print('''* Вы отразили атаку.
''')

    def crow_summon(self, player):
        if self.crow_index == 1:
            with open('texts\\bossfight\\crow_beg.txt', 'r', encoding='utf-8') as f:
                crow_beg = f.read()
                print(crow_beg)
            # вступительная речь к призыву вороны
            password = input('-> ').lower().strip()
            if password == 'non scholae sed vitae discimus':
                with open('texts\\bossfight\\endings\\win.txt', 'r', encoding='utf-8') as f:
                    win = f.read()
                    print(win)
                # хорошая концовка
            else:
                with open('texts\\bossfight\\endings\\crow_death.txt', 'r', encoding='utf-8') as f:
                    crow_death = f.read()
                    print(crow_death)
