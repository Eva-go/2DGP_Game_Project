from pico2d import *
import random
import game_framework

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 7

class Slime:

    def __init__(self, num):
        self.x, self.y = 866 + 100 * num, 300
        self.frame = random.randint(0, 6)
        self.hp=20
        self.sleep = Animation('monseter_file\\slime_sleep.png',6,200,200)
        self. slime_attack=5
        self.image = self.sleep
    def update(self):

        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 7
        if self.frame >= self.image.max_frame:
            self.frame = 0

    def draw(self):

        self.image.clip_draw(int(self.frame), 0, 200, 200, self.x, self.y)



class Animation:
    def __init__(self, path, max_frame, image_w, image_h):
        self.image = load_image(path)
        self.max_frame = max_frame

        self.image_h = image_h
        self.image_w = image_w

    def clip_draw(self, image_x, image_y, w, h, x, y):
        self.image.clip_draw(image_x * self.image_w, image_y, self.image_w, self.image_h, x, y)