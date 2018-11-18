from pico2d import *
import game_world
import random

class Enemy:
    image = None

    def __init__(self, x = random.randint(50, 550), y = 800, velocity = 1):
        if Enemy.image == None:
            Enemy.image = load_image('enemy1.png')
        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb1())
        draw_rectangle(*self.get_bb2())


    def get_bb1(self):
        return self.x - 40, self.y , self.x + 40, self.y + 45

    def get_bb2(self):
        return self.x - 20, self.y - 40, self.x + 20, self.y

    def update(self):
        self.y -= self.velocity

        if self.y < 20:
            game_world.remove_object(self)

