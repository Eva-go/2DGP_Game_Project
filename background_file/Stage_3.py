import game_framework
import main_state
from pico2d import *


name = "stage_1"
image = None
logo_time = 0.0


def enter():
    global image
    image = load_image('background_file\\Stage_3.png')


def exit():
    global image
    del (image)


def update():
    global logo_time
    if logo_time > 0.5:
        logo_time = 0
        game_framework.change_state(main_state)
    delay(0.01)
    logo_time += 0.01