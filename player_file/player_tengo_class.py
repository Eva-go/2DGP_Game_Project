from pico2d import *
import random
import Class_files
import game_framework

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 10


class Tengo:

    def __init__(self):
        self.x, self.y = 266, 350
        self.frame = 0
        self.hp = 50
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
        self.image.clip_draw(int(self.frame), 0, 200, 200, self.x, self.y)

        pass

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % self.image.max_frame

        if Class_files.tengo_attack and not Class_files.tengo_shield:
            self.image = self.attack
            self.image_count = (self.image_count + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 13
            print(self.image_count)
            if self.image_count >= 12.0:
                self.image = self.sleep
                Class_files.tengo_attack = False
                self.image_count=0

        if Class_files.tengo_shield and not Class_files.tengo_attack:
            self.image = self.skill
            self.image_count = (self.image_count + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 16
            print(self.image_count)
            if self.image_count >= 15.0:
                self.image = self.sleep
                Class_files.tengo_shield = False
                self.image_count=0


class Animation:
    def __init__(self, path, max_frame, image_w, image_h):
        self.image = load_image(path)
        self.max_frame = max_frame

        self.image_h = image_h
        self.image_w = image_w

    def clip_draw(self, image_x, image_y, w, h, x, y):
        self.image.clip_draw(image_x * self.image_w, image_y, self.image_w, self.image_h, x, y)
