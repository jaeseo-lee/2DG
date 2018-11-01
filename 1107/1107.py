from pico2d import *

pico2d.open_canvas(600, 800)
BackGround = load_image('Maingamebackground.png')
Player = load_image('Player1.png')
bullet = load_image('Gun1.png')
# Player Event
UP, DOWN, LEFT, RIGHT, RIGHT_UP, LEFT_UP, RIGHT_DOWN, LEFT_DOWN, LAUNCH = range(9)
key_event_table = {
    (SDL_KEYUP): UP,
    (SDL_KEYDOWN): DOWN,
    (SDLK_LEFT): LEFT,
    (SDLK_RIGHT): RIGHT,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDLK_SPACE): LAUNCH
}
class Player:

    def __init__(self):
        self.x, self.y = 800 // 2, 50
        self.image = load_image('Player1.png')

    def update(self):
        self.cur_state.do(self)

    def draw(self):
        self.cur_state.draw(self)

    def handle_event(self, event):
        if(event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

close_canvas()








