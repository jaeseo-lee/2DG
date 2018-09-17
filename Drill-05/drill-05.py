from pico2d import *
import os

os.getcwd()
os.chdir('C:\\2DGP\\2018-2DGP\\Labs\\Lecture04')

open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

def goto_x_y_1():
    x1, x2 = 25, 203
    y1, y2 = 90, 535
    x_change = x2 - x1
    y_change = y2 - y1
    m = y_change // x_change
    frame = 0
    while (x1 < x2):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x1, y1)
        update_canvas()
        frame = (frame + 1) % 8
        x1 += 5
        y1 += 5 * m
        delay(0.02)
        get_events()
def goto_x_y_2():
    pass
def goto_x_y_3():
    pass
def goto_x_y_4():
    pass
def goto_x_y_5():
    pass
def goto_x_y_6():
    pass
def goto_x_y_7():
    pass
def goto_x_y_8():
    pass
def goto_x_y_9():
    pass
def goto_x_y_10():
    pass

while True:
    goto_x_y_1()
    goto_x_y_2()
    goto_x_y_3()
    goto_x_y_4()
    goto_x_y_5()
    goto_x_y_6()
    goto_x_y_7()
    goto_x_y_8()
    goto_x_y_9()
    goto_x_y_10()
close_canvas()