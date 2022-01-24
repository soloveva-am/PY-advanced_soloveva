# coding: utf-8
# license: GPLv3
from enemies import *
from hero import *

def annoying_input_int(message =''):
    answer = None
    while answer == None:
        insert=input(message)
        try:
            answer = int(insert)
        except ValueError:
            if insert == 'Run Away':
                answer = 'Run Away'
            elif insert == 'Give Up':
                answer = 'Give Up'
            else: print('Вы ввели недопустимые символы')
    return answer


def game_tournament(hero, dragon_list):
    for dragon in dragon_list:
        print('Вышел', dragon._color, 'дракон!')
        while dragon.is_alive() and hero.is_alive():
            print('Вопрос:', dragon.question())
            answer = annoying_input_int('Ответ:')

            if dragon.check_answer(answer)== 'Verno':
                hero.attack(dragon)
                print('Верно! \n** дракон кричит от боли **')
            elif dragon.check_answer(answer)== 'Neverno':
                dragon.attack(hero)
                print('Ошибка! \n** вам нанесён удар... **')
            elif dragon.check_answer(answer)=='Give Up':
                hero.Give_Up
            elif dragon.check_answer(answer)=='Run Away':
                if hero.class != 'Wizard':
                    dragon.attack(hero)
                continue
        if dragon.is_alive():
            break
        print('Дракон', dragon._color, 'повержен!\n')
        hero._experience+=10
        print ('вы получили опыт')

    if hero.is_alive():
        print('Поздравляем! Вы победили!')
        print('Ваш накопленный опыт:', hero._experience)
    else:
        print('К сожалению, Вы проиграли...')

def start_game():

    try:
        print('Добро пожаловать в арифметико-ролевую игру с драконами!')
        print('выберите класс: Fighter, Wizard, Rogue')
        cl=input()
        print('Представьтесь, пожалуйста: ', end='')
        name = input()
        if cl=='Wizard':
            hero = Wizard(name)
        elif cl=='Rogue':
            hero=Rogue(name)
        else: hero = Fighter (name)

        hero = Hero(input())

        dragon_number = 3
        dragon_list = generate_dragon_list(dragon_number)
        assert(len(dragon_list) == 3)
        print('У Вас на пути', dragon_number, 'драконов!')
        game_tournament(hero, dragon_list)

    except EOFError:
        print('Поток ввода закончился. Извините, принимать ответы более невозможно.')
