#player turn state 플레이어 턴->행동->몬스터 턴-> 행동 반복
from pico2d import *
from monseter_file import monster_slime_class
from turn_file import turn_state
import game_world
import main_state
monster_slimes=[]
monster_turn=False
monster_action_count=0
monster_die_count=2
class Monster_turn_image():
    image = None

    def __init__(self):
        self.x, self.y = 650, 650
        if self.image == None:
            self.image = load_image('turn_file\\enemy_turn.png')

    def update(self):
        if main_state.turn_end_button.turn_owner == main_state.turn_end_button.monster_turn:
            self.image.draw(self.x, self.y)

    def draw(self):
        if main_state.turn_end_button.turn_owner ==main_state.turn_end_button.monster_turn:
            self.image.draw(self.x, self.y)


def monster_slime_turn_enter():
    #print("monster_slime_turn_enter")
    global  monster_slimes
    for monsters in range(3):
        monster_slimes.append(monster_slime_class.Slime(monsters))
    game_world.add_objects(monster_slimes, 1)  #몬스터 숫자



def monster_slime_turn():
    pass