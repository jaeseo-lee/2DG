from pico2d import *
import game_world
import random
import main_state

class Boss_Bullet2:
    image = None

    def __init__(self, x=300, y=300):
        velocity = 1.6
        damage = 1
        if Boss_Bullet2.image == None:
            Boss_Bullet2.image = load_image('EnemyGun3.png')
        self.x, self.y, self.velocity = x, y, velocity


    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 12, self.y - 10, self.x + 12, self.y + 10

    def update(self):
        self.y -= self.velocity / 1.065

        if main_state.collide(self, main_state.player):
            game_world.remove_object(self)
            main_state.life -= 1
        #if main_state.player.hp == 0:
            #game_world.remove_object(main_state.player)
            #main_state.player.life -= 1

        if self.y < 20:
            game_world.remove_object(self)


class Boss_Bullet3:
    image = None

    def __init__(self, x=300, y=300):
        velocity = 1.5
        damage = 1
        if Boss_Bullet3.image == None:
            Boss_Bullet3.image = load_image('EnemyGun3.png')
        self.x, self.y, self.velocity = x, y, velocity


    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 12, self.y - 10, self.x + 12, self.y + 10

    def update(self):
        self.y -= self.velocity
        self.x += self.velocity / 4

        if main_state.collide(self, main_state.player):
            game_world.remove_object(self)
            main_state.life -= 1

        #if main_state.player.hp == 0:
            #game_world.remove_object(main_state.player)
            #main_state.player.life -= 1

        if self.y < 20:
            game_world.remove_object(self)

class Boss_Bullet4:
    image = None

    def __init__(self, x=300, y=300):
        velocity = 1.5
        damage = 1
        if Boss_Bullet4.image == None:
            Boss_Bullet4.image = load_image('EnemyGun3.png')
        self.x, self.y, self.velocity = x, y, velocity


    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 12, self.y - 10, self.x + 12, self.y + 10

    def update(self):
        self.y -= self.velocity
        self.x -= self.velocity / 4

        if main_state.collide(self, main_state.player):
            game_world.remove_object(self)
            main_state.life -= 1


        #if main_state.player.hp == 0:
            #game_world.remove_object(main_state.player)
            #main_state.player.life -= 1

        if self.y < 20:
            game_world.remove_object(self)

class Boss_Bullet5:
    image = None

    def __init__(self, x=300, y=300):
        velocity = 1.5
        damage = 1
        if Boss_Bullet5.image == None:
            Boss_Bullet5.image = load_image('EnemyGun3.png')
        self.x, self.y, self.velocity = x, y, velocity


    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 12, self.y - 10, self.x + 12, self.y + 10

    def update(self):
        self.y -= self.velocity
        self.x += self.velocity / 2

        if main_state.collide(self, main_state.player):
            game_world.remove_object(self)
            main_state.life -= 1


        #if main_state.player.hp == 0:
            #game_world.remove_object(main_state.player)
            #main_state.player.life -= 1

        if self.y < 20:
            game_world.remove_object(self)

class Boss_Bullet6:
    image = None

    def __init__(self, x=300, y=300):
        velocity = 1.5
        damage = 1
        if Boss_Bullet6.image == None:
            Boss_Bullet6.image = load_image('EnemyGun3.png')
        self.x, self.y, self.velocity = x, y, velocity


    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 12, self.y - 10, self.x + 12, self.y + 10

    def update(self):
        self.y -= self.velocity
        self.x -= self.velocity / 2

        if main_state.collide(self, main_state.player):
            game_world.remove_object(self)
            main_state.life -= 1


        #if main_state.player.hp == 0:
            #game_world.remove_object(main_state.player)
            #main_state.player.life -= 1

        if self.y < 20:
            game_world.remove_object(self)