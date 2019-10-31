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

count = 1
tmp=4 #스프라이트 속도 제한 변수


# CARD 속성
class Card:
    def __init__(self,num):
        # 엑셀로 카드이미지,값처리
        self.wb = openpyxl.load_workbook('Card_list.xlsx', data_only=True)
        self.ws = self.wb['Sheet1']
        self.x, self.y = 300 + 100 * num, 125


# CARD 메서드
class Card_Attack(Card):
    # 상속 받아서 image등록
    card_attack = None
    def __init__(self,num):
        super().__init__(num)
        if Card_Attack.card_attack == None:
            self.image = load_image(self.ws['E2'].value)

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass


class Card_Shield(Card):
    # 상속 받아서 image등록
    card_shield = None
    def __init__(self,num):
        super().__init__(num)
        if Card_Shield.card_shield == None:
            self.image = load_image(self.ws['E3'].value)

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass


class Grass:
    def __init__(self):
        self.image = load_image('grass2.png')
        self.layer = 0

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
        global tmp
        self.x, self.y = 266, 350
        self.frame = 0
        if Tengo.tengo == None:
            self.image = load_image('tengo_sleep.png')

    def update(self):
        global tmp
        self.frame = (self.frame + 1) % 12

    def draw(self):
        self.image.clip_draw(self.frame * 200, 0, 200, 200, self.x, self.y)



class Slime:
    slime = None

    def __init__(self, num):
        self.x, self.y = 1066+100*num, 300
        self.frame = random.randint(0, 6)
        if Slime.slime == None:
            self.image = load_image('slime_sleep.png')


    def update(self):
        global tmp
        self.frame += 1
        if self.frame/tmp>=7:
            self.frame=0


    def draw(self):
        global tmp
        self.image.clip_draw((self.frame//tmp) * 200, 0, 200, 200, self.x, self.y)


def enter():
    global tengo,slimes, grass, map,curser,monster,card
    monster=0
    curser = load_image('curser.png')
    tengo = Tengo()
    #slimes=[Slime() for monster in range(3)]
    slimes = [] # 슬라임들 리스트 생성
    for i in range(0,3,1): #슬라임들 시작 끝 스텝순으로
        slimes.append(Slime(i)) # 생성하기

    card=[]
    for i in range(0,5,1):
        rand = random.randint(1, 2)
        if rand == 1:
            card.append(Card_Attack(i))
        elif rand==2:
            card.append(Card_Shield(i))
    grass = Grass()
    map = Map()


def exit():
    global tengo,slimes, grass, map, card_attack, card_shield,curser
    del (tengo)
    del (grass)
    del (slimes) # 궁금!
    del (map)
    del (card_attack)
    del (card_shield)
    del (curser)
    del (card)

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
    for c in card:
        c.draw()
    tengo.draw()
    for slime in slimes:
        slime.draw()
    curser.draw(mouse_x, mouse_y)
   # delay(0.1)

    update_canvas()
