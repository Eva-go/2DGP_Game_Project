from pico2d import *

class Trun_end:
    def __init__(self):
        self.x,self.y = 150,100
        self.trun_end = False
        self.image=load_image('turn_file\\turn_end.png')

    def get_rect(self):
        return (self.x-self.half_w, self.y-self.half_h,self.x + self.half_w, self.y + self.half_h)

    def draw(self):
        self.image.draw(self.x,self.y)

    def update(self):
        pass

    def trun_image_coflict_check(self,mouse_pos):
        x, y, x2, y2 = self.get_rect()
        if self.x-100 >= x and  self.y-40 >= y and self.x+100 <= x2 and self.y+40 <= y2:
            return True

class Player_trun:
    def __init__(self):
        pass

class Monster_turn:
    def __init__(self):
        pass