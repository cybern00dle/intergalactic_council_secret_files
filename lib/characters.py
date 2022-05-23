from lib.character import Character
# Это файл для создания персонажей. Каждый персонаж является классом, который наследован от класса Character (то есть все функции оттуда, кроме __init__)
class Captain(Character):
    def __init__(self):
        super().__init__()
        self.name = 'Капитан Кондраки'
        self.picture = ''
        self.hello = 'Приветствую, разведчик! Надеюсь, ты готова к своей первой операции по поддержанию равновесия в Мультивселенной? Конечно, готова! Вот твое первое задание...'
        self.goodbye = '''Не хочу сгущать краски, но от твоего успеха напрямую зависит существование всех разумных форм жизни! Удачи, разведчик!
'''
        self.good_end = '''Капитан Кондраки: Какая забавная земная шутка! Вот что, держи за нее подарок. Если ты будешь успешно взаимодействовать с обитателями, то они тоже выдадут тебе что-нибудь интересное.
* Вы получили Ручку, которую точно кто-то попросит.'''
        self.trigger_good_end = '1'
        self.bad_end = 'Капитан Кондраки: ...Неловко. Ладно, бывай. По возвращении отчитаешься перед Пиперсом.'
        self.trigger_bad_end = '2'
        self.death = '''Капитан Кондраки: ...Бедняга.
* Капитан смотрит на Вас с некой жалостью. Он приближается к вам, вытягивая в Вашем направлении руки, но, вопреки Вашим надеждам, это не объятие. Капитан пожалел Вас достаточно, чтобы быстро свернуть Вам шею, и Вы почти не чувствуете боли перед наступлением вечной темноты. Вы мертвы.'''
        self.trigger_death = '3'
        self.neutral_end = '''Капитан Кондраки: Да-да, конечно, удачи.
* Капитан быстро теряет в Вас интерес и исчезает.'''
        self.trigger_neutral_end = '4'
        self.question = '''Капитан Кондраки: Хочешь ли ты что-то мне сказать перед началом миссии?
1. *рассказать анекдот про медведя*
2. *промолчать*
3. *рассказать анекдот про улитку*
4. *пообещать, что не подведёте*'''
        self.close_to_end_coef = 1
        self.have_we_met_before = 0
        self.level = 1
        self.artefact = 'Ручка, которую точно кто-то попросит'

class Emo_Janitor(Character):
    def __init__(self):
        super().__init__()
        self.name = 'Эмо-уборщик'
        self.picture = ''
        self.hello = 'Жизнь тлен.'
        self.goodbye = '''Жизнь все равно тлен.
'''
        self.good_end = '''Эмо-уборщик: Мейнстрим. Но многие и такого не знают. На, заслужила.
* Вы получили Брендовые тапочки My Chemical Romance.'''
        self.trigger_good_end = '3'
        self.bad_end = 'Эмо-уборщик: Хм, невежество не заведет тебе друзей. Артефакта тебе не видать.'
        self.trigger_bad_end = '1'
        self.death = '''Эмо-уборщик: Мда.
* Эмо-уборщик, не меняясь в лице, проворачивает швабру в руках и пронзает Вас насквозь. Вы мертвы.'''
        self.trigger_death = '2'
        self.neutral_end = 'Эмо-уборщик: Хм, ладно. Но артефакт все равно не дам.'
        self.trigger_neutral_end = '4'
        self.question = '''Если ты не слушаешь хорошую музыку, то артефакт не получишь. Ты знаешь, о чем я.
1. Да ты и сам хорошую музыку не слушаешь
2. (Что-то Вы точно слышали) Come back down to my knees, gotta get free...
3. (Что-то Вы точно слышали) We are the very hurt you sold...
4. Да как-то не до музыки было. Тренировки, миссии, все дела...'''
        self.close_to_end_coef = 1
        self.have_we_met_before = 0
        self.level = 2
        self.artefact = 'Брендовые тапочки My Chemical Romance (Вы не решаетесь комментировать)'

class The_Lost_Student(Character):
    def __init__(self):
        super().__init__()
        self.name = 'Потерявшийся студент'
        self.picture = ''
        self.hello = '* Студент смотрит на вас и начинает быстро говорить что-то на языке жестов. На ненастоящем языке жестов.'
        self.goodbye = '''* Студент уходит куда-то. Вы предполагаете, что в поисках космического костюма и выхода.
'''
        self.good_end = '''Потерявшийся студент: ...Что, настолько заметно? Эх, теперь я должен тебе дать артефакт, такие уж правила. Эээээ... А, вот! Вот, держи, тебе нужнее, я уже сдал этот экзамен!
* Вы получили Конспект по цифровой грамотности.'''
        self.trigger_good_end = '4'
        self.bad_end = '* Студент пугается, стукает вас по голове тетрадью, а потом исчезает. Вы не успеваете сказать ему, что это была шутка.'
        self.trigger_bad_end = '2'
        self.death = '* Вы, довольная собой, идёте дальше и поскальзываетесь на банановой кожуре. Вы не успеваете подумать о том, карма ли это. Вы мертвы.'
        self.trigger_death = '3'
        self.neutral_end = '* Студент пялится на Вас. Вы начинаете сомневаться в своей экспертизе касательно жестовых языков.'
        self.trigger_neutral_end = '1'
        self.question = '''...
1. Ты уверен, что это настоящий язык жестов?
2. *пригрозить* Сейчас вызову Сержанта Пиперса, он разберется, что это у нас за шпион.
3. *вызвать охрану. Вы не знаете, кто это и что он тут делает.*
4. Я свой, не бойся, можешь не делать вид, что не понимаешь меня.'''
        self.close_to_end_coef = 1
        self.have_we_met_before = 0
        self.level = 3
        self.artefact = 'Конспект по цифровой грамотности ("+5 к сдаче НОКа" сказали бы разработчики, если бы Вы сдавали НОК)'

