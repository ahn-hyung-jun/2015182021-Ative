from pico2d import *
KPU_WIDTH, KPU_HEIGHT = 1280, 1024
import random



def move_character(x,y):
    clear_canvas()
    global frame
    frame=0
    frame = frame % 8
    frame = frame + 1

    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 0, 100, 100, x, y)
    update_canvas()

def draw_curve_5_points(points, size):

    for i in range(0,size):
       for i in range(0, 100, 2):
           t = i / 100
           x = ((-t ** 3 + 2 * t ** 2 - t) * points[i%11][0] + (3 * t ** 3 - 5 * t ** 2 + 2) * points[(i+1)%11][0] + (
                       -3 * t ** 3 + 4 * t ** 2 + t) * points[(i+2)%11][0] + (t ** 3 - t ** 2) * points[(i+3)%11][0]) / 2
           y = ((-t ** 3 + 2 * t ** 2 - t) * points[i%11][1] + (3 * t ** 3 - 5 * t ** 2 + 2) * points[(i+1)%11][1] + (
                       -3 * t ** 3 + 4 * t ** 2 + t) * points[(i+2)%11][1] + (t ** 3 - t ** 2) * points[(i+3)%11][1]) / 2
           move_character(x, y)


open_canvas(KPU_WIDTH, KPU_HEIGHT)

kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')


p1 = (-300,200)
p2 = (400,350)
p3 = (300,-300)
p4 = (-200,-200)

size=10
points = [(random.randint(-600,600),random.randint(-500,500)) for n in range(size)]

while True:
    draw_curve_5_points(points,size)



close_canvas()