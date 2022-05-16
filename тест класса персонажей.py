from lib.character import Character
import lib.scenes as sc
from lib.characters import Hare, Fox

#создаем словарь с характеристиками игрока. считаем, что в начале он не мертв, и у него одно очко, список артефактов пуст
player = {'close_to_end_index': 1, 'player_is_dead': 0, 'artefacts' : []}

#выводим приветственный текст. пока игрок не выберет "начать", выводим его снова и снова.
hello_text = 'добро пожаловать в текстовый квест про колобка!\nчтобы выбрать действие, введите с клавиатуры цифру, под которой написано желаемое действие.\n\n1. Начать.\n2. Повторить правила'
answer = ''
while answer != '1':
    print(hello_text)
    answer = input('->')

#создаем список с персонажами. дальше пойдем в цикле по элементам списка(пока подряд, но потом придумаем механизм с уровнем)    
character_list = [Hare(), Fox()]
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
                character_list = [Hare(), Fox()]
                break

def artefacts_collection(player):
    if len(player['artefacts']) > 10:
        artefacts_result = 'good'
    elif len(player['artefacts']) < 10:
        artefacts_result = 'bad'
    return(artefacts_result)

# Настя! здесь нужно написать и вызвать функцию битвы с боссом. используй artefacts_result, чтобы узнать об артефактах