class Sergeant_Peepers(Character):
    def __init__(self):
        super().__init__()
        self.name = 'Сержант Пиперс'
        self.picture = ''
        self.hello = 'А, ты опять. Ничего не знаешь, но активно делаешь вид, что заслужила повышение, чтобы мешать продвинуться по карьерной лестнице тем, кто *кхм-кхм* действительно этого заслуживает.'
        self.goodbye = '''* Высокомерно и не прощаясь, Сержант уходит. Вы надеетесь, что на борту скоро появится психолог.
'''
        self.good_end = '''Сержант Пиперс: Чистая удача! Ты не можешь знать этого сама! 
* Сержант злится и убегает, роняя красную папочку в жесткой обложке.'''
        self.trigger_good_end = '1'
        self.bad_end = 'Сержант Пиперс: Ага, так я и знал! Назад можешь не возвращаться, Капитан все узнает: и то, что тебе кажется смешным анекдот про улитку, и то, что ты ничегошеньки не знаешь! Повышение у меня в кармане!'
        self.trigger_bad_end = '2'
        self.death = '''Сержант Пиперс: Ты меня запугивать вздумала? 
* Сержант побелел от ярости. 
Сержант Пиперс: Что ж... Не жить тебе, самозванка. 
* Он нападает на вас и сильно ударяет в висок. 
* Вы мертвы.'''
        self.trigger_death = '3'
        self.neutral_end = 'Сержант Пиперс: То есть не знаешь! Я все доложу Капитану!'
        self.trigger_neutral_end = '4'
        self.question = '''Ты даже не знаешь, в каком году была основана наша корпорация.
1. Нет, знаю! 1995.
2. Нет, знаю! 1908. 
3. Шел бы ты отсюда, дружок-пирожок, пока не нажил врагов выше по званию. 
4. Знаю, но не скажу.'''
        self.close_to_end_coef = 1
        self.have_we_met_before = 0
        self.level = 4
        self.artefact = 'Папочка с компроматом (лучше у Вас, чем у Сержанта Пиперса)'

class Safety_Belt(Character):
    def __init__(self):
        super().__init__()
        self.name = 'Ремень безопасности'
        self.picture = ''
        self.hello = 'Пристегни меня!'
        self.goodbye = '''* Не-ремень безопасности тихо уползает в другой космический корабль. Вы надеетесь, что это будет корабль сержанта.
'''
        self.good_end = '''Ремень безопасности: Эх, ладно, зришь в самую суть, на вот.
* Вы получили Окаменелость.'''
        self.trigger_good_end = '1'
        self.bad_end = 'Ремень безопасности недоволен Вашими манерами. У ремня безопасности нет мимики, но это не мешает вам почувствовать его разочарование.'
        self.trigger_bad_end = '2'
        self.death = '''* Не спросив себя о том, почему ремень безопасности разговаривает, а Бога - о том, как Вы дожили до сегодняшнего дня, Вы ожидаемо узнаете, что ремень безопасности - хищный мимик. 
* Вы мертвы.'''
        self.trigger_death = '3'
        self.neutral_end = '* Вы успешно находите механика, который зовет Вас через пять минут к Вашему транспорту. Ремня безопасности больше нет.'
        self.trigger_neutral_end = '4'
        self.question = '''Пристегнуться?
1. (Это точно мимик!) *вежливо попросите его отдать Вам средство передвижения*
2. (Это точно мимик! *пригрозить ему*
3. А чё звучит. *пристегнуться*
4. *позвать механика и спросить, с каких пор в транспорте есть ремни безопасности*'''
        self.close_to_end_coef = 1
        self.have_we_met_before = 0
        self.level = 5
        self.artefact = 'Окаменелость'

