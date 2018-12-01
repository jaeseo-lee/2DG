from pico2d import *
import main_state
from boss import Boss


class Background:
    def __init__(self):
        self.image = load_image('Maingamebackground.png')
        self.bgm = load_music('DeathfireGrasp.wav')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()


    def update(self):
        pass

    def draw(self):
        self.image.draw(300, 400)