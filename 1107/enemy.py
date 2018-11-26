from pico2d import *
import game_world
import random
import math
from enemy_bullet import Enemy_Bullet

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

MOVE, DIE, ATTACK = range(3)

class IdleState:

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
class Enemy:
    image = None
    def __init__(self):
        velocity = 0.8
        if Enemy.image == None:
            Enemy.image = load_image('Enemy1.png')
        self.x, self.y, self.velocity = random.randint(50, 550), random.randint(850, 5000), velocity
        self.hp = 100


    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def launch(self):
        enemy_bullet = Enemy_Bullet(self.x,self.y)
        game_world.add_object(enemy_bullet, 1)

    def get_bb(self):
        return self.x - 20, self.y - 40, self.x + 20, self.y + 40

    def update(self):
        self.y -= self.velocity
        self.launch()

        if self.y < 20:
            game_world.remove_object(self)

