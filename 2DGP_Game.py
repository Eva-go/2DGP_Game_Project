from pico2d import *


# Game object class here
class Player:
    global image
    def __init__(self):
        self.x, self.y = 2000, 1000
        self.frame = 0
        self.image = load_image('tengo_sleep.png')
        self.dir = 0

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 200, 0, self.x, self.y)

    def update(self):
        self.frame = (self.frame + 1) % 12


class Monster:
    global image
    def __init__(self):
        self.x, self.y = 1000, 1000
        self.frame = 0
        self.image = load_image('slime.png')
        self.dir = 0

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 1000, 100, self.x, self.y)

    def update(self):
        self.frame = (self.frame + 1) % 7

class BackGround:
    global image
    def __init__(self):
        self.x, self.y = 0, 0
        self.image=load_image('forest.png')
    def draw(self):
        self.image.draw(0.0,1024,512)


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
   # Monster.update()
    clear_canvas()
    player.draw()
    #Monster.draw()
    BackGround.draw()
    update_canvas()
close_canvas()
