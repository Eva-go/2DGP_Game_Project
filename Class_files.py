import random
import json
import os
# import pause_state

from pico2d import *

import game_framework
import Title_state

name = "Class_files"

tengo = None
grass = None
font = None
slime = None
map = None

x = 0
y = 0
count = 1


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(683, 100)

class Map:
    def __init__(self):
        self.image = load_image("Map1.png")

    def draw(self):
        self.image.draw(683, 384)


class Tengo:
    def __init__(self):
        self.x, self.y = 266, 250
        self.frame = 0
        self.image = load_image('tengo_sleep.png')

    def update(self):
        self.frame = (self.frame + 1) % 12

    def draw(self):
        self.image.clip_draw(self.frame * 200, 0, 200, 200, self.x, self.y)

class Slime:
    def __init__(self):
        self.x, self.y = 1166, 220
        self.frame = 0
        self.image = load_image('slime_sleep.png')

    def update(self):
        self.frame = (self.frame + 1) % 7

    def draw(self):
        self.image.clip_draw(self.frame * 200, 0, 200, 200, self.x, self.y)





def enter():
    global tengo, grass, slime, map
    tengo = Tengo()
    grass = Grass()
    slime = Slime()
    map = Map()


def exit():
    global tengo, grass, slime, map
    del (tengo)
    del (grass)
    del (slime)
    del (map)


def pause():
    pass


def resume():
    pass


def handle_events():
    global count
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(Title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            x, y = event.x, event.y


            # game_framework.push_state(pause_state2)


def update():
    tengo.update()
    slime.update()


def draw():
    clear_canvas()
    # grass.draw()
    map.draw()
    grass.draw()
    tengo.draw()
    slime.draw()
    delay(0.1)

    update_canvas()
