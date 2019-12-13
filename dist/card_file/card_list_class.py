from pico2d import *
import main_state


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


        #self.x,self.y =mouse_pos


    # 카드가 마우스랑 충돌했는지?
    def card_conflict_check(self, mouse_pos):
        x,y,x2,y2 = self.get_rect() # 충돌범위
        if mouse_pos[0] >= x and  mouse_pos[1] >= y and mouse_pos[0] <= x2 and mouse_pos[1] <= y2:
            return True

CARD_ATTACK, CARD_SHIELD,CARD_ALL_ATTACK= range(3)

# CARD 메서드
class Card_Attack(Card):
    image = None

    def __init__(self, num):
        super().__init__(num)
        if Card_Attack.image == None:
            Card_Attack.image = load_image('card_file\\Card_Attack.png')

    def type(self):
        return CARD_ATTACK

    def draw(self):
        if main_state.card_draw:
            Card_Attack.image.draw(self.x, self.y)
    def update(self):
        if main_state.turn_end_button.turn_owner == main_state.turn_end_button.monster_turn:
            Card_Attack.image = load_image('card_file\\Card_Attack.png')
class Card_Shield(Card):
    image = None

    def __init__(self, num):
        super().__init__(num)
        if Card_Shield.image == None:
            Card_Shield.image = load_image('card_file\\Card_Shield.png')

    def type(self):
        return CARD_SHIELD

    def draw(self):
        if main_state.card_draw:
            Card_Shield.image.draw(self.x, self.y)

    def update(self):
        if main_state.turn_end_button.turn_owner == main_state.turn_end_button.monster_turn:
            Card_Shield.image = load_image('card_file\\Card_Shield.png')

class Card_all_attack(Card):
    image = None

    def __init__(self, num):
        super().__init__(num)
        if Card_all_attack.image == None:
            Card_all_attack.image = load_image('card_file\\Card_all_attack.png')

    def type(self):
        return CARD_ALL_ATTACK

    def draw(self):
        if main_state.card_draw:
            Card_all_attack.image.draw(self.x, self.y)

    def update(self):
        if main_state.turn_end_button.turn_owner == main_state.turn_end_button.monster_turn:
            Card_all_attack.image = load_image('card_file\\Card_all_attack.png')