class The_lost_child(Character):
    def __init__(self):
        super().__init__()
        self.name = 'Ребёнок, который пришел на олимпиаду и потерялся'
        self.picture = ''
        self.hello = 'Привет!'
        self.goodbye = '''Пока!
'''
        self.good_end = 'Ребёнок: Спасибо! Знаешь, никогда не поливай цветы кофе. А ещё не гладь кота против шерсти.'
        self.trigger_good_end = '3'
        self.bad_end = '* Вы проходите мимо и чувствуете, как Вам в спину прилетает железная линейка. Неприятно.'
        self.trigger_bad_end = '2'
        self.death = '''* Зря Вы так. Ребенок устал и хочет домой. Он не хочет оставаться в Вышке. Но он-то попадет домой, а Вы уже нет.
* Вы мертвы.'''
        self.trigger_death = '4'
        self.neutral_end = '''Ребёнок: А Вы точно волонтёр? Я лучше кого-нибудь ещё поищу.
* Школьник быстро уходит, несколько раз подозрительно оглядываясь'''
        self.trigger_neutral_end = '1'
        self.question = '''Где здесь выход?
1. Не знаю. Я здесь родилась и здесь умру.
2. *молча пройти мимо*
3. Пойдем вместе найдем. *проводить ребенка*
4. Зачем тебе уходить, тебе в вышке не нравится?'''
        self.close_to_end_coef = 1
        self.have_we_met_before = 0
        self.level = 7
        self.artefact = ''

class Predatory_plant(Character):
    def __init__(self):
        super().__init__()
        self.name = 'Совершенно обычный цветок, только с небольшой пастью и зубами'
        self.picture = ''
        self.hello = 'Эй! Да не туда смотри, левее, левее. Ага, в горшке.'
        self.goodbye = '''...
'''
        self.good_end = '''О-о-о, вода со вкусом воды, спасибо! Не уходи, у меня есть подарок 
* Цветок роется под листьями и вручает вам стаканчик из-под кофе.'''
        self.trigger_good_end = '3'
        self.bad_end = '''* Пока цветок летит до земли, до Вас доносится пара проклятий.
* Вы живы, но под правой лопаткой что-то подозрительно чешется.'''
        self.trigger_bad_end = '4' 
        self.death = '''* Когда Вы слышали, что энергетики вредят здоровью, то наверняка не представляли, что именно таким образом. Цветок пьёт энергетик, вылезает из горшка и съедает Вас.
* Вы мертвы.'''
        self.trigger_death = '2'
        self.neutral_end = '* Цветок не отвечает. Вы решаете, что спать нужно больше четырёх часов в день.'
        self.trigger_neutral_end = '1'
        self.question = '''Цветок: Полей меня.
1. Ты умеешь разговаривать?
2. *кажется, в вашей сумке оставался энергетик. Полить цветок энергетиком*
3. *сходить за водой из кулера и полить цветок водой*
4. О господи, говорящий цветок! *выбросить цветок в окно*'''
        self.close_to_end_coef = 1
        self.have_we_met_before = 0
        self.level = 8
        self.artefact = 'Стаканчик из-под кофе'

class Wicket(Character):
    def __init__(self):
        super().__init__()
        self.name = 'Турникет'
        self.picture = ''
        self.hello = '...'
        self.goodbye = '''...
'''
        self.good_end = '* Загорается зелёная стрелочка. Вы проходите в корпус'
        self.trigger_good_end = '2'
        self.bad_end = ''
        self.trigger_bad_end = ''
        self.death = '''* Загорается зелёная лампочка. Вы начинаете проходить, но турникет вдруг резко проворачивается и ломает Вам спину.
* Скорая путает корпус на Печёрке и с корпусом на Костина, и Вы умираете. '''
        self.trigger_death = '1'
        self.neutral_end = ''
        self.trigger_neutral_end = ''
        self.question = '''…
1. *приложить пропуск фотографией вверх*
2. *приложить пропуск фотографией вниз*'''
        self.close_to_end_coef = 1
        self.have_we_met_before = 0
        self.level = 6
        self.artefact = ''

class Talking_pie(Character):
    def __init__(self):
        super().__init__()
        self.name = 'Говорящий пирог'
        self.picture = ''
        self.hello = '''* В процессе поиска вы заглядываете в столовую. С прилавка на вас смотрит пирог.
Пирог: Какой я румяный, какой я вкусный...
* Вы решаете взять его. '''
        self.goodbye = '''Всё-таки приятно быть выбранным.
'''
        self.good_end = '''* Вы съедаете пирог. Он оказывается с луком, зато внутри есть бумажка. Вы разворачиваете её.
* Записка гласит: «Звёзд не видно в микроскоп». '''
        self.trigger_good_end = '3'
        self.bad_end = '* Теперь у вас в сумке есть пирог.'
        self.trigger_bad_end = '4'
        self.death = '''* Пирог не отвечает. Вы решаете съесть его, но как только вы откусываете кусочек, пирог отвечает.
Пирог: Разговариваю!
* Вы пугаетесь и умираете. Да, вот так.'''
        self.trigger_death = '2'
        self.neutral_end = '''Пирог: Не ешь меня, я это... От бабушки ушел, от второй бабушки ушел, от ... От кого же ещё ушёл... 
* Пирог начинает вспоминать. Вы не хотите дослушивать и уходите. Он продолжает вспоминать.'''
        self.trigger_neutral_end = '1'
        self.question = '''Пирог: Почему ты меня выбрала?
1. Пирог-пирог, я тебя съем.
2. Ты тоже разговариваешь?
3. *молча съесть пирог*
4. *положить пирог в сумку*'''
        self.close_to_end_coef = 1
        self.have_we_met_before = 0
        self.level = 9
        self.artefact = 'Записка'

