from pico2d import *
import openpyxl
import Class_files


class Card:
    def __init__(self, num):
        # 엑셀로 카드이미지,값처리
        self.x, self.y = 400 + 150 * num, 125
        self.half_w = 150//2
        self.half_h = 200//2
        self.layer = 2

    # 충돌 영역 반환 해줌
    def get_rect(self):
        return (self.x-self.half_w, self.y-self.half_h,self.x + self.half_w, self.y + self.half_h)

    def update(self, mouse_pos):
        self.x,self.y =mouse_pos


    # 카드가 마우스랑 충돌했는지?
    def card_conflict_check(self, mouse_pos):
        x,y,x2,y2 = self.get_rect() # 충돌범위
        if mouse_pos[0] >= x and  mouse_pos[1] >= y and mouse_pos[0] <= x2 and mouse_pos[1] <= y2:
            return True


# CARD 메서드
class Card_Attack(Card):
    global mouse_x, mouse_y
    card_attack = None

    def __init__(self, num):
        super().__init__(num)
        if Card_Attack.card_attack == None:
            self.image = load_image('card_file\\Card_Attack.png')


    def draw(self):
        self.image.draw(self.x, self.y)


class Card_Shield(Card):
    global mouse_x, mouse_y
    card_shield = None

    def __init__(self, num):
        super().__init__(num)
        if Card_Shield.card_shield == None:
            self.image = load_image('card_file\\Card_Shield.png')


    def draw(self):
        self.image.draw(self.x, self.y)
