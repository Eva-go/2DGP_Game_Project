import random
import json
import os

from pico2d import *
import game_framework
import Title_state
from player_file import player_tengo_class
from monseter_file import monster_slime_class
from card_file import card_list_class

mouse_x, mouse_y = 1366 / 2, 768 / 2
card_list_move = False

card_list = []

def enter():
    global grass, map, curser, player_tengo, monster_slimes, card_list
    map = load_image('background_file\\Map1.png')
    grass = load_image('background_file\\grass2.png')
    curser = load_image('curser.png')

    player_tengo = player_tengo_class.Tengo()

    monster_slimes = []
    for m in range(0, random.randint(1, 5), 1):
        monster_slimes.append(monster_slime_class.Slime(m))


    for c in range(0, 5, 1):
        rand = random.randint(1, 2)
        if rand == 1:
            card_list.append(card_list_class.Card_Attack(c))
        elif rand == 2:
            card_list.append(card_list_class.Card_Shield(c))


def exit():
    global grass, map, curser, player_tengo, monster_slimes, card_list
    del (grass)
    del (map)
    del (curser)
    del (player_tengo)
    del (monster_slimes)
    del (card_list)


def pause():
    pass


def resume():
    pass


def handle_events():
    global mouse_x, mouse_y, card_list_move
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(Title_state)
        elif event.type == SDL_MOUSEMOTION:
            mouse_x, mouse_y = event.x, 768 - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if mouse_x >= 325 and mouse_y >= 30 and mouse_x <= 475 and mouse_y <= 210:
                card_list_move = True

        elif event.type == SDL_MOUSEBUTTONUP:
            if card_list_move == True:
                # del(card_list[0])
                card_list.pop(0)
                print(card_list)
                card_list_move = False



def update():
    global card_list,mouse_x, mouse_y
    show_cursor()

    player_tengo.update()

    for slime in monster_slimes:
        slime.update()
    if card_list_move == True:
        card_list[0].update(mouse_x,mouse_y)


def draw():
    global mouse_x, mouse_y
    clear_canvas()
    map.draw(683, 384)
    grass.draw(683, 150)

    player_tengo.draw()
    for slime in monster_slimes:
        slime.draw()

    for card in card_list:
        card.draw()

    curser.draw(mouse_x, mouse_y)
    update_canvas()
