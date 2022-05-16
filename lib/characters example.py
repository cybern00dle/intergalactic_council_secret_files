from lib.character import Character
#это файл для создания персонажей. каждый персонаж является классом, который наследован от класса Character(то есть все функции оттуда, кроме __init__)
class Hare(Character):
    def __init__(self):
        super().__init__()
        self.name = 'Заяц'
        self.picture = 1
        self.hello = 'я заяц, привет-привет!\n'
        self.goodbye = 'еще увидимся.\n'
        self.good_end = 'Заяц: катись, колобок, дальше *вас не стали есть из-за пыли*\n'
        self.trigger_good_end = '1'
        self.bad_end = 'Заяц: сейчас я тебя съем! *зайцу не нравятся такие как вы. Он откусывает бочок*\n'
        self.trigger_bad_end = '2'
        self.death = 'Заяц: вкусный был колобок! *Зря вы нагрубили зайцу. вас съели*\n'
        self.trigger_death = '3' 
        self.neutral_end = 'Заяц: какой-то ты невкусный, Колобок *заяц задумался об ассортименте булочной и решил, что вы не самый вкусный*\n'
        self.trigger_neutral_end = '4' 
        self.question ='Заяц: колобок-колобок, куда ты катишься?\n\n1. катаюсь в пыли, чтобы быть красивым\n2. просто качусь...\n3. катись лесом, заяц\n4. в булочную\n'
        self.close_to_end_coef = 1
        self.have_we_met_before = 0
        self.level = 1
 
class Fox(Character):
    def __init__(self):
        super().__init__()
        self.name = 'Лиса'
        self.picture = 2
        self.hello = 'ну здравствуй, колобок\n'
        self.goodbye = 'пока.\n'
        self.good_end = 'Лиса: я с пола не ем *сказала лиса,  чтобы вы не подумали, что она вас не догонит*\n'
        self.trigger_good_end = '3'
        self.bad_end = 'Лиса: я, конечно, голодна, но не очень *лисе не понравился ваш ответ. Она откусывает кусочек*\n'
        self.trigger_bad_end = '1'
        self.death = 'Лиса: ну наконец-то не фаст-фуд! *пока вы думали, вас съели*\n'
        self.trigger_death = '4'
        self.neutral_end = 'Лиса: вот был бы ты без изюма... *лисе не понравился изюм, и она вас отпустила*\n'
        self.trigger_neutral_end = '2'
        self.question = 'Лиса: Что было раньше, курица или яйцо?\n\n1. яйцо\n2. изюм. изюм всему голова\n3. *не отвечать и катиться дальше*\n4. ну..... дайте подумать....\n'
        self.close_to_end_coef = 2
        self.have_we_met_before = 0
        self.level = 2
       
