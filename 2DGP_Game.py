from pico2d import *


# Game object class here
class Player:
    def __init__(self):
        self.x, self.y = 1000, 1000
        self.frame = 0
        self.image = load_image('tengo_sleep.png')
        self.dir=0

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

    def update(self):
        self.frame = (self.frame + 1) % 12

        if self.x >= 800:
            self.dir = -1
        elif self.x <= 0:
            self.dir = 1


class Monster:
    def __init__(self):
        self.x, self.y = 1000, 1000
        self.image = load_image('dw.gif')

    def draw(self):
        self.image.draw(600, 150)

    def update(self):
        pass


def handle_events():
    global Game_Strat
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            Game_Strat = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            Game_Strat = False


# initialization code 초기화
open_canvas()
player = Player()
Game_Strat = True
while Game_Strat:
    handle_events()
    player.update()

    clear_canvas()
    player.draw()

    update_canvas()
close_canvas()
