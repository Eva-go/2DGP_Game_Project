from pico2d import *
import random
import Class_files

tmp = 10


class Tengo:

    def __init__(self):
        global tmp
        self.x, self.y = 266, 350
        self.frame = 0
        self.hp = 50
        self.image_count=False
        self.sleep = Animation('player_file\\tengo_sleep.png', 12, 200, 200)
        self.attack = Animation('player_file\\tengo_attack.png', 11, 400, 300)
        #self.skill = Animation('player_file\\.png', 21, 351, 129)
        #self.skill = Animation('player_file\\skills.png,',21,173,127)

        self.image = self.sleep

        self.layer = 1

    def draw(self):
        self.image.clip_draw((self.frame // tmp), 0, 200, 200, self.x, self.y)

        pass
    def update(self):
        global tmp
        self.frame += 1
        if self.frame / tmp >= self.image.max_frame:
            self.frame = 0

        if Class_files.tengo_attack:
            self.image = self.attack
            if self.frame == 11:
                Class_files.tengo_attack =False



        #elif Class_files.tengo_shield == True:
            # self.image = self.skill
            pass
        else:
            self.image = self.sleep


class Animation:
    def __init__(self, path, max_frame,image_w, image_h):
        self.image = load_image(path)
        self.max_frame = max_frame

        self.image_h = image_h
        self.image_w = image_w

    def clip_draw(self, image_x, image_y, w, h, x, y):
        self.image.clip_draw(image_x * self.image_w, image_y, self.image_w, self.image_h, x, y)

