from pico2d import *
import game_world
import random
import main_state

class Enemy_Bullet2:
    image = None

    def __init__(self, x=300, y=300):
        velocity = 1.6
        damage = 1
        if Enemy_Bullet2.image == None:
            Enemy_Bullet2.image = load_image('EnemyGun2.png')
        self.x, self.y, self.velocity = x, y, velocity


    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 12, self.y - 10, self.x + 12, self.y + 10

    def update(self):
        self.y -= self.velocity

        if main_state.collide(self, main_state.player):
            game_world.remove_object(self)
            main_state.life -= 1



        #if main_state.player.hp == 0:
            #game_world.remove_object(main_state.player)
            #main_state.player.life -= 1

        if self.y < 20:
            game_world.remove_object(self)


class Enemy_Bullet3:
    image = None

    def __init__(self, x=300, y=300):
        velocity = 1.5
        damage = 1
        if Enemy_Bullet3.image == None:
            Enemy_Bullet3.image = load_image('EnemyGun2.png')
        self.x, self.y, self.velocity = x, y, velocity


    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 12, self.y - 10, self.x + 12, self.y + 10

    def update(self):
        self.y -= self.velocity
        self.x += self.velocity / 3

        if main_state.collide(self, main_state.player):
            game_world.remove_object(self)
            main_state.life -= 1

        #if main_state.player.hp == 0:
            #game_world.remove_object(main_state.player)
            #main_state.player.life -= 1

        if self.y < 20:
            game_world.remove_object(self)

class Enemy_Bullet4:
    image = None

    def __init__(self, x=300, y=300):
        velocity = 1.5
        damage = 1
        if Enemy_Bullet4.image == None:
            Enemy_Bullet4.image = load_image('EnemyGun2.png')
        self.x, self.y, self.velocity = x, y, velocity


    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 12, self.y - 10, self.x + 12, self.y + 10

    def update(self):
        self.y -= self.velocity
        self.x -= self.velocity / 3

        if main_state.collide(self, main_state.player):
            game_world.remove_object(self)
            main_state.life -= 1


        #if main_state.player.hp == 0:
            #game_world.remove_object(main_state.player)
            #main_state.player.life -= 1

        if self.y < 20:
            game_world.remove_object(self)