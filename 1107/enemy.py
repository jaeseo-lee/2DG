from pico2d import *
import game_world
import random

class Enemy:
    image = None

    def __init__(self, x = 400, y = 600, velocity = 2):
        if Enemy.image == None:
            Enemy.image = load_image('Enemy1.png')
        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.y -= self.velocity

        if self.y > 20:
            game_world.remove_object(self)