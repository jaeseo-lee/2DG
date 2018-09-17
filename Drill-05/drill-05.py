from pico2d import *
import os

os.getcwd()
os.chdir('C:\\2DGP\\2018-2DGP\\Labs\\Lecture04')
os.getcwd()

open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')



def goto_x_y_1():
    x = 800 // 2
    y = 600 // 2
    frame = 0
    while (x >= 203 & y <= 535):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x = x - 1
        y = y + 1
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
