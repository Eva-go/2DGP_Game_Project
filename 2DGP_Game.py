from pico2d import *


# Game object class here
class Player:
    def __init__(self):
        self.x, self.y = 1000, 1000
        self.image = load_image('Ironclad.png')

    def draw(self):
        self.image.draw(200, 150)
    def update(self):
        pass



class Monster:
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

    delay(0.01)
    update_canvas()
close_canvas()
