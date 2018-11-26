from pico2d import *
import game_world
import random
import main_state

class Enemy_Bullet2:
    image = None

    def __init__(self, x=300, y=300):
        velocity = 1.3
        damage = 1
        if Enemy_Bullet.image == None:
            Enemy_Bullet.image = load_image('EnemyGun5.png')
        self.x, self.y, self.velocity = x, y, velocity


    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def update(self):
        self.y -= self.velocity

        if main_state.collide(self, main_state.player):
            game_world.remove_object(self)


        #if main_state.player.hp == 0:
            #game_world.remove_object(main_state.player)
            #main_state.player.life -= 1



        if self.y < 20:
            game_world.remove_object(self)