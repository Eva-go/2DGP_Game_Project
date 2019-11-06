import game_framework
import Class_files
import Title_state
from pico2d import *


name = "LogoStartState"
image = None
logo_time = 0.0


def enter():
    global image
    image = load_image("KPU_Logo.png")


def exit():
    global image
    del (image)


def update():
    global logo_time
    if logo_time > 0.5:
        logo_time = 0
        game_framework.change_state(Title_state)
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
