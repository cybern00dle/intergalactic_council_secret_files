from lib.character import Character
import lib.scenes as sc
#девочки, не забываем импортировать сюда своих персонажей, а также добавлять их в два списка ниже
from lib.characters import The_clone, Talking_pie, The_lost_child, Wicket, Predatory_plant

#создаем словарь с характеристиками игрока. считаем, что в начале он не мертв, и у него одно очко, список артефактов пуст
player = {'close_to_end_index': 1, 'player_is_dead': 0, 'artefacts' : []}

#выводим приветственный текст. пока игрок не выберет "начать", выводим его снова и снова.
hello_text = 'добро пожаловать в текстовый квест про колобка!\nчтобы выбрать действие, введите с клавиатуры цифру, под которой написано желаемое действие.\n\n1. Начать.\n2. Повторить правила'
answer = ''
while answer != '1':
    print(hello_text)
    answer = input('->')

#создаем список с персонажами. дальше пойдем в цикле по элементам списка(пока подряд, но потом придумаем механизм с уровнем)    
character_list = [The_clone(), Talking_pie(), The_lost_child(), Wicket(), Predatory_plant()]
stop=False
while stop == False:
    for character in character_list:
        if character == character_list[-1]:
            stop = True
        #пока персонажи идут подряд, цикл прерывается, когда мы доходим до последнего персонажа.
        # Алёна, твоя задача!!! - Написать функцию - алгоритм выбора следующего персонажа, основываясь на коэффициенте близости игрока к концу и уровне персонажа. 
        # Можно же проходиться по элементам списка в цикле и выбирать персонажа, который соответсвует нам по уровню. 
        if character.have_we_met_before == 0:
            res = sc.one_character_scene(character, hello_text, player)
            if res == 1:
                stop = True
                break
            elif res == 2:
                stop == False
                player['player_is_dead']=0
                player['close_to_end_index'] = 1
                character_list = [The_clone(), Talking_pie(), The_lost_child(), Wicket(), Predatory_plant()]
                break

#функция, которая подсчитывает собранные артефакты, показывает их игроку и решает, как собранные артефакты повлияют на бой с боссом
def artefacts_collection(player):
    final_artefacts = [value for value in player['artefacts'] if value != '']
    artefacts_number = len(final_artefacts)
    i = input('Кажется, все разошлись по домам. В вышке никого не осталось. Вы решаете собраться с мыслями и замечаете, что ваша сумка стала очень тяжелой.\n\n1. Открыть сумку и посмотреть, что внутри\n2. Выбросить сумку.\n->')
    if i == '1' and final_artefacts != []:
        print('в вашей сумке вы находите: ', final_artefacts, '\nСохраните на будущее. Вдруг пригодится.')
    elif i == '1' and final_artefacts == []:
        print('Это не сумка тяжелая, а вы устали.')
    else:
        print('Странное решение. Но как хотите.')
    if artefacts_number > 10 or artefacts_number == 10:
        artefacts_result = 'good'
    elif artefacts_number < 10 and artefacts_number > 5:
        artefacts_result = 'bad'
    else:
        artefacts_result = 'verybad'
    return(artefacts_number, artefacts_result)
   
result_for_final_fight = artefacts_collection(player)
#количество артефактов
artefacts_number = result_for_final_fight[0]
#строка good, bad, verybad для определение концовки
artefacts_result = result_for_final_fight[1]

# Настя! здесь нужно написать и вызвать функцию битвы с боссом. используй artefacts_result, чтобы узнать об артефактах
