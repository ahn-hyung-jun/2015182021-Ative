from pico2d import *
import random

# Game object class here

class Grass:
    def __init__(self):
        self.image=load_image('grass.png')

    def draw(self):
        self.image.draw(400,30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100,700),90
        self.image=load_image('run_animation.png')
        self.frame = random.randint(0,7)

    def update(self):
        self.frame = (self.frame + 1)%8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100,0,100,100,self.x,self.y)

class Ball:
    def __init__(self):
        self.x, self.y = random.randint(100,700),0
        self.speed = random.randint(10,20)
        self.ball_size = random.randint(0,1)

    def update(self):
        if(self.ball_size == 0):
            self.image = load_image('ball41x41.png')
        elif(self.ball_size == 1):
            self.image = load_image('ball21x21.png')

        self.y = self.y - self.speed
    








def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas()

boy = Boy()
team = [Boy() for i in range(11)]
grass = Grass()

running = True;

# game main loop code
while running:
    handle_events()
    for boy in team:
        boy.update()
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    update_canvas()
    delay(0.05)

# finalization code
close_canvas()