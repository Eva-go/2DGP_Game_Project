from pico2d import *
import main_state
from background_file import Stage_1
class Grass:
    def __init__(self):
        self.x = 683
        self.y = 150
        self.image = load_image('background_file\\grass2.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass


class Back_ground:
    def __init__(self):
        self.x = 683
        self.y = 384
        self.stage_1 = Stage('background_file\\Map1.png', self.x, self.y)
        self.stage_2 = Stage('background_file\\Map2.png', self.x, self.y)
        self.stage_3 = Stage('background_file\\Map3.png', self.x, self.y)
        self.image = self.stage_1
        self.layer = 0

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        if Stage_1.stage_count==1:
            self.image = self.stage_2
        if Stage_1.stage_count==2:
            self.image = self.stage_3



class Stage:
    def __init__(self, path, x, y):
        self.image = load_image(path)
        self.x = x
        self.y = y

    def draw(self, x, y):
        self.image.draw(x, y)
