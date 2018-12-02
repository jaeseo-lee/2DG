from pico2d import *
import game_world
import random
import math
import game_framework
from boss_bullet import Boss_Bullet2
from boss_bullet import Boss_Bullet3
from boss_bullet import Boss_Bullet4
from boss_bullet import Boss_Bullet5
from boss_bullet import Boss_Bullet6
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
        if boss.y > 600:
            boss.y += boss.velocity * game_framework.frame_time

        boss.timer -= 2
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
        self.x, self.y, self.velocity = 300, 600, velocity
        self.velocityUD = 0
        self.hp = 100 #체력
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)


    def draw(self):
        self.cur_state.draw(self)
        self.image.draw(self.x, self.y)
        #draw_rectangle(*self.get_bb())

    def launch(self):
        boss_bullet2 = Boss_Bullet2(self.x, self.y-45)
        boss_bullet3 = Boss_Bullet3(self.x + 15, self.y - 45)
        boss_bullet4 = Boss_Bullet4(self.x - 15, self.y - 45)
        boss_bullet5 = Boss_Bullet5(self.x + 30, self.y - 45)
        boss_bullet6 = Boss_Bullet6(self.x - 30, self.y - 45)
        game_world.add_object(boss_bullet2, 1)
        game_world.add_object(boss_bullet3, 1)
        game_world.add_object(boss_bullet4, 1)
        game_world.add_object(boss_bullet5, 1)
        game_world.add_object(boss_bullet6, 1)


    def get_bb(self):
        return self.x - 50, self.y - 40, self.x + 50, self.y + 40

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



