from pico2d import *

class Grass:
    def __init__(self):
        self.image = load_image('Maingamebackground.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(300, 400)