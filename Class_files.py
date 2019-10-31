import random
import json
import os
# import pause_state

from pico2d import *
import game_framework
import Title_state
import openpyxl  # 엑셀 사용 라이브러리

name = "Class_files"


grass = None


map = None



mouse_x, mouse_y = 1366 / 2, 768 / 2
i=0
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
    card_attack = None
    def __init__(self):
        super().__init__()
        if Card_Attack.card_attack == None:
            self.image = load_image(self.ws['E2'].value)

    def draw(self):
        self.image.draw(400, 125)

    def update(self):
        pass


class Card_Shield(Card):
    # 상속 받아서 image등록
    card_shield = None
    def __init__(self):
        super().__init__()
        if Card_Shield.card_shield == None:
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
    tengo = None
    def __init__(self):
        self.x, self.y = 266, 350
        self.frame = 0
        if Tengo.tengo == None:
            self.image = load_image('tengo_sleep.png')

    def update(self):
        self.frame = (self.frame + 1) % 12

    def draw(self):
        self.image.clip_draw(self.frame * 200, 0, 200, 200, self.x, self.y)


class Slime:
    slime = None
    def __init__(self):
        self.x, self.y = random.randint(1066, 1266), 300
        self.frame = random.randint(0, 6)
        if Slime.slime == None:
            self.image = load_image('slime_sleep.png')


    def update(self):
        self.frame = (self.frame + 1) % 7


    def draw(self):
        self.image.clip_draw(self.frame * 200, 0, 200, 200, self.x, self.y)


def enter():
    global tengo,slimes, grass, map, card_attack, card_shield,curser,monster
    monster=0
    curser = load_image('curser.png')
    tengo = Tengo()
    card_attack = Card_Attack()
    slimes=[Slime() for monster in range(3)]
    grass = Grass()
    map = Map()
    card_shield = Card_Shield()


def exit():
    global tengo,slimes, grass, map, card_attack, card_shield,curser
    del (tengo)
    del (grass)
    del (slimes)
    del (map)
    del (card_attack)
    del (card_shield)
    del (curser)

def pause():
    pass


def resume():
    pass


def handle_events():
    global count, mouse_x, mouse_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(Title_state)
        elif event.type == SDL_MOUSEMOTION:
            mouse_x, mouse_y = event.x, 768 - 1 - event.y



def update():
    hide_cursor()
    tengo.update()
    for slime in slimes:
        slime.update()


def draw():
    global mouse_x, mouse_y
    clear_canvas()

    map.draw()
    grass.draw()
    card_attack.draw()
    card_shield.draw()
    tengo.draw()
    for slime in slimes:
        slime.draw()
    curser.draw(mouse_x, mouse_y)
    delay(0.1)

    update_canvas()
