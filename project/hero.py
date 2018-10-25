import random
import json
import os

from pico2d import *

import game_framework

class hero:
    def __init__(self):
        self.x, self.y = 800 // 2, 90
        self.state = 0
        self.dir = 0
        self.hor_speed, self.ver_speed = 0
        self.image = load_image('animation_sheet.png')

    def move_character(self):
        pass


