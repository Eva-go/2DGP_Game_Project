import random
import json
import os
import game_world
from pico2d import *

from player_file import player_tengo_class
from card_file import card_list_class
from handle_event import main_handle_event_class
from monseter_file import monster_slime_class
from cost_file import cost
from turn_file import turn_state
from turn_file import player_turn_state
# mouse_x, mouse_y = 1366 / 2, 768 / 2



monster_slimes = []
card_list_del = False



def enter():
    global grass, map, curser, player_tengo, monster_slimes, main_handle_event,turn_end_button
    map = load_image('background_file\\Map1.png')
    grass = load_image('background_file\\grass2.png')
    curser = load_image('curser.png')

    player_tengo = player_tengo_class.Tengo()
    main_handle_event = main_handle_event_class.Main_handle_event()
    game_world.add_object(player_tengo, 1)

    turn_end_button = turn_state.Trun_end()
    game_world.add_object(turn_end_button, 1)


    monster_slimes = [monster_slime_class.Slime(slime) for slime in range(3)]
    game_world.add_objects(monster_slimes, 1)

    player_turn_state.player_enter()
    # cost_count = [cost.Game_cost(Counting) for Counting in range(3)]




def exit():
    global grass, map, curser, player_tengo, monster_slimes, main_handle_event
    del (grass)
    del (map)
    del (curser)
    del (player_tengo)
    del (monster_slimes)
    del (main_handle_event)



def pause():
    pass


def resume():
    pass


def handle_events():
    main_handle_event.handle_events()


# 마우스가 때면 main_handle_event_class 에서 불러줌
def on_mouse_up(mouse_pos):
    player_turn_state.player_turn(mouse_pos)

def turn_end_up(mouse_pos):
    if turn_end_button.trun_image_coflict_check(mouse_pos):
        print("턴종료")




def update():
    show_cursor()

    for game_object in game_world.all_objects():
        game_object.update()


def draw():
    clear_canvas()
    map.draw(683, 384)
    grass.draw(683, 150)

    for game_object in game_world.all_objects():
        game_object.draw()

    curser.draw(main_handle_event.mouse_x, main_handle_event.mouse_y)
    update_canvas()
