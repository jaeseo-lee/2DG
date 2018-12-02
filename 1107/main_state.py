import random
import json
import os
import success_state
import fail_state
from pico2d import *
import game_framework
import game_world
from enemy import Enemy
from enemy2 import Enemy2
from boss import Boss
from player import Player
from background import Background
from enemy_bullet import Enemy_Bullet

name = "MainState"
score = None
life = None
player = None
grass = None
enemy = None
enemy2 = None
boss = None

def enter():
    global player, background, enemies, score, enemies2, life, boss
    score = 0
    life = 3
    player = Player()
    background = Background()
    enemies = [Enemy() for i in range(50)]
    enemies2 = [Enemy2() for i in range(18)]
    boss = Boss()
    game_world.add_objects(enemies, 1)
    game_world.add_objects(enemies2, 1)
    game_world.add_object(background, 0)
    game_world.add_object(player, 1)
    game_world.add_object(boss, 1)




def exit():
    game_world.clear()

def pause():
    pass

def resume():
    pass

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            player.handle_event(event)
    if life == 0:
        game_framework.run(fail_state)






def update():
    for game_object in game_world.all_objects():
        game_object.update()


def draw():
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()







