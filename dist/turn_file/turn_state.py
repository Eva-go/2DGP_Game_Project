from pico2d import *
from turn_file import player_turn_state
import game_world
class Trun_end:
    def __init__(self):
        self.x,self.y = 150,100
        self.image_w,self.image_h =150//2,100//2
        self.turn_owner=1
        self.player_turn=1
        self.monster_turn=2
        self.none_turn=0
        self.previous_turn_count=1
        self.image=load_image('turn_file\\turn_end.png')

    def turn_owner_state(self):
        self. turn_owner = self.none_turn

    def draw(self):
        if self.turn_owner==self.player_turn:
            self.image.draw(self.x,self.y)
    def update(self):
        if self.turn_owner==self.player_turn:
            self.image.draw(self.x, self.y)

    def get_rect(self):
        #print("turn_get_rect")
        return (self.x-self.image_w, self.y-self.image_w,self.x + self.image_h, self.y + self.image_h)

    def trun_image_coflict_check(self,mouse_pos):
        #print('trun_image_coflict_check')
        x,y,x2,y2 = self.get_rect()
        if mouse_pos[0] >= x and mouse_pos[1] >= y and mouse_pos[0] <= x2 and mouse_pos[1] <= y2:
            return True


