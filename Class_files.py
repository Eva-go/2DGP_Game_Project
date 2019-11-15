import random
import json
import os

from pico2d import *
import game_framework
import Title_state
from player_file import player_tengo_class
from monseter_file import monster_slime_class
from card_file import card_list_class
from handle_event import main_handle_event_class
#mouse_x, mouse_y = 1366 / 2, 768 / 2


card_list = []
monster_slimes = []

def enter():
    global grass, map, curser, player_tengo, monster_slimes, card_list,main_handle_event
    map = load_image('background_file\\Map1.png')
    grass = load_image('background_file\\grass2.png')
    curser = load_image('curser.png')

    player_tengo = player_tengo_class.Tengo()
    main_handle_event= main_handle_event_class.Main_handle_event()

    for m in range(0, random.randint(1, 5), 1):
        monster_slimes.append(monster_slime_class.Slime(m))


    for c in range(0, 5, 1):
        rand = random.randint(1, 2)
        if rand == 1:
            card_list.append(card_list_class.Card_Attack(c))
        elif rand == 2:
            card_list.append(card_list_class.Card_Shield(c))


def exit():
    global grass, map, curser, player_tengo, monster_slimes, card_list,main_handle_event
    del (grass)
    del (map)
    del (curser)
    del (player_tengo)
    del (monster_slimes)
    del (card_list)
    del (main_handle_event)


def pause():
    pass


def resume():
    pass


def handle_events():
    main_handle_event.handle_events()

# 마우스가 때면 main_handle_event_class 에서 불러줌
def on_mouse_up(mouse_pos):
    i = 0;
    while i < len(card_list):
        if card_list[i].card_conflict_check(mouse_pos):
            del card_list[i]


        else:
            i += 1

#여기서 카드 움직임(제작 불가)
def on_mouse_down(mouse_pos):
    i = 0;
    while i < len(card_list):
        if card_list[i].card_conflict_check(mouse_pos):
            card_list[i].update(mouse_pos)
        else:
            i += 1



#여기서 어떻게 check가 false로 바꿀수 있는가.

def update():
    global card_list
    show_cursor()

    player_tengo.update()

    for slime in monster_slimes:
        slime.update()

        #card_list.pop(0)
        #main_handle_event_class.card_list_move=False

def draw():
    clear_canvas()
    map.draw(683, 384)
    grass.draw(683, 150)

    player_tengo.draw()
    for slime in monster_slimes:
        slime.draw()

    for card in card_list:
        card.draw()

    curser.draw(main_handle_event.mouse_x,main_handle_event.mouse_y)
    update_canvas()
