from pico2d import *
import random
import game_framework
import main_state
import game_world
from turn_file import monster_turn_state
from background_file import Stage_1
from background_file import Stage_2
from background_file import Stage_3
from ui_file import game_clear
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
        self.attack_sound = load_wav('music_file\\tengo_attack_sound.wav')
        self.attack_sound.set_volume(30)
        self.font=load_font('resource_file\\Maplestory Light.TTF',20)
        self.slime_attack_damage = 20
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
                    self.attack_sound.play()
                    main_state.player_tengo_attack_hit=True
                    main_state.player_tengo.total_hp = main_state.player_tengo.hp+main_state.player_tengo.tengo_shield
                    main_state.player_tengo.total_hp -= self.slime_attack_damage
                    main_state.player_tengo.hp=main_state.player_tengo.total_hp
                    self.image_count = 0
                self.attack_count=0
                main_state.monster_turn_end()

        if main_state.turn_end_button.turn_owner == main_state.turn_end_button.player_turn:
            if monster_turn_state.monster_slimes[0].hp <= 0 and main_state.monster_die_check==True:
                main_state.monster_die_check = False
                main_state.monster_die_count-=1
                if len(monster_turn_state.monster_slimes)>1:
                    monster_turn_state.monster_slimes[0].hp = monster_turn_state.monster_slimes[1].hp
                else:
                    monster_turn_state.monster_slimes[0].hp=monster_turn_state.monster_slimes[0].hp
                if len(monster_turn_state.monster_slimes) == 1:
                    main_state.replay=2
                    Stage_1.stage_count+=1
                    if Stage_1.stage_count==1:
                        game_framework.change_state(Stage_2)
                    elif Stage_1.stage_count==2:
                        game_framework.change_state(Stage_3)
                    elif Stage_1.stage_count==3:
                         game_framework.change_state(game_clear)



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