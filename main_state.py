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
player_tengo=None
game_time = None
player_turn_image = None
monster_turn_image = None
card_draw = True
card_check_count = 0
monster_attck_end = 0
monster_die_check = True
monster_die_count = 3
monster_die_check_end=False
player_turn_start=False
def enter():
    global grass, map, curser, player_tengo, main_handle_event, turn_end_button, player_turn_image, monster_turn_image
    map = load_image('background_file\\Map1.png')
    grass = load_image('background_file\\grass2.png')
    curser = load_image('curser.png')


    main_handle_event = main_handle_event_class.Main_handle_event()
    player_tengo = player_tengo_class.Tengo() #플레이어
    game_world.add_object(player_tengo, 1)

    turn_end_button = turn_state.Trun_end() #턴종료
    game_world.add_object(turn_end_button, 0)


    player_turn_state.player_turn_enter()
    player_turn_image = player_turn_state.Player_turn_image()
    game_world.add_object(player_turn_image, 0)

    monster_turn_state.monster_slime_turn_enter()
    monster_turn_image = monster_turn_state.Monster_turn_image()
    game_world.add_object(monster_turn_image, 0)

def exit():
    global map,curser,grass
    del(map)
    del(curser)
    del(grass)

def pause():
    pass


def resume():
    pass


def handle_events():
    main_handle_event.handle_events()


def on_mouse_up(mouse_pos):
    print('on_mouse_up')
    player_turn_state.player_turn(mouse_pos)


def player_turn_end(mouse_pos):
    global card_draw, card_check_count,player_turn_start
    print('player_turn_end')
    if turn_end_button.trun_image_coflict_check(mouse_pos) and not turn_end_button.turn_owner == turn_end_button.monster_turn:
        turn_end_button.previous_turn_count = turn_end_button.player_turn  # 이전 턴은 플레이어 턴이였다.
        turn_end_button.turn_owner_state()
        print("시작")

        player_turn_state.card_count=0
        while player_turn_state.card_count<len(player_turn_state.card_list):
            print("class_while")
            if len(player_turn_state.card_list)>=1:
                game_world.remove_object(player_turn_state.card_list[player_turn_state.card_count])
                player_turn_state.card_list.pop(0)
            if len(player_turn_state.cost_list) >= 1:
                game_world.remove_object(player_turn_state.cost_list[player_turn_state.cost_count])
                player_turn_state.cost_list.pop(0)
            else:
                pass


        card_draw = False
        player_turn_start=True
        turn_end_button.turn_owner = turn_end_button.monster_turn
        print("종료")

def monster_turn_end():
    global card_draw,player_turn_start
    monster_turn_state.monster_action_count=0
    player_turn_state.player_turn_enter()
    player_turn_image = player_turn_state.Player_turn_image()
    game_world.add_object(player_turn_image, 0)
    player_turn_start=False
    turn_end_button.previous_turn_count = turn_end_button.monster_turn
    turn_end_button.turn_owner_state()

    turn_end_button.turn_owner = turn_end_button.player_turn
    player_turn_state.player_turn(main_handle_event_class.Main_handle_event().mouse_point)

    card_draw = True

def update():
    global monster_attck_end
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
