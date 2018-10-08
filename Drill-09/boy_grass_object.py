from pico2d import *
import os

os.getcwd()
os.chdir('C:\\2DGP\\2018-2DGP\\Labs\\Lecture08')

class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400.30)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas()
boy = Boy()
grass = Grass()
running = True

while running:
    handle_events()

    boy.update()

    clear_canvas()
    grass.draw()
    boy.draw()

    update_canvas()
    delay(0.05)

close_canvas()