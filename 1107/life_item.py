from pico2d import *
import game_world
import random
import math
import game_framework
import main_state

PIXEL_PER_METER = (10.0 / 4)
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

class IdleState:

    @staticmethod
    def enter(enemy, event):
        enemy.velocity -= RUN_SPEED_PPS

        pass
    @staticmethod
    def exit(enemy, event):
        pass
    @staticmethod
    def do(enemy):
        enemy.y += enemy.velocity * game_framework.frame_time
        enemy.timer -= 1
        if enemy.timer < 0 and enemy.y <= 840:
            enemy.timer = 300
        pass
    @staticmethod
    def draw(enemy):
        pass
next_state_table = {
    IdleState: {},

}
class Life_item:
    image = None
    def __init__(self):
        velocity = 0.5
        if Life_item.image == None:
            Life_item.image = load_image('life_up.png')
        self.timer = 500
        self.x, self.y, self.velocity = random.randint(50, 550), random.randint(3000, 7000), velocity
        self.velocityUD = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def draw(self):
        self.cur_state.draw(self)
        self.image.draw(self.x, self.y)
        #draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 15, self.y - 20, self.x + 15, self.y + 20

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

        if self.y < 10:
            game_world.remove_object(self)
        if main_state.collide(self, main_state.player):
            game_world.remove_object(self)
            main_state.life += 1