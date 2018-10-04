from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

frame, x, y, temp = 0, 0, 0, 0
xPosition = [random.randint(0, 1280 - 20) for n1 in range(10)]
yPosition = [random.randint(0, 1024 - 20) for n2 in range(10)]

def Draw(x, y) :
    global frame
    global temp
    if (temp < x):
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
    else:
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    temp = x
    delay(0.05)

while True:
    # draw 1 -> 2
    for i in range(0, 50, 1):
        t = i / 100
        x = (2 * t ** 2 - 3 * t + 1) * xPosition[0] + (-4 * t ** 2 + 4 * t) * xPosition[1] + (2 * t ** 2 - t) * xPosition[2]
        y = (2 * t ** 2 - 3 * t + 1) * yPosition[0] + (-4 * t ** 2 + 4 * t) * yPosition[1] + (2 * t ** 2 - t) * yPosition[2]
        Draw(x, y)

    # draw 2 -> 3
    # draw 3 -> 4
    # draw 4 -> 5
    # draw 5 -> 6
    # draw 6 -> 7
    # draw 7 -> 8
    # draw 8 -> 9
    # draw 9 -> 10
    # draw 10 -> 1

close_canvas()