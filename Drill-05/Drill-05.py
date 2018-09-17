from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')


def move_1_to_2():
    x1, y1, x2, y2 = 203,535,132,243
    x_plus=x2-x1
    y_plus=y2-y1
    r=y_plus//x_plus
    frame = 0
    while(x1>x2):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x1, y1)
        update_canvas()
        frame = (frame + 1) % 8
        x1 -= 5
        y1 -=5*r
        delay(0.05)
        get_events()

def move_2_to_3():
    pass

def move_3_to_4():
    pass

def move_4_to_5():
    pass

def move_5_to_6():
    pass

def move_6_to_7():
    pass

def move_7_to_8():
    pass

def move_8_to_9():
    pass

def move_9_to_10():
    pass

def move_10_to_1():
    pass

def move_character():
    move_1_to_2()
    move_2_to_3()
    move_3_to_4()
    move_4_to_5()
    move_5_to_6()
    move_6_to_7()
    move_7_to_8()
    move_8_to_9()
    move_9_to_10()
    move_10_to_1()


while True:
    move_character()





close_canvas()
