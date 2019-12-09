from pico2d import *
import main_state
from card_file import card_list_class
from cost_file import cost
import game_world
import random
from turn_file import turn_state
from handle_event import main_handle_event_class
card_count = 0
card_list = []
cost_list = []
cost_count = 0
card_draw_list = 0
tengo_attack = False
tengo_shield = False
monster_hit = False

class Player_turn_image():
    image = None

    def __init__(self):
        self.x, self.y = 650, 650
        if self.image == None:
            self.image = load_image('turn_file\\Your_turn.png')

    def update(self):
        if main_state.turn_end_button.turn_owner == main_state.turn_end_button.player_turn:
            self.image.draw(self.x, self.y)

    def draw(self):
        if main_state.turn_end_button.turn_owner == main_state.turn_end_button.player_turn:
            self.image.draw(self.x, self.y)


def player_turn_enter():
    global card_list, card_draw_list
    print('player_turn_enter')
    for counting in range(5):
        cost_list.append(cost.Game_cost(counting))
    game_world.add_objects(cost_list, 1)#코스트

    for card_draw_list in range(5):
        # del(card_list_class.Card_Attack(card_draw_list).image)
        # del(card_list_class.Card_Shield(card_draw_list).image)
        rand = random.randint(1, 2)
        if rand == 1:
            card_list.append(card_list_class.Card_Attack(card_draw_list))
        elif rand == 2:
            card_list.append(card_list_class.Card_Shield(card_draw_list))
    game_world.add_objects(card_list, 1)#카드


def player_turn(mouse_pos):
    global tengo_attack, tengo_shield, card_count
    card_count = 0

    if main_state.turn_end_button.turn_owner==main_state.turn_end_button.player_turn:
        while card_count < len(card_list):

            if card_list[card_count].card_conflict_check(mouse_pos):
                if card_list[card_count].type() == card_list_class.CARD_ATTACK:

                    tengo_attack = True
                elif card_list[card_count].type() == card_list_class.CARD_SHIELD:

                    tengo_shield = True

                card_tem = card_list[card_count]
                card_list.remove(card_tem)
                # cost_count +=1
                if tengo_attack and not tengo_shield:
                    cost_tem = cost_list[-1]
                    # if len(cost_tem) > len(cost_list):
                    cost_list.remove(cost_tem)
                    game_world.remove_object(cost_tem)
                elif tengo_shield and not tengo_attack:
                    cost_tem = cost_list[-1]
                    # if len(cost_tem)>len(cost_list):
                    cost_list.remove(cost_tem)
                    game_world.remove_object(cost_tem)
                else:

                    tengo_attack = False
                    tengo_shield = False

                game_world.remove_object(card_tem)
            else:

                card_count += 1
