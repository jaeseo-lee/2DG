from pico2d import *
import math
import os
open_canvas()

		       
os.getcwd()     
os.chdir('C:\\2DGP\\2018-2DGP\\Labs\\Lecture03')
		       
os.getcwd()
		       
grass = load_image('grass.png')
character = load_image('character.png')
def left_right():
        x = 40
        y = 0
        while (x < 760):
                clear_canvas_now()
                grass.draw_now(400,30)
                character.draw_now(x, 90)
                x = x + 2
                delay(0.002)
def south_north():
        x = 0
        y = 0
        while (y + 90 <= 540):
                clear_canvas_now()
                grass.draw_now(400,30)
                character.draw_now(760, 90 + y)
                y = y + 2
                delay(0.002)
def right_left():
        x = 760
        while(40 <= x):
                clear_canvas_now()
                grass.draw_now(400,30)
                character.draw_now(x, 540)
                x = x - 2
                delay(0.002)
def north_south():
        y = 540
        while(y >= 90):
                clear_canvas_now()
                grass.draw_now(400,30)
                character.draw_now(40, y)
                y = y - 2
                delay(0.002)
def right_down():
        x = 400
        y = 90
        delta = 0
        r = 200
        while (x < 800 and y < 300) :
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            x = x + 4
            delta = math.sqrt((400 - x)**2 + (300 - y)**2) 
            y = y + (delta - r)
            if (x > 800) :
                x = 800
            delay(0.002)

def right_up():
        x = 800
        y = 300
        delta = 0
        r = 200
        while (x > 400 and y < 600) :
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            y = y + 4
            delta = math.sqrt((400 - x)**2 + (300 - y)**2)
            if ( r > delta) :
                x = x - (r - delta)
            else :
                x = x - (delta - r)
            delay(0.002)

def left_up():
        x = 400
        y = 600
        delta = 0
        r = 200
        while (x > 0 and y > 300) :
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            x = x - 4
            delta = math.sqrt((400 - x)**2 + (300 - y)**2) 
            if ( r > delta) :
                y = y - (r - delta)
            else :
                y = y - (delta - r)
            delay(0.002)

def left_down():
        x = 200
        y = 300
        delta = 0
        r = 200
        while (x < 400 and y > 90) :
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            x = x + 30
            delta = math.sqrt((400 - x)**2 + (300 - y)**2)
            if ( r > delta) :
                y = y - (r - delta)
            else :
                y = y - (delta - r)
            
while (True):
       left_right()
       south_north()
       right_left()
       north_south()
       x = 40
       y = 0
       while (x < 400):
                clear_canvas_now()
                grass.draw_now(400,30)
                character.draw_now(x, 90)
                x = x + 2
                delay(0.002)
       right_down() 
       right_up()
       left_up()
       left_down()
        
close_canvas()
