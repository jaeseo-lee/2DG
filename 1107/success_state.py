import game_framework
import game_world
from background import Background
from pico2d import *

name = "FinalState"
image = None
logo_time = 0.0


def enter():
    global image
    image = load_image('Finishbackground.png')
    pass

def exit():
    game_world.clear()
    global image
    del(image)
    pass

import title_state

def update():

    global logo_time

    if(logo_time > 5.0):
        logo_time = 0
        # game_framework.quit()
        game_framework.change_state(title_state)

    delay(0.01)
    logo_time += 0.01
    pass

def draw():
    global image
    clear_canvas()
    image.draw(300,400)
    update_canvas()
    pass

def handle_events():
    events = get_events()
    pass


def pause(): pass

def resume(): pass