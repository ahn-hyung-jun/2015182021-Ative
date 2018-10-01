from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def move_character(p1, p2):
    for i in range(0,100+1,2):
        t = i / 100
        x = (1-t)*p1[0]+t*p2[0]
        y = (1-t)*p1[1]+t*p2[1]
        frame = 0
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.05)





size = 20
points = [(random.randint(-500, 500), random.randint(-350, 350)) for i in range(size)]
n = 1

open_canvas(KPU_WIDTH, KPU_HEIGHT)

kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')



while True:
    move_character(points[n-1], points[n])
    n = (n+1)%size


close_canvas()