class The_clone(Character):
    def __init__(self):
        super().__init__()
        self.name = 'Злой клон Лосяша'
        self.picture = ''
        self.hello = 'Нефеноменально.'
        self.goodbye = '''И всё же нефеноменально.
'''
        self.good_end = '''* Злой клон Лосяша уходит, не поблагодарив вас. Он роняет ключи от космического корабля прошлогодней модели. Вы забираете их себе.'''
        self.trigger_good_end = '4'
        self.bad_end = '''* Злой клон Лосяша: Кофейная гуща - это ненаучно!
* Стиснув зубы и стукнув копытом, похмуревший злой клон Лосяша уходит.'''
        self.trigger_bad_end = '2'
        self.death = '''* Вы не успеваете и заметить, как становитесь убиты ретроградным Юпитером.
* Сегодня явно не ваш день.'''
        self.trigger_death = '3'
        self.neutral_end = '''Злой клон Лосяша: Ох уж эта молодёжь, всё бы вам в интернете найти.
* Разочарованный злой клон Лосяша уходит.'''
        self.trigger_neutral_end = '1'
        self.question = '''Злой клон Лосяша: Неправильный у вас институт, ни одного микроскопа нет. Вот как мне узнать свой гороскоп на сегодня?!
1. Найти в интернете.
2. Давайте я лучше вам все по кофейной гуще расскажу.
3. Гороскопы – глупость.
4. Он есть в самом юго-восточном коворкинге.'''
        self.close_to_end_coef = 1
        self.have_we_met_before = 0
        self.level = 10
        self.artefact = 'Космический корабль прошлогодней модели'

class Projector(Character):
    def __init__(self):
        super().__init__()
        self.name = 'Проектор'
        self.picture = ''
        self.hello = ''' *жужжит*
* Проектор, подвешенный к потолку, встречает вас гудением лампы.
* Изображение абстрактной композиции из шумов и полосок на стене начинает мигать, то темнея, то бледнея, как вдруг появляется огромный знак вопроса, а затем фотография аппетитной котлеты с картофельным пюре.'''
        self.goodbye = '''*дребезжит*.
'''
        self.good_end = '''* Цвет проецируемого света меняется на зелëный. Появляются слабые помехи, после чего на экране мелькают фотографии мужчины, сначала одна в пустыне на фоне древнего храма, потом другая с глиняной статуэткой, третья - на фоне логотипа с вороной рядом с другими людьми его возраста, и четвёртая - рядом с девочкой с пурпурными волосами. Внезапно трансляция прекращается. '''
        self.trigger_good_end = '3'
        self.bad_end = '''* Проектор выводит на экран эмодзи-череп, после чего падает, ломая пополам стоящую под ним парту. Вы напуганы, но живы.'''
        self.trigger_bad_end = '1'
        self.death = '''* Цвет проецируемого света меняется на красный. После непродолжительной настройки линз проектор выпускает мощный лазер и поворачивается лампой к вам.
* Вас сожгли.'''
        self.trigger_death = '4'
        self.neutral_end = '* Проектор сначала немного глючит, после чего транслирует на стену видеоклип "Never Gonna Give You Up".'
        self.trigger_neutral_end = '2'
        self.question = '''* Похоже, этот проектор осознаёт себя. Как найти общий язык с ним?
1. *показать ему большой палец*
2. *показать фото своей любимой модели спейс-шаттла*
3. *попытаться связаться с помощью телепатии*
4. *спросить его вслух о том, знает ли он что-то про белых ворон*'''
        self.close_to_end_coef = 1
        self.have_we_met_before = 0
        self.level = 11
        self.artefact = 'technical_artifact_1'

class Red_cat(Character):
    def __init__(self):
        super().__init__()
        self.name = 'Рыжая кошечка'
        self.picture = ''
        self.hello = '''* Вы решаете немного передохнуть и осмотреться. Перед собой вы замечаете пушистый полосатый комочек.
Рыжая кошечка: Мр-р-рть!'''
        self.goodbye = '''Мя.
'''
        self.good_end = '''Рыжая кошечка: ур-р-р-рр-р-р-р-рр-р-р.
* Вы замечаете, что у зверька есть ошейник. К нему привязана флешка. К чему бы это?'''
        self.trigger_good_end = '2'
        self.bad_end = '''Рыжая кошечка: ...
* Кошка не сомневается в своей очаровательности, но в вашей адекватности - да. Она идёт дальше, а вам - в другую сторону.'''
        self.trigger_bad_end = '4'
        self.death = '''Рыжая кошечка: КХ-Х-Х-Х!
* По вашему телу проходит разряд статического электричества. Не 220 V, но этого достаточно, чтобы уничтожить ваш хрупкий внеземной аналог нервной системы.
* Вы умираете.'''
        self.trigger_death = '1'
        self.neutral_end = '* Кошка пугается и убегает. Она не держит на вас зла и скоро забудет об этом происшествии.'
        self.trigger_neutral_end = '3' 
        self.question = '''* Кошка садится напротив и пристально вас изучает.
1. КИСА-А-А!!!! *фанатично гладить*
2. Привет! *почесать за ушком*
3. *нарочито пристально изучить в ответ*
4. *игнорировать*'''
        self.close_to_end_coef = 1
        self.have_we_met_before = 0
        self.level = 12
        self.artefact = 'Флешка'

