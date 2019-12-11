from pico2d import *
from turn_file import player_turn_state
import game_framework
import main_state
from turn_file import monster_turn_state

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 10

monster_count=1

class Tengo:

    def __init__(self):
        self.x, self.y = 266, 350
        self.frame = 0
        self.hp = 100
        self.tengo_attack_damage = 20
        self.font=load_font('resource_file\\Maplestory Light.TTF',20)
        self.image_count = 0
        self.sleep = Animation('player_file\\tengo_sleep.png', 12, 200, 200)
        self.attack = Animation('player_file\\tengo_attack.png', 11, 400, 300)
        self.skill = Animation('player_file\\sk.png', 15, 500, 300)
        # self.skill = Animation('player_file\\skills.png,',21,173,127)

        self.image = self.sleep

        self.layer = 1

    # def do(self):
    # self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % Animation.max_frame

    def draw(self):
        self.font.draw(self.x-35, self.y + 50, '(HP: %3.0f)' % self.hp, (240, 200, 255))
        self.image.clip_draw(int(self.frame), 0, 200, 200, self.x, self.y)

        pass

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % self.image.max_frame

        if player_turn_state.tengo_attack and not player_turn_state.tengo_shield and not player_turn_state.tengo_all_attack:
            self.image = self.attack
            self.image_count = (self.image_count + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 13
            if self.image_count >= 12.0:
                if len(monster_turn_state.monster_slimes)>0: #몬스터가 0마리보다 크면
                    monster_turn_state.monster_slimes[0].hp-= self.tengo_attack_damage

                main_state.monster_die_check=True
                self.image = self.sleep
                player_turn_state.tengo_attack = False
                self.image_count=0

        if player_turn_state.tengo_shield and not player_turn_state.tengo_attack and not player_turn_state.tengo_all_attack:
            self.image = self.skill
            self.image_count = (self.image_count + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 16
            if self.image_count >= 15.0:
                self.image = self.sleep
                player_turn_state.tengo_shield = False
                self.image_count=0

        if player_turn_state.tengo_all_attack and not player_turn_state.tengo_shield and not player_turn_state.tengo_attack:
            self.image = self.attack
            self.image_count = (self.image_count + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 13
            if self.image_count >= 12.0:
                if len(monster_turn_state.monster_slimes)>0: #몬스터가 0마리보다 크면
                    for i in range(len((monster_turn_state.monster_slimes))):
                        monster_turn_state.monster_slimes[i].hp -= self.tengo_attack_damage

                main_state.monster_die_check = True
                self.image = self.sleep
                player_turn_state.tengo_all_attack = False
                self.image_count = 0


class Animation:
    def __init__(self, path, max_frame, image_w, image_h):
        self.image = load_image(path)
        self.max_frame = max_frame

        self.image_h = image_h
        self.image_w = image_w

    def clip_draw(self, image_x, image_y, w, h, x, y):
        self.image.clip_draw(image_x * self.image_w, image_y, self.image_w, self.image_h, x, y)
