import random
import json
import os
# import pause_state

from pico2d import *
import game_framework
import Title_state
import openpyxl #엑셀 사용 라이브러리

name = "Class_files"

tengo = None
grass = None
font = None
slime = None
map = None
card_attack = None
card_shield= None

x = 0
y = 0
count = 1


class Card:
    def __init__(self):
        #엑셀로 카드이미지,값처리
        self.wb=openpyxl.load_workbook('Card_list.xlsx', data_only=True)
        self.ws = self.wb['Sheet1']


class Card_Attack(Card):
    #상속 받아서 image등록
    def __init__(self):
        super().__init__()
        self.image = load_image(self.ws['E2'].value)

    def draw(self):
        self.image.draw(400, 200)

    def update(self):
        pass

class Card_Shield(Card):
    # 상속 받아서 image등록
    def __init__(self):
        super().__init__()
        self.image = load_image(self.ws['E3'].value)

        self.x = 0
        self.y = 0
    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass


class Grass:
    def __init__(self):
        self.image = load_image('grass2.png')

    def draw(self):
        self.image.draw(683, 150)


class Map:
    def __init__(self):
        self.image = load_image("Map1.png")

    def draw(self):
        self.image.draw(683, 384)


class Tengo:
    def __init__(self):
        self.x, self.y = 266, 350
        self.frame = 0
        self.image = load_image('tengo_sleep.png')

    def update(self):
        self.frame = (self.frame + 1) % 12

    def draw(self):
        self.image.clip_draw(self.frame * 200, 0, 200, 200, self.x, self.y)


class Slime:
    def __init__(self):
        self.x, self.y = 1166, 270
        self.frame = 0
        self.image = load_image('slime_sleep.png')

    def update(self):
        self.frame = (self.frame + 1) % 7

    def draw(self):
        self.image.clip_draw(self.frame * 200, 0, 200, 200, self.x, self.y)


def enter():
    global tengo, grass, slime, map, card_attack,card_shield
    tengo = Tengo()
    card_attack = Card_Attack()
    grass = Grass()
    slime = Slime()
    map = Map()
    card_shield=Card_Shield()


def exit():
    global tengo, grass, slime, map, card_attack,card_shield
    del (tengo)
    del (grass)
    del (slime)
    del (map)
    del (card_attack)
    del (card_shield)


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
    map.draw()
    grass.draw()
    card_attack.draw()
    card_shield.draw()
    tengo.draw()
    slime.draw()
    delay(0.1)

    update_canvas()
