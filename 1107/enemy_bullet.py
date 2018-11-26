from pico2d import *
import game_world
import random
import main_state

class Enemy_Bullet:
    image = None

    def __init__(self, x=300, y=300):
        velocity = 1.5
        if Enemy_Bullet.image == None:
            Enemy_Bullet.image = load_image('EnemyGun1.png')
        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def update(self):
        self.y -= self.velocity

        if self.y < 20:
            game_world.remove_object(self)