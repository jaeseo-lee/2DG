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
    delay(0.03)

while True:
    # draw 1 -> 2
    for i in range(0, 50, 1):
        t = i / 100
        x = (2 * t ** 2 - 3 * t + 1) * xPosition[0] + (-4 * t ** 2 + 4 * t) * xPosition[1] + (2 * t ** 2 - t) * xPosition[2]
        y = (2 * t ** 2 - 3 * t + 1) * yPosition[0] + (-4 * t ** 2 + 4 * t) * yPosition[1] + (2 * t ** 2 - t) * yPosition[2]
        Draw(x, y)
    frame = 0

    # draw 2 -> 3
    for i in range(0, 100, 1):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * xPosition[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * xPosition[1] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * xPosition[2] + (t ** 3 - t ** 2) * xPosition[3]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * yPosition[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * yPosition[1] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * yPosition[2] + (t ** 3 - t ** 2) * yPosition[3]) / 2
        Draw(x, y)

    frame = 0

    # draw 3 -> 4
    for i in range(0, 100, 1):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * xPosition[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * xPosition[2] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * xPosition[3] + (t ** 3 - t ** 2) * xPosition[4]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * yPosition[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * yPosition[2] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * yPosition[3] + (t ** 3 - t ** 2) * yPosition[4]) / 2
        Draw(x, y)

    frame = 0

    # draw 4 -> 5
    for i in range(0, 100, 1):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * xPosition[2] + (3 * t ** 3 - 5 * t ** 2 + 2) * xPosition[3] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * xPosition[4] + (t ** 3 - t ** 2) * xPosition[5]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * yPosition[2] + (3 * t ** 3 - 5 * t ** 2 + 2) * yPosition[3] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * yPosition[4] + (t ** 3 - t ** 2) * yPosition[5]) / 2
        Draw(x, y)

    frame = 0

    # draw 5 -> 6
    for i in range(0, 100, 1):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * xPosition[3] + (3 * t ** 3 - 5 * t ** 2 + 2) * xPosition[4] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * xPosition[5] + (t ** 3 - t ** 2) * xPosition[6]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * yPosition[3] + (3 * t ** 3 - 5 * t ** 2 + 2) * yPosition[4] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * yPosition[5] + (t ** 3 - t ** 2) * yPosition[6]) / 2
        Draw(x, y)

    frame = 0

    # draw 6 -> 7
    for i in range(0, 100, 1):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * xPosition[4] + (3 * t ** 3 - 5 * t ** 2 + 2) * xPosition[5] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * xPosition[6] + (t ** 3 - t ** 2) * xPosition[7]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * yPosition[4] + (3 * t ** 3 - 5 * t ** 2 + 2) * yPosition[5] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * yPosition[6] + (t ** 3 - t ** 2) * yPosition[7]) / 2
        Draw(x, y)

    frame = 0

    # draw 7 -> 8
    for i in range(0, 100, 1):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * xPosition[5] + (3 * t ** 3 - 5 * t ** 2 + 2) * xPosition[6] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * xPosition[7] + (t ** 3 - t ** 2) * xPosition[8]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * yPosition[5] + (3 * t ** 3 - 5 * t ** 2 + 2) * yPosition[6] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * yPosition[7] + (t ** 3 - t ** 2) * yPosition[8]) / 2
        Draw(x, y)

    frame = 0

    # draw 8 -> 9
    for i in range(0, 100, 1):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * xPosition[6] + (3 * t ** 3 - 5 * t ** 2 + 2) * xPosition[7] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * xPosition[8] + (t ** 3 - t ** 2) * xPosition[9]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * yPosition[6] + (3 * t ** 3 - 5 * t ** 2 + 2) * yPosition[7] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * yPosition[8] + (t ** 3 - t ** 2) * yPosition[9]) / 2
        Draw(x, y)

    frame = 0

    # draw 9 -> 10
    for i in range(0, 100, 1):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * xPosition[7] + (3 * t ** 3 - 5 * t ** 2 + 2) * xPosition[8] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * xPosition[9] + (t ** 3 - t ** 2) * xPosition[9]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * yPosition[7] + (3 * t ** 3 - 5 * t ** 2 + 2) * yPosition[8] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * yPosition[9] + (t ** 3 - t ** 2) * yPosition[9]) / 2
        Draw(x, y)

    frame = 0

    # draw 10 -> 1
    for i in range(50, 100, 1):
        t = i / 100
        x = (2 * t ** 2 - 3 * t + 1) * xPosition[8] + (-4 * t ** 2 + 4 * t) * xPosition[9] + (2 * t ** 2 - t) * xPosition[0]
        y = (2 * t ** 2 - 3 * t + 1) * yPosition[8] + (-4 * t ** 2 + 4 * t) * yPosition[9] + (2 * t ** 2 - t) * yPosition[0]
        Draw(x, y)

close_canvas()