from pico2d import *

class Trun_end:
    def __init__(self):
        self.x,self.y = 150,100
        self.image_w,self.image_h =150//2,100//2
        self.trun_end = False
        self.image=load_image('turn_file\\turn_end.png')


    def draw(self):
        self.image.draw(self.x,self.y)

    def update(self):
        pass

    def get_rect(self):
        return (self.x-self.image_w, self.y-self.image_w,self.x + self.image_h, self.y + self.image_h)

    def trun_image_coflict_check(self,mouse_pos):
        x,y,x2,y2 = self.get_rect()
        if mouse_pos[0] >= x and mouse_pos[1] >= y and mouse_pos[0] <= x2 and mouse_pos[1] <= y2:
            return True


