import random
import json
import os

from pico2d import *

import game_framework
from map import Map
import hero

name = "MainState"

maps = None

def enter():
    global maps
    maps = [[Map(i,j) for i in range(100)] for j in range(100)]

def exit():
    pass



def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            pass


def update():
    pass

def draw():
    clear_canvas()

    for i in range(100):
        for j in range(100):
            maps[j][i].draw()
    update_canvas()