class Printer_station(Character):
    def __init__(self):
        super().__init__()
        self.name = 'Преподавательница'
        self.picture = ''
        self.hello = '''Извините, вы не могли бы мне помочь?
* Вы видите растерянную преподавательницу, кучу мятых бумажек, сотни чернильных пятен разных размеров и нервно мигающий оранжевым индикатором принтер Xenon.'''
        self.goodbye = '''...
''' 
        self.good_end = '''* Вы, оглядываясь по сторонам, используете не привычный межгалактический архив, а земной Google.
* Чуть-чуть покопавшись, вы находите модель принтера и пересобираете его. 
* У вас остаётся две лишние детали - одна бесформенная и бесполезная, однако вторая по форме напоминает перо. И на ощупь как перо. И на вкус - самое настоящее воронье перо. Только светится.'''
        self.trigger_good_end = '2'
        self.bad_end = '''* Вы достаёте из Бездонного Хранилища звуковую отвёртку, направляете её на принтер и цвет его индикатора резко сменяется на зелёный.
* Прибор выплёвывает замятую бумагу и печатает красивые, чистые документы. Но в лотке даже нет бумажных листов...
* Преподавательница садится на пол и много думает. Похоже, лингвистам всё-таки придётся лишний час подождать контрольных.'''
        self.trigger_bad_end = '1'
        self.death = '''* На что вы рассчитывали? Преподавательнице сейчас не до шуток, у её лингвистов оценки не проставлены, а они сидят сейчас на паре без препода и, наверное, чаи гоняют.
* Через окошко в вас ударяет молния и вы умираете.'''
        self.trigger_death = '3'
        self.neutral_end = '''Преподавательница: ничего, я попробую найти инструкцию.
* Вы двигаетесь дальше.'''
        self.trigger_neutral_end = '4'
        self.question = '''Преподавательница: Мне нужно как можно скорее напечатать контрольные, но принтер, похоже, сломан...
1. Без проблем, технологии - моя стихия!
2. К нему где-то должна быть инструкция.
3. Я помогу! Давайте я приду сюда завтра в это же время
4. Извините, я не могу, я впервые такую шайтан-машину вижу.'''
        self.close_to_end_coef = 1
        self.have_we_met_before = 0
        self.level = 13
        self.artefact = 'Воронье перо'

class Seagull_Charmer(Character):
    def __init__(self):
        super().__init__()
        self.name = 'Заклинатель чаек'
        self.picture = ''
        self.hello = '''* Во дворе вы видите студента, подкармливающего чаек котлетами с макарошками. Кажется, это блюдо сегодня входит в бизнес-ланч. Вы слышите ворчание из своего живота.
Заклинатель чаек: Привет!'''
        self.goodbye = '''Ладно, давай! В конце концов, белое оперение не несёт в себе серьёзной угрозы, когда не сочетается с красными глазами.
''' 
        self.good_end = '''Заклинатель чаек: Хах, слушай, не советую есть комплекс. Но я могу поделиться с тобой купоном на десерт, мелочь, но лучше, чем ничего. Мне всё равно не нужен.
* Студент протягивает купон, на котором напечатан штрих-код и фраза "Дисерт Анна Павловна".'''
        self.trigger_good_end = '3'
        self.bad_end = '''Заклинатель чаек: Да, они знают команду "фас"!..Ой...
* Вас немного поклевали. До свадьбы заживёт.'''
        self.trigger_bad_end = '2'
        self.death = '''* Чайке, сидящей на вашей голове, фраза не понравилась. Кислота, содержащаяся в помёте птицы, разъедает ваш череп.
* Вы умираете.'''
        self.trigger_death = '1'
        self.neutral_end = '* Чайка, сидящая на вашей голове, улетает. Вы думаете, что этому пареню всё равно далеко до заклинателей крыс или голубей.'
        self.trigger_neutral_end = '4'
        self.question = '''* Одна чайка садится вам на голову.
1. Какие красивые! Только орут много.
2. Ты их дрессируешь?
3. *шутливо* М-м-м, с макаро-о-ошками... Я могу сойти за чайку?
4. *пройти мимо*'''
        self.close_to_end_coef = 1
        self.have_we_met_before = 0
        self.level = 14
        self.artefact = 'Купон на десерт'

