from pico2d import *
import game_world


class Game_cost:
    image=None
    def __init__(self, cost_point):
        self.cost_max=3
        self.cost_current=self.cost_max
        self.x,self.y =50,500+(50 * cost_point)
        if Game_cost.image == None:
            self.image = load_image('cost_file\\cost_image.png')

    def draw(self):
       self.image.draw(self.x, self.y)


    def update(self):
        self.cost_current