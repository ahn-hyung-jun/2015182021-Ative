import game_framework
from pico2d import *
import main_state
import title_state


name = "Pouse_state"
image = None


def enter():
    global image
    image = load_image('pause.png')


def exit():
    global image
    del(image)

global time
time = 0

def update():
    global time
    time = time + 1
    delay(0.3)

def draw():
    global image
    clear_canvas()
    if time%2 == 0:
        image.draw(400, 300)
    main_state.grass.draw()
    main_state.boy.draw()
    update_canvas()






def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_state()

def pause(): pass


def resume(): pass