class Zhenya(Character):
    def __init__(self):
        super().__init__()
        self.name = 'Женя'
        self.picture = ''
        self.hello = 'Привет! Не хочешь заполнить анкету?'
        self.goodbye = '''Мне пора!
'''
        self.good_end = '''Женя: Да, конечно. Пиши то, что считаешь нужным. 
* Вы проходите всю анкету, где-то отвечая честно, где-то основываясь на вашей придуманной специально для миссии личности, где-то отшучиваясь, а иногда пропуская поля для ответа совсем. Дописывая пожелания хозяйке анкеты, вы краем глаза замечаете фотографию мужчины с именем Максим Дΐ͈̘̟̰̞͢Ψ̧̗̰͖͉̙∆̢͓̣̙͕љ̧̲͚͔̣͔ẅ̡̮͓̠‰̢͇͉̗∆̧͍̥о̧̩̬в̞̭̮͇̰͢  '''
        self.trigger_good_end = '3'
        self.bad_end = '''Женя: зачем? Я... Ну... А разве?..
* Вы видите, как студентка надула губы и опустила голову. Она уходит как можно скорее.'''
        self.trigger_bad_end = '1'
        self.death = '''* Вы чувствуете удар тупым предметом по голове.
* Вы умерли.'''
        self.trigger_death = '4'
        self.neutral_end ='''* Вы проставили ответы на все вопросы, не тратя слишком много времени на обдумывание каждого и иногда приукрашивая.
* Женя благодарит вас и, шустро прочитав ваши ответы, советует вступить в студенческий совет. Вы отвечаете ей, что подумаете над предложением.'''
        self.trigger_neutral_end = '2'
        self.question = '''* Женя протягивает вам брошюрку, на обложке которой написано "Анкета для друзей".
1. Извини, тут есть вопросы слишком личные. Можно я не буду на них отвечать?
2. О, давно такие не видела! Давай.
3. А зачем?
4. *забрать брошюрку и начать листать*'''
        self.close_to_end_coef = 1
        self.have_we_met_before = 0
        self.level = 15
        self.artefact = 'technical_artifact_2'

class FGN_student(Character):
    def __init__(self):
        super().__init__()
        self.name = 'Студентка ФГН'
        self.picture = ''
        self.hello = '''Хей!
* Девушка, сидящая на скамейке, машет вам рукой.'''
        self.goodbye = '''До связи!
'''
        self.good_end = '''* Девушка многозначительно улыбается и подмигивает Вам.
Студентка ФГН: Хороший выбор. Мне нравится, что мы друг друга понимаем.
Студентка ФГН: Спасибо за помощь, правда. Я бы так и сидела, наверно. Лови.
* Вы хватаете в воздухе купон на бесплатную шаурму с фалафелем. Рассмотрев его и немного подумав, Вы решаете спросить о Белой Вороне.
* Студентка говорит, что знает только ФиЛин, но потом добавляет, что птицы держатся рядом.'''
        self.trigger_good_end = '1'
        self.bad_end = '''* Студентка понимающе кивает.
Студентка ФГН: Есть такое... Чёрт, я на пару опаздываю! И сама просидела, и тебя задержала, и так ничего и не выбрала. Ладно, спасибо.'''
        self.trigger_bad_end = '4'
        self.death = '''Студентка ФГН: Да, треш...
* Библиотечная книжка прилетает Вам прямо в висок. Всё.'''
        self.trigger_death = '3'
        self.neutral_end = '''* Студентка хмыкает.
Студентка ФГН: Если так подумать, не особо отличается от альтернативного варианта. Спасибо за помощь!'''
        self.trigger_neutral_end = '2'
        self.question = '''Студентка ФГН: Слушай, ты выглядишь как человек понимающий. 
* Вы вопросительно поднимаете бровь.
Студентка ФГН: Ну, знаешь, у тебя вайбы dark academia. И этот шоппер хорошо дополняет образ.
* Девушка кивает в сторону Бездонного Хранилища.
Студентка ФГН: У меня как раз проблема с шопперами. Не могу выбрать новый, рассматриваю их уже битый час. Принятие решений - не моя сильная сторона.
Студентка ФГН: Что думаешь? Girl in Red или HSE?
1. Girl in Red
2. HSE
3. Рюкзак
4. *сказать, что тоже не знаете*'''
        self.close_to_end_coef = 1
        self.have_we_met_before = 0
        self.level = 16
        self.artefact = 'Купон на шаурму'

