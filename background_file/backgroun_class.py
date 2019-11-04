from pico2d import *


class Grass:
    def __init__(self):
        self.image = load_image('grass2.png')
        self.layer = 0

    def draw(self):
        self.image.draw(683, 150)



class Map:
    def __init__(self):
        self.image = load_image("Map1.png")
        self.layer = 0

    def draw(self):
        self.image.draw(683, 384)

