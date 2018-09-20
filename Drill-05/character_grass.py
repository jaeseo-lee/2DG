from pico2d import *
import os

os.getcwd()
os.chdir('C:\\2DGP\\2018-2DGP\\Labs\\Lecture04')

open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

def goto_x_y_2():
    x1, x2 = 203, 132
    y1, y2 = 535, 243
    x_change = x2 - x1
    y_change = y2 - y1
    m = y_change // x_change
    frame = 0
    while (x1 > x2):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x1, y1)
        update_canvas()
        frame = (frame + 1) % 8
        x1 -= 5
        y1 -= 5 * m
        delay(0.02)
        get_events()
def goto_x_y_3():
    x1, x2 = 132, 535
    y1, y2 = 243, 470
    x_change = x2 - x1
    y_change = y2 - y1
    m = y_change / x_change
    frame = 0
    while (x1 < x2):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x1, y1)
        update_canvas()
        frame = (frame + 1) % 8
        x1 += 5
        y1 += 5 * m
        delay(0.02)
        get_events()
def goto_x_y_4():
    x1, x2 = 535, 477
    y1, y2 = 470, 203
    x_change = x2 - x1
    y_change = y2 - y1
    m = y_change / x_change
    frame = 0
    while (x1 > x2):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x1, y1)
        update_canvas()
        frame = (frame + 1) % 8
        x1 -= 5
        y1 -= 5 * m
        delay(0.02)
        get_events()
def goto_x_y_5():
    x1, x2 = 477, 715
    y1, y2 = 203, 136
    x_change = x2 - x1
    y_change = y2 - y1
    m = y_change / x_change
    frame = 0
    while (x1 < x2):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x1, y1)
        update_canvas()
        frame = (frame + 1) % 8
        x1 += 5
        y1 += 5 * m
        delay(0.02)
        get_events()
def goto_x_y_6():
    x1, x2 = 715, 316
    y1, y2 = 136, 225
    x_change = x2 - x1
    y_change = y2 - y1
    m = y_change / x_change
    frame = 0
    while (x1 > x2):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x1, y1)
        update_canvas()
        frame = (frame + 1) % 8
        x1 -= 5
        y1 -= 5 * m
        delay(0.02)
        get_events()
def goto_x_y_7():
    x1, x2 = 316, 510
    y1, y2 = 225, 92
    x_change = x2 - x1
    y_change = y2 - y1
    m = y_change / x_change
    frame = 0
    while (x1 < x2):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x1, y1)
        update_canvas()
        frame = (frame + 1) % 8
        x1 += 5
        y1 += 5 * m
        delay(0.02)
        get_events()
def goto_x_y_8():
    x1, x2 = 510, 692
    y1, y2 = 92, 518
    x_change = x2 - x1
    y_change = y2 - y1
    m = y_change / x_change
    frame = 0
    while (x1 < x2):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x1, y1)
        update_canvas()
        frame = (frame + 1) % 8
        x1 += 5
        y1 += 5 * m
        delay(0.02)
        get_events()
def goto_x_y_9():
    x1, x2 = 692, 682
    y1, y2 = 518, 336
    x_change = x2 - x1
    y_change = y2 - y1
    m = y_change / x_change
    frame = 0
    while (x1 > x2):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x1, y1)
        update_canvas()
        frame = (frame + 1) % 8
        x1 -= 5
        y1 -= 5 * m
        delay(0.02)
        get_events()
def goto_x_y_10():
    x1, x2 = 682, 712
    y1, y2 = 336, 349
    x_change = x2 - x1
    y_change = y2 - y1
    m = y_change / x_change
    frame = 0
    while (x1 < x2):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x1, y1)
        update_canvas()
        frame = (frame + 1) % 8
        x1 += 5
        y1 += 5 * m
        delay(0.02)
        get_events()
def goto_10to1():
    x1, x2 = 712, 203
    y1, y2 = 349, 535
    x_change = x2 - x1
    y_change = y2 - y1
    m = y_change / x_change
    frame = 0
    while (x1 > x2):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x1, y1)
        update_canvas()
        frame = (frame + 1) % 8
        x1 -= 5
        y1 -= 5 * m
        delay(0.02)
        get_events()
while True:

    goto_x_y_2()
    goto_x_y_3()
    goto_x_y_4()
    goto_x_y_5()
    goto_x_y_6()
    goto_x_y_7()
    goto_x_y_8()
    goto_x_y_9()
    goto_x_y_10()
    goto_10to1()
close_canvas()