from pico2d import *
import game_world
import random

class Enemy:
    image = None

    def __init__(self):
        velocity = 1
        if Enemy.image == None:
            Enemy.image = load_image('enemy1.png')
        self.x, self.y, self.velocity = random.randint(50, 550), random.randint(850, 3000), velocity
        self.hp = 100 ## 체력
        self.score = 80 ## 점수

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())


    def get_bb(self):
        return self.x - 20, self.y - 40 , self.x + 20, self.y + 40

    def update(self):
        self.y -= self.velocity

        if self.y < 20:
            game_world.remove_object(self)

