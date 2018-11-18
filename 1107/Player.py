import game_framework
from pico2d import *
from bullet import Bullet
from enemy import Enemy
import game_world
import random
import math
import main_state
PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_KMPH * PIXEL_PER_METER)
DEGREE_PER_TIME = 3.141592
ROTATE_PER_TIME = PIXEL_PER_METER * 3

# Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

RIGHT_DOWN, LEFT_DOWN, UP_DOWN, DOWN_DOWN, RIGHT_UP, LEFT_UP, UP_UP, DOWN_UP, SPACE = range(9)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYDOWN, SDLK_UP): UP_DOWN,
    (SDL_KEYDOWN, SDLK_DOWN): DOWN_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYUP, SDLK_UP): UP_UP,
    (SDL_KEYUP, SDLK_DOWN): DOWN_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE
}


class IdleState:

    @staticmethod
    def enter(player, event):
        if event == RIGHT_DOWN:
            player.velocityRL += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            player.velocityRL -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            player.velocityRL -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            player.velocityRL += RUN_SPEED_PPS
        elif event == UP_DOWN:
            player.velocityUD += RUN_SPEED_PPS
        elif event == UP_UP:
            player.velocityUD -= RUN_SPEED_PPS
        elif event == DOWN_UP:
            player.velocityUD += RUN_SPEED_PPS
        elif event == DOWN_DOWN:
            player.velocityUD -= RUN_SPEED_PPS
        player.dir_x = clamp(-1, player.velocityRL, 1)
        player.dir_y = clamp(-1, player.velocityUD, 1)

        player.timer = get_time()
        player.cur_time = get_time()
        player.sleep_timer = player.timer + 10.0

    @staticmethod
    def exit(player, event):
        if event == SPACE:
            player.fire_ball()

    @staticmethod
    def do(player):
        player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        player.timer = get_time()

    @staticmethod
    def draw(player):
        player.image.draw(player.x, player.y)


class RunState:

    @staticmethod
    def enter(player, event):
        if event == RIGHT_DOWN:
            player.velocityRL += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            player.velocityRL -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            player.velocityRL -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            player.velocityRL += RUN_SPEED_PPS
        elif event == UP_DOWN:
            player.velocityUD += RUN_SPEED_PPS
        elif event == UP_UP:
            player.velocityUD -= RUN_SPEED_PPS
        elif event == DOWN_UP:
            player.velocityUD += RUN_SPEED_PPS
        elif event == DOWN_DOWN:
            player.velocityUD -= RUN_SPEED_PPS
        player.dir_x = clamp(-1, player.velocityRL, 1)
        player.dir_y = clamp(-1, player.velocityUD, 1)


    @staticmethod
    def exit(player, event):
        if event == SPACE:
            player.fire_ball()

    @staticmethod
    def do(player):
        player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        player.x += player.velocityRL * game_framework.frame_time
        player.y += player.velocityUD * game_framework.frame_time
        player.x = clamp(25, player.x, 600 - 25)
        player.y = clamp(25, player.y, 800 - 25)

    @staticmethod
    def draw(player):
       # if player.dir_x == 1:
       player.image.draw(player.x, player.y)
        #else:
            #player.image.draw(player.x, player.y)

next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState,
                UP_DOWN: RunState, DOWN_DOWN: RunState, UP_UP: RunState, DOWN_UP: RunState, SPACE: IdleState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState,
               UP_DOWN: IdleState, DOWN_DOWN: IdleState, UP_UP: IdleState, DOWN_UP: IdleState, SPACE: RunState},
}

class Player:
    def __init__(self) :
        self.image = load_image("player1.png")
        self.x, self.y = 300, 50
        self.font = load_font('ENCR10B.TTF', 16)
        self.frame = 0
        self.hp = 1
        self.velocityRL = 0
        self.velocityUD = 0
        self.time_x = 470
        self.time_y = 780
        self.dir_x = 1
        self.dir_y = 1
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def draw(self):
        self.cur_state.draw(self)
        self.font.draw(470, 760, 'SCORE: ', (255, 255, 255))
        self.font.draw(self.time_x, self.time_y, '(Time: %3.2f)' % get_time(), (255, 255, 255))

        draw_rectangle(*self.get_bb())

    def fire_ball(self):
        bullet = Bullet(self.x, self.y)
        game_world.add_object(bullet, 1)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self) :
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def get_bb(self):
        return self.x - 16, self.y - 30, self.x + 16, self.y + 30
