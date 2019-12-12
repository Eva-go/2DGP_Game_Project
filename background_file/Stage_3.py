import game_framework
import main_state
from pico2d import *


name = "stage_3"
image = None
logo_time = 0.0


def enter():
    global image
    image = load_image('background_file\\Stage_3.png')


def exit():
    global image
    del (image)

def draw():
    global image
    clear_canvas()
    image.draw(683, 384)
    update_canvas()


def update():
    global logo_time
    if logo_time > 0.5:
        logo_time = 0
        game_framework.change_state(main_state)
    delay(0.01)
    logo_time += 0.01

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False