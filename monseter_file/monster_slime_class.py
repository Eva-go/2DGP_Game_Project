from pico2d import *
import random

tmp = 20


class Slime:
    slime = None

    def __init__(self, num):
        self.x, self.y = 866 + 100 * num, 300
        self.frame = random.randint(0, 6)
        if Slime.slime == None:
            self.image = load_image('monseter_file\\slime_sleep.png')

        self.layer = 2

    def update(self):
        global tmp
        self.frame += 1
        if self.frame / tmp >= 7:
            self.frame = 0

    def draw(self):
        global tmp
        self.image.clip_draw((self.frame // tmp) * 200, 0, 200, 200, self.x, self.y)
