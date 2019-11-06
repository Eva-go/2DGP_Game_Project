from pico2d import *
from handle_event import title_handle_event_class

name = "TitleState"
title = None
curser = None
#mouse_x, mouse_y = 1366 / 2, 768 / 2


def enter():
    global title, curser, event
    title = load_image('Title.png')
    curser = load_image('curser.png')
    event= title_handle_event_class.Title_state_event()


def handle_events():
    event.handle_events()


def exit():
    global title, curser,event
    del (title)
    del (curser)
    del (event)

def draw():
    clear_canvas()
    title.draw(683, 384)
    curser.draw(event.mouse_x, event.mouse_y)
    update_canvas()


def update():
    hide_cursor()


def pause():
    pass


def resume():
    pass
