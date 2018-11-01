from pico2d import *
from ball import Ball

import game_world

# Boy Event
UP_DOWN, DOWN_DOWN, RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, UP_UP, DOWN_UP, SPACE, RIGHT = range(10)

key_event_table = {
    (SDL_KEYDOWN, SDLK_UP): UP_DOWN,
    (SDL_KEYDOWN, SDLK_DOWN): DOWN_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYUP, SDLK_UP): UP_UP,
    (SDL_KEYUP, SDLK_DOWN): DOWN_UP,
    (SDL_KEYDOWN, SDLK_UP and SDLK_RIGHT): RIGHT,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE
}
# Boy States
class IdleState:

    @staticmethod
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity_x += 1
        elif event == LEFT_DOWN:
            boy.velocity_x -= 1
        elif event == RIGHT_UP:
            boy.velocity_x -= 1
        elif event == LEFT_UP:
            boy.velocity_x += 1
        elif event == UP_DOWN:
            boy.velocity_y += 1
        elif event == UP_UP:
            boy.velocity_y -= 1
        elif event == DOWN_DOWN:
            boy.velocity_y -= 1
        elif event == DOWN_UP:
            boy.velocity_y += 1
        elif event == RIGHT:
            boy.velocity_x += 1
            boy.velocity_y += 1
        boy.timer = 1000

    @staticmethod
    def exit(boy, event):
        if event == SPACE:
            boy.fire_ball()

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        boy.timer -= 1
        #if boy.timer == 0:
            #boy.add_event(SLEEP_TIMER)

    @staticmethod
    def draw(boy):
        boy.image.draw(boy.x, boy.y)


class RunState:

    @staticmethod
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity_x += 1
        elif event == LEFT_DOWN:
            boy.velocity_x -= 1
        elif event == RIGHT_UP:
            boy.velocity_x -= 1
        elif event == LEFT_UP:
            boy.velocity_x += 1
        elif event == UP_DOWN:
            boy.velocity_y += 1
        elif event == UP_UP:
            boy.velocity_y -= 1
        elif event == DOWN_DOWN:
            boy.velocity_y -= 1
        elif event == DOWN_UP:
            boy.velocity_y += 1
        elif event == RIGHT:
            boy.velocity_x += 1
            boy.velocity_y += 1
        boy.dir = boy.velocity_x

    @staticmethod
    def exit(boy, event):
       if event == SPACE:
           boy.fire_ball()

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        boy.timer -= 1
        boy.x += boy.velocity_x
        boy.x = clamp(25, boy.x, 600 - 25)
        boy.y += boy.velocity_y
        boy.y = clamp(25, boy.y, 800 - 25)

    @staticmethod
    def draw(boy):
         boy.image.draw(boy.x, boy.y)

next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState,
                UP_UP: RunState, DOWN_UP: RunState, UP_DOWN: RunState, DOWN_DOWN: RunState,
                RIGHT: RunState, SPACE: IdleState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, RIGHT_DOWN: IdleState, LEFT_DOWN: IdleState,
               UP_UP: IdleState, UP_DOWN: IdleState, DOWN_UP: IdleState, DOWN_DOWN: IdleState,SPACE: RunState},
}

class Boy:

    def __init__(self):
        self.x, self.y = 600 // 2, 50
        self.image = load_image('Player1.png')
        self.dir = 1
        self.velocity_x = 0
        self.velocity_y = 0
        self.frame = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)


    def fire_ball(self):
        ball = Ball(self.x, self.y, self.dir*3)
        game_world.add_object(ball, 1)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

