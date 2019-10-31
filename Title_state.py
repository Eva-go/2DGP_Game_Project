import Class_files
import game_framework

from pico2d import *
import Class_files

name = "TitleState"
title = None
curser = None
mouse_x, mouse_y = 1366 / 2, 768 / 2


def enter():
    global title, curser
    title = load_image('Title.png')
    curser = load_image('curser.png')


def exit():
    global title, curser
    del (title)
    del (curser)


def handle_events():
    global mouse_x, mouse_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(Class_files)
            elif event.type == SDL_MOUSEMOTION:
                mouse_x, mouse_y = event.x, 768 - 1 - event.y
            elif event.type == SDL_MOUSEBUTTONDOWN:
                if mouse_x >= 200 and mouse_y <= 188 and mouse_x <= 485 and mouse_y >= 123:
                    game_framework.change_state(Class_files)
                elif mouse_x >= 880 and mouse_y <= 188 and mouse_x <= 1165 and mouse_y >= 123:
                    game_framework.quit()

def draw():
    global mouse_x, mouse_y
    clear_canvas()
    title.draw(683, 384)
    curser.draw(mouse_x, mouse_y)
    update_canvas()


def update():
    hide_cursor()

def pause():
    pass


def resume():
    pass
