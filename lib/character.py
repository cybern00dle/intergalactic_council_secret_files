#это класс персонажей
class Character:
    #конструктор персонажа
    def __init__(self):
        self.name = "name"
        self.picture = "picture"
        #в self.picture передаем наверное файл
        self.hello = "hello"
        self.goodbye = "goodbye"
        self.good_end = "good_end"
        self.trigger_good_end = "trigger_good_end"
        self.bad_end = "bad_end"
        self.trigger_bad_end = "trigger_bad_end"
        self.death = "death"
        self.trigger_death = "trigger_death" 
        self.neutral_end = "neutral_end"
        self.trigger_neutral_end = "trigger_neutral_end" 
        self.question ="question"
        self.close_to_end_coef = "close_to_end_coef"
        self.have_we_met_before = "have_we_met_before"
        self.level = "level"
        self.artefact = "artefact"

    def __str__(self):
        return self.name
    
    #функция взаимодействия персонажа с игроком
    def action(self, player):
        #персонаж задает вопрос игроку, игрок объявляется еще не мертвым, мы просим ввести ответ
        print(self.question)
        player['player_is_dead'] = 0
        answer = input('->')
        #дальше проверяем, триггером какого итога является ответ игрока
        if answer == self.trigger_good_end:
            end = self.good_end
            player['close_to_end_index'] += self.close_to_end_coef
            player['artefacts'] += self.artefact
            #хороший итог добавляет очки игроку и дает артефакт
        elif answer == self.trigger_bad_end:
            end = self.bad_end
            player['close_to_end_index'] -= self.close_to_end_coef
            #плохой итог отнимает очки игрока
        elif answer == self.trigger_death:
            end = self.death
            player['player_is_dead'] = 1
            #если ответ приводит к смерти, в словаре игрок меняем значение на 1
        else: 
            end = self.neutral_end
            #если игрок ввел с клавиатуры не пойми что, считаем, что это привело к нейтральному результату
        print(end)
    
    def meet_the_character(self):
        print(f'{self.name}: {self.hello}')
        #вывести картинку

    def farewell(self):
        print(f'{self.name}: {self.goodbye}')
        self.have_we_met_before = 1

    #def print_characters_image():
    # Таня, твоя задача: Внутри класса персонажей написать функцию, выводящую на экран картинку. 
    # Для этого разобраться с графическим выводом в питоне. Это необязательно, конечно, но было бы прикольно
