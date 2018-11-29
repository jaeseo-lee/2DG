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
    def enter(boss, event):
        boss.velocity -= RUN_SPEED_PPS

        pass
    @staticmethod
    def exit(boss, event):
        pass
    @staticmethod
    def do(boss):
        if boss.y > 500:
            boss.y += boss.velocity * game_framework.frame_time

        boss.timer -= 1
        if boss.timer < 0 and boss.y <= 840:
            Boss.launch(boss)
            boss.timer = 400
        pass
    @staticmethod
    def draw(boss):
        pass

class MoveState:

    @staticmethod
    def enter(boss, event):

        pass
    @staticmethod
    def exit(boss, event):
        pass
    @staticmethod
    def do(boss):

        pass
    @staticmethod
    def draw(boss):

        pass

class AttackState:

    @staticmethod
    def enter(boss, event):

        pass
    @staticmethod
    def exit(boss, event):
        pass
    @staticmethod
    def do(boss):

        pass
    @staticmethod
    def draw(enemy2):

        pass
next_state_table = {
    IdleState: {},
    MoveState: {},
    AttackState: {}
}

class Boss:
    image = None
    enemy_bullet = None
    def __init__(self):
        velocity = 0.5
        if Boss.image == None:
            Boss.image = load_image('MiddleBoss.png')
        self.timer = 400
        self.x, self.y, self.velocity = 300, 500, velocity
        self.velocityUD = 0
        self.hp = 5000 #체력
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
        return self.x - 50, self.y - 40 , self.x + 50, self.y + 40

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



