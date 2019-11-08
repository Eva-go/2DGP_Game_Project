from pico2d import *
import openpyxl
import Class_files


class Card:
    def __init__(self, num):
        # 엑셀로 카드이미지,값처리
        self.x, self.y = 400 + 150 * num, 125
        self.layer = 2

    def update(self, mx, my):
        self.x,self.y =mx,my


# CARD 메서드
class Card_Attack(Card):
    global mouse_x, mouse_y
    card_attack = None

    def __init__(self, num):
        super().__init__(num)
        if Card_Attack.card_attack == None:
            self.image = load_image('card_file\\Card_Attack.png')

    # def update(self, mx, my):
    #   self.x = mx,self.y = my

    def draw(self):
        self.image.draw(self.x, self.y)


class Card_Shield(Card):
    global mouse_x, mouse_y
    card_shield = None

    def __init__(self, num):
        super().__init__(num)
        if Card_Shield.card_shield == None:
            self.image = load_image('card_file\\Card_Shield.png')

    # def update(self, mx, my):
    #   self.x = mx, self.y = my

    def draw(self):
        self.image.draw(self.x, self.y)
