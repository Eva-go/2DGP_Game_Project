import random
import json
import os
# import pause_state

from pico2d import *
import game_framework
import Title_state
import openpyxl  # 엑셀 사용 라이브러리

name = "Class_files"

tengo = None
grass = None
font = None
slime1 = None
slime2 = None
map = None
card_attack = None
card_shield = None

x = 0
y = 0
count = 1


# CARD 속성
class Card:
    def __init__(self):
        # 엑셀로 카드이미지,값처리
        self.wb = openpyxl.load_workbook('Card_list.xlsx', data_only=True)
        self.ws = self.wb['Sheet1']


# CARD 메서드
class Card_Attack(Card):
    # 상속 받아서 image등록
    def __init__(self):
        super().__init__()
        self.image = load_image(self.ws['E2'].value)

    def draw(self):
        self.image.draw(400, 125)

    def update(self):
        pass


class Card_Shield(Card):
    # 상속 받아서 image등록
    def __init__(self):
        super().__init__()
        self.image = load_image(self.ws['E3'].value)

    def draw(self):
        self.image.draw(500, 125)

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
    def __init__(self,x,y):
        self.frame = 0
        self.image = load_image('slime_sleep.png')
        self.x, self.y = x, y
    def update(self):
        self.frame = (self.frame + 1) % 7


    def draw(self):
        self.image.clip_draw(self.frame * 200, 0, 200, 200, self.x, self.y)


def enter():
    global tengo, grass, map, card_attack, card_shield, slime1, slime2
    tengo = Tengo()
    card_attack = Card_Attack()
    grass = Grass()
    slime1 = Slime(1166, 300)
    slime2 = Slime(1166, 350)
    map = Map()
    card_shield = Card_Shield()


def exit():
    global tengo, grass, map, card_attack, card_shield, slime1, slime2
    del (tengo)
    del (grass)
    del (slime1)
    del (slime2)
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
    slime1.update()
    slime2.update()


def draw():
    clear_canvas()
    map.draw()
    grass.draw()
    card_attack.draw()
    card_shield.draw()
    tengo.draw()
    slime1.draw()
    slime2.draw()
    delay(0.1)

    update_canvas()
