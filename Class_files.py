import random
import json
import os
import game_world
import game_framework
from pico2d import *

from player_file import player_tengo_class
from handle_event import main_handle_event_class

from turn_file import turn_state
from turn_file import player_turn_state
from turn_file import monster_turn_state

# mouse_x, mouse_y = 1366 / 2, 768 / 2

card_list_del = False
turn_end_button = None
game_time=None

def enter():
    global grass, map, curser, player_tengo, main_handle_event, turn_end_button
    map = load_image('background_file\\Map1.png')
    grass = load_image('background_file\\grass2.png')
    curser = load_image('curser.png')

    player_tengo = player_tengo_class.Tengo()
    main_handle_event = main_handle_event_class.Main_handle_event()
    game_world.add_object(player_tengo, 1)

    turn_end_button = turn_state.Trun_end()
    game_world.add_object(turn_end_button, 1)

    player_turn_state.player__turn_enter()
    monster_turn_state.monster_slime_turn_enter()
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


def on_mouse_up(mouse_pos):
    player_turn_state.player_turn(mouse_pos)


def player_turn_end(mouse_pos):
    if turn_end_button.trun_image_coflict_check(mouse_pos):
        turn_end_button.turn_owner = turn_end_button.none_turn
    turn_end_button.previous_turn_count = turn_end_button.player_turn

def monster_turn_end():
    turn_end_button.turn_owner = turn_end_button.none_turn
    turn_end_button.previous_turn_count = turn_end_button.monster_turn

def none_turn_end():
    global game_time
    game_time = game_framework.frame_time % 4
    if turn_end_button.previous_turn_count == turn_end_button.player_turn:
        if game_time>3.0:
            turn_end_button.previous_turn_count=turn_end_button.monster_turn
    elif turn_end_button.previous_turn_count == turn_end_button.monster_turn:
        if game_time>3.0:
            turn_end_button.previous_turn_count=turn_end_button.player_turn



def update():
    show_cursor()
    # player_turn_state.update()
    for game_object in game_world.all_objects():
        game_object.update()


def draw():
    clear_canvas()
    map.draw(683, 384)
    grass.draw(683, 150)
    # player_turn_state.draw()

    for game_object in game_world.all_objects():
        game_object.draw()

    curser.draw(main_handle_event.mouse_x, main_handle_event.mouse_y)
    update_canvas()
