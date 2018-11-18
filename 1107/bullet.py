from pico2d import *
import game_world

class Bullet:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 10):
        if Bullet.image == None:
            Bullet.image = load_image('Gun1.png')
        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 12, self.y - 10, self.x + 12, self.y + 10

    def update(self):
        self.y += self.velocity

        if self.y > 800 - 20:
            game_world.remove_object(self)
