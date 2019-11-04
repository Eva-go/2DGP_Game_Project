from pico2d import *

tmp = 20
class Tengo:
    tengo = None

    def __init__(self):
        global tmp
        self.x, self.y = 266, 350
        self.frame = 0
        if Tengo.tengo == None:
            self.image = load_image('player_file\\tengo_sleep.png')

        self.layer = 1

    def update(self):
        global tmp
        self.frame += 1
        if self.frame / tmp >= 12:
            self.frame = 0

    def draw(self):
        self.image.clip_draw((self.frame // tmp) * 200, 0, 200, 200, self.x, self.y)
