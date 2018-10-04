from pico2d import *
KPU_WIDTH, KPU_HEIGHT = 1280, 1024
import random


def move_character(x,y):
    pass

def draw_curve_5_points(p1, p2, p3, p4, p5):

    # draw p1-p2
    for i in range(0, 50, 2):
        t = i / 100
        x = (2*t**2-3*t+1)*p1[0]+(-4*t**2+4*t)*p2[0]+(2*t**2-t)*p3[0]
        y = (2*t**2-3*t+1)*p1[1]+(-4*t**2+4*t)*p2[1]+(2*t**2-t)*p3[1]
        move_character(x, y)

    # draw p2-p3
    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p1[0] + (3*t**3 - 5*t**2 + 2)*p2[0] + (-3*t**3 + 4*t**2 + t)*p3[0] + (t**3 - t**2)*p4[0])/2
        y = ((-t**3 + 2*t**2 - t)*p1[1] + (3*t**3 - 5*t**2 + 2)*p2[1] + (-3*t**3 + 4*t**2 + t)*p3[1] + (t**3 - t**2)*p4[1])/2
        move_character(x, y)

    # draw p3-p4
    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p2[0] + (3*t**3 - 5*t**2 + 2)*p3[0] + (-3*t**3 + 4*t**2 + t)*p4[0] + (t**3 - t**2)*p5[0])/2
        y = ((-t**3 + 2*t**2 - t)*p2[1] + (3*t**3 - 5*t**2 + 2)*p3[1] + (-3*t**3 + 4*t**2 + t)*p4[1] + (t**3 - t**2)*p5[1])/2
        move_character(x, y)

    # draw p4-p5
    for i in range(50, 100, 2):
        t = i / 100
        x = (2 * t ** 2 - 3 * t + 1) * p3[0] + (-4 * t ** 2 + 4 * t) * p4[0] + (2 * t ** 2 - t) * p5[0]
        y = (2 * t ** 2 - 3 * t + 1) * p3[1] + (-4 * t ** 2 + 4 * t) * p4[1] + (2 * t ** 2 - t) * p5[1]
        move_character(x, y)



open_canvas(KPU_WIDTH, KPU_HEIGHT)

kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')


p1 = (-300,200)
p2 = (400,350)
p3 = (300,-300)
p4 = (-200,-200)


points = [(random.randint(-600,600),random.randint(-500,500)) for n in range(10)]
while True:
 draw_curve_5_points(p1, p2, p3, p4, p1)

close_canvas()