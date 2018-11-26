from pico2d import *
import game_world
import random

class Enemy2:
    image = None
    enemy_bullet = None
    def __init__(self):
        velocity = 0.5
        if Enemy2.image == None:
            Enemy2.image = load_image('Enemy2.png')
        if Enemy2.enemy_bullet == None:
            Enemy2.enemy_bullet = load_image('EnemyGun2.png')
        self.x, self.y, self.velocity = random.randint(50, 550), random.randint(1500, 5000), velocity
        self.hp = 200 # 체력
         # 점수

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 40, self.y - 40 , self.x + 40, self.y + 40

    def update(self):
        self.y -= self.velocity

        if self.y < 20:
            game_world.remove_object(self)