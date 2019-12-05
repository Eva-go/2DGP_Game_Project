from pico2d import *
import Class_files
from card_file import card_list_class
from cost_file import cost
import game_world
import random
from turn_file import turn_state

card_count=0
card_list = []
cost_list = []
cost_count = 0

tengo_attack = False
tengo_shield = False
image=None
lode_time=0.0
your_turn=False
def enter():
    global image
    image = load_image('turn_file\\Your_turn.png')

def update():
    global image
    if turn_state.Trun_end().turn_owner == turn_state.Trun_end().player_turn:
        image.draw(783,367)
def draw():
    global image
    if turn_state.Trun_end().turn_owner == turn_state.Trun_end().player_turn:
        image.draw(783,367)


def player_turn_enter():
    global card_list

    for counting in range(3):
        cost_list.append(cost.Game_cost(counting))
    game_world.add_objects(cost_list, 1)

    for c in range(5):
        rand = random.randint(1, 2)
        if rand == 1:
            card_list.append(card_list_class.Card_Attack(c))
        elif rand == 2:
            card_list.append(card_list_class.Card_Shield(c))
    game_world.add_objects(card_list, 1)

def player_turn(mouse_pos):
    global tengo_attack, tengo_shield, card_list_del,cost_count,card_count
    card_count = 0
    if turn_state.Trun_end().turn_owner == turn_state.Trun_end().player_turn:
        turn_state.Trun_end().turn_owner
        while card_count < len(card_list):
         if card_list[card_count].card_conflict_check(mouse_pos):
             card_list_del = True

             if card_list[card_count].type() == card_list_class.CARD_ATTACK:
                 tengo_attack = True
             elif card_list[card_count].type() == card_list_class.CARD_SHIELD:
                 tengo_shield = True
             card_tem = card_list[card_count]
             card_list.remove(card_tem)
             #cost_count +=1
             if tengo_attack and not tengo_shield:
                 cost_tem = cost_list[-1]
                 cost_list.remove(cost_tem)
                 game_world.remove_object(cost_tem)
             elif tengo_shield and not tengo_attack:
                 cost_tem = cost_list[-1]
                 cost_list.remove(cost_tem)
                 game_world.remove_object(cost_tem)
             else:
                 tengo_attack = False
                 tengo_shield = False

             game_world.remove_object(card_tem)
             if Class_files.turn_end_button.trun_image_coflict_check(mouse_pos):
                 pass
                 #for i in len(card_list):
                    #game_world.remove_object(i+1)
             pass


         else:
             card_count +=1

