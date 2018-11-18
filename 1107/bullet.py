from pico2d import *
import game_world
import main_state

class Bullet:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 10):
        if Bullet.image == None:
            Bullet.image = load_image('Gun1.png')
        self.x, self.y, self.velocity = x, y, velocity
        self.damage = 20

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 13, self.y - 13, self.x + 13, self.y + 13

    def update(self):
        self.y += self.velocity
        if main_state.collide(self, main_state.enemy):
            game_world.remove_object(self)
            main_state.enemy.hp -= self.damage
        if (main_state.enemy.hp == 0):
            game_world.remove_object(main_state.enemy)

        if self.y > 800 - 20:
            game_world.remove_object(self)
