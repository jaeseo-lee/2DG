import game_framework
import pico2d
import main_state
import start_state
pico2d.open_canvas(600, 800, sync=True)
game_framework.run(main_state)
pico2d.close_canvas()