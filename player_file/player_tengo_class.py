from pico2d import *
import random
import Class_files
tmp = 10
class Tengo:
    tengo = None

    def __init__(self):
        global tmp
        self.x, self.y = 266, 350
        self.frame = 0
        self.hp=50
        if Tengo.tengo == None:
            self.image = load_image('player_file\\tengo_sleep.png')

        self.layer = 1

    def draw(self):
        self.image.clip_draw((self.frame // tmp) * 200, 0, 200, 200, self.x, self.y)

    def update(self):
        global tmp
        self.frame += 1
        if self.frame / tmp >= 12:
            self.frame = 0
        if Class_files.tengo_attack==True:
            self.image = load_image('player_file\\tengo_attack.png')
        elif Class_files.tengo_shield==True:
            self.image = load_image('player_file\\tengo_skill1.png')
        else:
            self.image = load_image('player_file\\tengo_sleep.png')
