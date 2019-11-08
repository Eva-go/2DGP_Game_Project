from pico2d import *
import Class_files
import game_framework


class Title_state_event:
    def __init__(self):
        self.mouse_x, self.mouse_y = 0, 0

    def handle_events(self):
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
                    self.mouse_x, self.mouse_y = event.x, 768 - 1 - event.y
                elif event.type == SDL_MOUSEBUTTONUP:
                    if self.mouse_x >= 200 and self.mouse_y <= 188 and self.mouse_x <= 485 and self.mouse_y >= 123:
                        game_framework.change_state(Class_files)
                    elif self.mouse_x >= 880 and self.mouse_y <= 188 and self.mouse_x <= 1165 and self.mouse_y >= 123:
                        game_framework.quit()
    def draw(self):
        pass
    def update(self):
        pass
