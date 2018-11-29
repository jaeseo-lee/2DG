from pico2d import *
import game_world
import random
import math
import game_framework
from enemy_bullet import Enemy_Bullet

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

MOVE, DIE, ATTACK = range(3)

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
            Enemy.launch(enemy)
            enemy.timer = 300
        pass
    @staticmethod
    def draw(enemy):
        pass

class MoveState:

    @staticmethod
    def enter(enemy, event):

        pass
    @staticmethod
    def exit(enemy, event):
        pass
    @staticmethod
    def do(enemy):

        pass
    @staticmethod
    def draw(enemy):

        pass

class AttackState:

    @staticmethod
    def enter(enemy, event):

        pass
    @staticmethod
    def exit(enemy, event):
        pass
    @staticmethod
    def do(enemy):

        pass
    @staticmethod
    def draw(enemy):

        pass
next_state_table = {
    IdleState: {},
    MoveState: {},
    AttackState: {}
}
class Enemy:
    image = None
    def __init__(self):
        velocity = 0.7
        if Enemy.image == None:
            Enemy.image = load_image('Enemy1.png')
        self.timer = 500
        self.x, self.y, self.velocity = random.randint(50, 550), random.randint(1200, 6000), velocity
        self.velocityUD = 0
        self.hp = 100
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def draw(self):
        self.cur_state.draw(self)
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def launch(self):
        enemy_bullet1 = Enemy_Bullet(self.x, self.y-45)
        game_world.add_object(enemy_bullet1, 1)

    def get_bb(self):
        return self.x - 20, self.y - 40, self.x + 20, self.y + 40

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

        if self.y < 20:
            game_world.remove_object(self)

