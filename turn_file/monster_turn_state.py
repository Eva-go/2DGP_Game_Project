#player turn state 플레이어 턴->행동->몬스터 턴-> 행동 반복
from pico2d import *
from monseter_file import monster_slime_class
import game_world

monster_slimes=[]
monster_turn=False
def monster_slime_turn_enter():
    global  monster_slimes
    monster_slimes = [monster_slime_class.Slime(slime) for slime in range(3)]
    game_world.add_objects(monster_slimes, 1)


def monster_slime_turn():
    pass