class Booklets(Character):
    def __init__(self):
        super().__init__()
        self.name = 'Буклеты'
        self.picture = ''
        self.hello = '''Ну это просто невозможно!!!
* Вы наблюдаете странную картину. Перед Вами ожесточённо спорят два оживших буклета ОП "Фундаментальная и прикладная лингвистика".
Синий буклет: Посмотри на себя! Какие-то прямоугольники! Жалкое зрелище!
Фиолетовый буклет: Нет, ну знаешь что! Ты просто далёк от минимализма.
* Вы кашляете для привлечения внимания.
Буклеты: О, привет, человек. Ты-то нам и нужен.'''
        self.goodbye = '''*прощальное шуршание бумаги*
'''
        self.good_end = '''
* Вы читаете продолжительную лекцию о том, почему оба дизайна имеют свои плюсы и минусы.
* Буклеты выглядят уставшими и заскучавшими, но убеждёнными. Они уже не настроены враждебно.
Синий буклет: Да, что-то я погорячился, брат.
Фиолетовый буклет: Да и я, старичок. Ведь не важно, что снаружи.
Синий буклет: Важно, что...
Буклеты: ...внутри! А внутренний мир у нас общий.
* Буклеты примирительно шелестят страницами и прыгают вам в руки, замолкая и замирая.
* Возможно, вам это всё показалось. Надо больше спать. В любом случае, Вы получили новый артефакт.
* На форзаце Фиолетового буклета вы замечаете небрежные карандашные записи. Вам удаётся разобрать только два слова: "Белая Ворона".'''
        self.trigger_good_end = '3'
        self.bad_end = '''* Фиолетовый буклет торжествует. Синий буклет выглядит обиженным.
Синий буклет: Ну... Ладно, это неприятно, но я тут в меньшинстве.
Синий буклет косится на стенд с буклетами позади Вас.
Синий буклет: Люди ничего не понимают в искусстве.
* Спор разрешён, но какой ценой?'''
        self.trigger_bad_end = '1'
        self.death = '''* Синий буклет радостно смеётся, но тут же замолкает со звуком рвущейся бумаги.
* Последнее, что Вы видите - взбешённая обложка Фиолетового буклета и десятки его клонов, летящие на Вас со стенда за Вашей спиной.
* Смерть от сотен бумажных порезов наступает мгновенно.'''
        self.trigger_death = '2'
        self.neutral_end = '''* Буклеты выглядят немного раздосадованными.
Буклеты: Ладно, иди, человек. Подождём ещё кого-нибудь.
* Вы разворачиваетесь, слыша, что спор продолжается.'''
        self.trigger_neutral_end = '4'
        self.question = '''Буклеты: У нас тут разногласия. Вот, решаем, чей дизайн лучше. Разреши спор, а?
1. *выбрать фиолетовый буклет*
2. *выбрать синий буклет*
3. *сказать, что оба дизайна хороши*
4. *сказать, что ничего не понимаете в дизайне*'''
        self.close_to_end_coef = 1
        self.have_we_met_before = 0
        self.level = 17
        self.artefact = 'Два Буклета ОП "Фундаментальная и прикладная лингвистика"'

class Cleaner(Character):
    def __init__(self):
        super().__init__()
        self.name = 'Уборщица'
        self.picture = ''
        self.hello = '''Здравствуйте.
* Бабушка со шваброй приветливо Вам улыбается.'''
        self.goodbye = '''До свидания.
'''
        self.good_end = '''* Вы киваете, быстро поднимаетесь и берёте ведро по бокам.
* Спускаясь, Вы замечаете, что ручка ведра едва держится. Передавая ведро уборщице, Вы предупреждаете её об этом.
Уборщица: Спасибо Вам большое! Извините, что отвлекла, мне так неловко, так неловко...
Уборщица: Вот, возьмите в знак благодарности.
* Бабушка протягивает Вам маленького вязаного воронёнка.
* Перед тем, как уйти, Вы решаете спросить, не замечала ли она чего-то необычного в последнее время.
* Уборщица оглядывается по сторонам и загадочно говорит, что по воскресеньям перья белеют.'''
        self.trigger_good_end = '2'
        self.bad_end = '''* Вы проноситесь вверх по лестнице, делая вид, что торопитесь на пару.
* Вежливая полуулыбка сходит с лица уборщицы. Её сменяет грусть.'''
        self.trigger_bad_end = '4'
        self.death = '''* Вы киваете, быстро поднимаетесь и берёте ведро за ручку.
* Ручка со щелчком отрывается, ведро падает Вам на ногу, вода разливается по лестнице. Вы поскальзываетесь на первой же ступеньке сверху.
* Прокатившись кубарем вниз, Вы ударяетесь головой прямо о край ступеньки. Мир вмиг темнеет.'''
        self.trigger_death = '1'
        self.neutral_end = '''* Вы окликаете студента, проходящего мимо, быстро объясняя ситуацию и делая вид, что торопитесь на пару.
* Студент соглашается и поднимается за ведром. Что-то внутри Вас заставляет сказать студенту обратить внимание на ручку ведра. 
* Уборщица благодарно смотрит вам двоим вслед.'''
        self.trigger_neutral_end = '3'
        self.question = '''Уборщица: Мне так неловко просить, но не могли бы Вы помочь мне?
Уборщица: Там на пролёт выше стоит моё ведро, а у меня в спину вступило. Годы, мои годы...
Уборщица: Мне правда так неловко. Это же моя работа. Но не могли бы Вы подать мне ведро? Оно совсем не тяжёлое.
1. *согласиться и взять ведро за ручку*
2. *согласиться и взять ведро по бокам*
3. *сделать вид, что торопитесь на пару, и попросить помочь проходящего мимо студента*
4. *сделать вид, что торопитесь на пару, и проигнорировать просьбу*'''
        self.close_to_end_coef = 1
        self.have_we_met_before = 0
        self.level = 18
        self.artefact = 'Вязаный воронёнок'

