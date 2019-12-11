from pico2d import *
import random
import game_framework
import main_state
import game_world
from turn_file import monster_turn_state
from turn_file import player_turn_state
from player_file import player_tengo_class
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 7

monster_get_hit = 0

class Slime:

    def __init__(self, slime_point):
        self.x, self.y = 866 + 100 * slime_point, 300
        self.frame = random.randint(0, 6)
        self.num=slime_point
        self.hp=20
        self.font=load_font('resource_file\\Maplestory Light.TTF',20)
        self.slime_attack_damage = 15
        self.sleep = Animation('monseter_file\\slime_sleep.png',6,200,200)
        self.attack = Animation('monseter_file\\slime_attck.png',20,200,200)
        self.die = Animation('monseter_file\\slime_die.png',31,200,200)
        self. image_count = 0
        self.image = self.sleep
        self.monster_attack=False
        self.attack_count=0

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 7

        if main_state.turn_end_button.turn_owner == main_state.turn_end_button.monster_turn: #현제 턴이 몬스터 턴일때?
            check_monster_attack=False
            #self.image_count=0
            self.image_count = (self.image_count + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time)
            self.image_count = self.image_count % 21
            for m in monster_turn_state.monster_slimes:
                m.image = self.attack
                self.attack_count+=1
            if self.attack_count>=3 and self.image_count >=20.0:
                for m in monster_turn_state.monster_slimes:
                    m.image = self.sleep
                    main_state.player_tengo.hp -= self.slime_attack_damage
                    self.image_count = 0
                self.attack_count=0
                main_state.monster_turn_end()



       # if player_turn_state.tengo_attack:
            #monster_turn_state.monster_slimes[monster_get_hit].image = self.die
            #self.image_count = (self.image_count + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 32
            #if player_turn_state.tengo_attack==False:
                #monster_turn_state.monster_slimes[monster_get_hit].image = self.sleep
                #self.image_count=0
          #  player_turn_state.monster_hit = False

        if main_state.turn_end_button.turn_owner == main_state.turn_end_button.player_turn:
            if monster_turn_state.monster_slimes[0].hp == 0 and main_state.monster_die_check==True:
                main_state.monster_die_check = False
                main_state.monster_die_count-=1
                monster_turn_state.monster_slimes[0].hp = 20
                if len(monster_turn_state.monster_slimes)>0: #몬스터 숫자가 0마리 이상일때
                    monster_die = monster_turn_state.monster_slimes[-1]
                    monster_turn_state.monster_die_count -=1
                    monster_turn_state.monster_slimes.remove(monster_die)
                    game_world.remove_object(monster_die)


    def draw(self):
        self.font.draw(self.x - 35, self.y + 25, '(HP: %3.0f)' % self.hp, (255, 155, 0))
        self.image.clip_draw(int(self.frame), 0, 200, 200, self.x, self.y)



class Animation:
    def __init__(self, path, max_frame, image_w, image_h):
        self.image = load_image(path)
        self.max_frame = max_frame

        self.image_h = image_h
        self.image_w = image_w

    def clip_draw(self, image_x, image_y, w, h, x, y):
        self.image.clip_draw(image_x * self.image_w, image_y, self.image_w, self.image_h, x, y)