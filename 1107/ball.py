from pico2d import *
import game_world

class Ball:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 10):
        if Ball.image == None:
            Ball.image = load_image('Gun1.png')
        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.y += self.velocity

        if self.y > 800 - 20:
            game_world.remove_object(self)
