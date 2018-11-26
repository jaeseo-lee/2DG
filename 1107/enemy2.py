from pico2d import *
import game_world
import random
import math
import game_framework
from enemy_bullet2 import Enemy_Bullet2
from enemy_bullet2 import Enemy_Bullet3
from enemy_bullet2 import Enemy_Bullet4

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
    def enter(enemy2, event):
        enemy2.velocity -= RUN_SPEED_PPS

        pass
    @staticmethod
    def exit(enemy2, event):
        pass
    @staticmethod
    def do(enemy2):
        enemy2.y += enemy2.velocity * game_framework.frame_time
        enemy2.timer -= 1
        if enemy2.timer < 0 and enemy2.y <= 840:
            Enemy2.launch(enemy2)
            enemy2.timer = 500
        pass
    @staticmethod
    def draw(enemy2):
        pass

class MoveState:

    @staticmethod
    def enter(enemy2, event):

        pass
    @staticmethod
    def exit(enemy2, event):
        pass
    @staticmethod
    def do(enemy2):

        pass
    @staticmethod
    def draw(enemy2):

        pass

class AttackState:

    @staticmethod
    def enter(enemy2, event):

        pass
    @staticmethod
    def exit(enemy2, event):
        pass
    @staticmethod
    def do(enemy2):

        pass
    @staticmethod
    def draw(enemy2):

        pass
next_state_table = {
    IdleState: {},
    MoveState: {},
    AttackState: {}
}

class Enemy2:
    image = None
    enemy_bullet = None
    def __init__(self):
        velocity = 0.5
        if Enemy2.image == None:
            Enemy2.image = load_image('Enemy2.png')
        self.timer = 500
        self.x, self.y, self.velocity = random.randint(50, 550), random.randint(1500, 5000), velocity
        self.velocityUD = 0
        self.hp = 200# 체력
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)


    def draw(self):
        self.cur_state.draw(self)
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def launch(self):
        enemy_bullet2 = Enemy_Bullet2(self.x, self.y-45)
        enemy_bullet4 = Enemy_Bullet4(self.x - 25, self.y - 45)
        enemy_bullet3 = Enemy_Bullet3(self.x + 25, self.y - 45)
        game_world.add_object(enemy_bullet2, 1)
        game_world.add_object(enemy_bullet4, 1)
        game_world.add_object(enemy_bullet3, 1)

    def get_bb(self):
        return self.x - 40, self.y - 40 , self.x + 40, self.y + 40

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