class Timur(Character):
    def __init__(self):
        super().__init__()
        self.name = 'Т. Мур'
        self.picture = ''
        self.hello = '''Ой! Я и не заметил, как ты подошла.
Т. Мур: Меня все Т. Мур зовут. А тебя?
* Вы представляетесь.
Т. Мур: Приятно познакомиться!'''
        self.goodbye = '''Удачи!'''
        self.good_end = '''Т. Мур: Самолётик? Хехе, хороший выбор!
* Вы вспоминаете, как в детстве складывали с мамой космические кораблики из каменной бумаги.
* Вы с лёгкостью сворачиваете лист в незамысловатый трансгалактический шаттл.
Т. Мур: Ого! Я... не видел таких самолётиков раньше.
Т. Мур: Слушай, не хочешь обменяться? Ты мне самолётик, а я тебе... вот.
Т. Мур протягивает Вам бумажный кинжал с рукояткой в форме головы вороны. Вы соглашаетесь на обмен.
* Вы замечаете, что цифры с распечатки, из которой был сложен кинжал, складываются на клюве в "125 10:00".'''
        self.trigger_good_end = '2'
        self.bad_end = '''* Т. Мур улыбается Вашему выбору.
* К сожалению, Ваших знаний о внешнем виде птиц средней полосы России недостаточно. Сложить ворону не получается.
* Вы пытаетесь исправить ситуацию. В конце концов, тонкая бумага рвётся.
Т. Мур: Эх! Ну ничего страшного.'''
        self.trigger_bad_end = '1'
        self.death = '''* Вы отказываетесь, утверждая, что уже переросли возраст, когда складывать оригами было весело.
* Прежде, чем Вы успеваете осознать возможные последствия Вашего ответа, бумажный кинжал вонзается Вам в горло.'''
        self.trigger_death = '4'
        self.neutral_end = '''* Вы вежливо отказываетесь.
Т. Мур: Что ж! Тогда в другой раз.'''
        self.trigger_neutral_end = '3'
        self.question = '''Т. Мур: Слушай, я тут оригами занимаюсь, но мне одному уже скучновато стало. Не хочешь присоединиться?
Т. Мур: Только у меня всего один лист бумаги остался, так что придётся быть аккуратнее.
1. *согласиться и попробовать сложить ворону*
2. *согласиться и попробовать сложить самолётик*
3. *вежливо отказаться*
4. *не очень вежливо отказаться*'''
        self.close_to_end_coef = 1
        self.have_we_met_before = 0
        self.level = 19
        self.artefact = 'Бумажный кинжал'

class Strange_group(Character):
    def __init__(self):
        super().__init__()
        self.name = 'Безымянная группа'
        self.picture = ''
        self.hello = '''Вот и ты.
* Это было сказано тихо. Скорее всего, группа не надеялась, что Вы это услышите.'''
#……………………………………*ОПИСАНИЯ НАС ДЕВАЧЬКИ*……………………………………….
        self.goodbye = '''Счастливого пути! И привет Совету.
'''
        self.good_end = '''* Вам и правда не составляет труда объяснить группе, что да как в GitHub.
* Одна из девушек протягивает Вам тонкую книжечку "Тайны ФГН". Наспех пролистав страницы, Вы замечаете, что задача, предлагающая спеть хотя бы два куплета "Gaudeamus", жирно обведена красным.
* Девушки замечают Ваше удивление и улыбаются. Что-то вам подсказывает, что пора повторить латынь.'''
        self.trigger_good_end = '1'
        self.bad_end = ''
        self.trigger_bad_end = ''
        self.death = ''
        self.trigger_death = ''
        self.neutral_end = '''* Девушки пожимают плечами и возвращаются к изучению сайта.
* Уходя, вы слышите слова, брошенные Вам вслед.
Безымянная группа: Будь осторожен!'''
        self.trigger_neutral_end = '2'
        self.question = '''Безымянная группа: Нам тут помощь нужна небольшая. Надо с GitHub разобраться, за это плюсики обещали.
* Вы думаете, что у землян-вышкинцев странная форма поощрения. Вы решаете, что "плюсики" нужны для искусственного улучшения навыков индивида. Откуда вам знать, что не всё сделано из кода?
Безымянная группа: Всё хорошо, можешь не помогать, ты выглядишь уставшим. Но у нас такое чувство, что ты в этом много понимаешь.
Безымянная группа: ...
Безымянная группа: И, возможно, мы сможем помочь в ответ.
1. *согласиться*
2. *не соглашаться*'''
        self.close_to_end_coef = 1
        self.have_we_met_before = 0
        self.level = 20
        self.artefact = 'Книжечка "Тайны ФГН"'
