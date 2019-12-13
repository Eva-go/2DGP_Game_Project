import game_framework
from pico2d import *
import Title_state

name = "stage_1"
image = None
logo_time = 0.0
stage_count=0
def enter():
    global image
    image = load_image('background_file\\grass2.png')

    image = load_image('ui_file\\game_clear.png')



def exit():
    global image
    del (image)


def update():
    global logo_time
    if logo_time > 1.0:
        logo_time = 0
        game_framework.quit()
    delay(0.01)
    logo_time += 0.01


def draw():
    global image
    clear_canvas()
    image.draw(683, 384)
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
