from pico2d import*
import Title_state
import Class_files
import game_framework

class Main_handle_event():
    def __init__(self):
        self.mouse_x, self.mouse_y=0,0
        self.card_list_move = False
        self. card_list_del = False
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
                Class_files.on_mouse_down((event.x, 768 - 1 - event.y))
                #if  self.mouse_x >= 325 and  self.mouse_y >= 30 and self. mouse_x <= 475 and self. mouse_y <= 210:
                 #   self.card_list_move = True

            elif event.type == SDL_MOUSEBUTTONUP:
                pass
                #self.card_list_del = True
                #del (card_list[0])
               #card_list.pop(0)
