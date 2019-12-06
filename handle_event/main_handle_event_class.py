from pico2d import*
import Title_state
import Class_files
import game_framework
from card_file import card_list_class
class Main_handle_event():
    def __init__(self):
        self.mouse_x, self.mouse_y=0,0
        self.card_list_move = False
        self.card_list_del = False
        self.mouse_point=0,0
    def handle_events(self):
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                game_framework.quit()
            elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.change_state(Title_state)
            elif event.type == SDL_MOUSEMOTION:
                self.mouse_x,  self.mouse_y = event.x, 768 - 1 - event.y

            elif event.type == SDL_MOUSEBUTTONDOWN:
                pass

            elif event.type == SDL_MOUSEBUTTONUP:
                 Class_files.on_mouse_up((event.x, 768 - 1 - event.y))
                 Class_files.player_turn_end((event.x, 768 - 1 - event.y))
                 self.mouse_point=(event.x, 768 - 1 - event.y)