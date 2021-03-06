import game_framework
from pico2d import *
from ball import Ball
import math
import random
import game_world

# Boy Run Speed
# fill expressions correctly
PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
ANGLE_PER_SEC = 720.0

# Boy Action Speed
# fill expressions correctly
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8



# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SLEEP_TIMER, SPACE = range(6)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE
}


# Boy States

class IdleState:

    @staticmethod
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            boy.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            boy.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            boy.velocity += RUN_SPEED_PPS
        boy.start_time = get_time()
        boy.timer = get_time()
        boy.save_timer = boy.timer + 10.0

    @staticmethod
    def exit(boy, event):
        if event == SPACE:
            boy.fire_ball()
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        boy.timer = get_time()
        if boy.timer >= boy.save_timer:
            boy.add_event(SLEEP_TIMER)

    @staticmethod
    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(int(boy.frame) * 100, 300, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(int(boy.frame) * 100, 200, 100, 100, boy.x, boy.y)
        boy.font.draw(boy.x - 60, boy.y + 75, '(IDLE_START_TIME = %f)' % boy.start_time, (255, 0, 0))
        boy.font.draw(boy.x - 60, boy.y + 90, '(Time - IDLE_START_TIME = 10)')

class RunState:

    @staticmethod
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            boy.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            boy.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            boy.velocity += RUN_SPEED_PPS
        boy.dir = clamp(-1, boy.velocity, 1)
        pass

    @staticmethod
    def exit(boy, event):
        if event == SPACE:
            boy.fire_ball()

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        boy.x += boy.velocity * game_framework.frame_time
        boy.x = clamp(25, boy.x, 1600 - 25)

    @staticmethod
    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(int(boy.frame) * 100, 100, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(int(boy.frame) * 100, 0, 100, 100, boy.x, boy.y)


class SleepState:

    @staticmethod
    def enter(boy, event):
        boy.frame = 0
        boy.ghost_frame = 0
        boy.ghost_light = random.randint(0, 100) * 0.01
        boy.ghost_up_timer = 0
        boy.ghost_circle_start_timer = 0
        boy.ghost_circle_timer = 0
        boy.r = PIXEL_PER_METER * 3
        boy.ghost_start = 0

    @staticmethod
    def exit(boy, event):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        boy.ghost_frame = (boy.ghost_frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8

        if (boy.ghost_up_timer <= boy.r and boy.ghost_start == 0):
            boy.ghost_up_timer += boy.r / 100
        elif (boy.ghost_up_timer >= boy.r and boy.ghost_start == 0):
            boy.ghost_circle_start_timer = get_time()
            boy.ghost_start = 1
            boy.ghost_up_timer = 0

        if (boy.ghost_circle_start_timer > 0):
            boy.ghost_circle_timer = boy.ghost_circle_start_timer - get_time()
        elif (boy.ghost_circle_timer >= 1):
            boy.ghost_circle_start_timer = get_time()

    @staticmethod
    def draw(boy):
        if boy.dir == 1:
            boy.image.opacify(1)
            boy.image.clip_composite_draw(int(boy.frame) * 100, 300, 100, 100, 3.141592 / 2, '', boy.x - 25, boy.y - 25, 100, 100)
            boy.image.opacify(boy.ghost_light)
            if boy.ghost_start == 0:
                boy.image.clip_composite_draw(int(boy.ghost_frame) * 100, 300, 100, 100, 3.141592 / 2, '', (boy.x - 25), boy.y - 25 + boy.ghost_up_timer, 100, 100)
            elif boy.ghost_start == 1:
                boy.image.clip_composite_draw(int(boy.ghost_frame) * 100, 300, 100, 100, 3.141592 / 2, '', (boy.x - 25) + boy.r * math.cos(ANGLE_PER_SEC * (boy.ghost_circle_timer % 1)),boy.y - 25 + boy.ghost_up_timer + boy.r * math.sin(ANGLE_PER_SEC * (boy.ghost_circle_timer % 1)), 100, 100)
            boy.image.opacify(1)

        else:
            boy.image.opacify(1)
            boy.image.clip_composite_draw(int(boy.frame) * 100, 200, 100, 100, -3.141592 / 2, '', boy.x + 25, boy.y - 25, 100, 100)
            boy.image.opacify(boy.ghost_light)

            if boy.ghost_start == 0:
                boy.image.clip_composite_draw(int(boy.ghost_frame) * 100, 200, 100, 100, -3.141592 / 2, '', (boy.x + 25), boy.y - 25 + boy.ghost_up_timer, 100, 100)
            elif boy.ghost_start == 1:
                boy.image.clip_composite_draw(int(boy.ghost_frame) * 100, 200, 100, 100, -3.141592 / 2, '',  (boy.x + 25) + boy.r * math.cos(ANGLE_PER_SEC * (boy.ghost_circle_timer % 1)),  boy.y - 25 + boy.ghost_up_timer + boy.r * math.sin( ANGLE_PER_SEC * (boy.ghost_circle_timer % 1)), 100, 100)
            boy.image.opacify(1)

next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, SLEEP_TIMER: SleepState, SPACE: IdleState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, SPACE: RunState},
    SleepState: {LEFT_DOWN: RunState, RIGHT_DOWN: RunState, LEFT_UP: RunState, RIGHT_UP: RunState, SPACE: IdleState}
}

class Boy:

    def __init__(self):
        self.x, self.y = 1600 // 2, 90
        # Boy is only once created, so instance image loading is fine
        self.image = load_image('animation_sheet.png')
        self.font = load_font('ENCR10B.TTF', 16)
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)


    def fire_ball(self):
        ball = Ball(self.x, self.y, self.dir*RUN_SPEED_PPS)
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
        self.font.draw(self.x - 60, self.y + 50, '(Time: %3.2f)' % get_time(), (255, 255, 0))

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

