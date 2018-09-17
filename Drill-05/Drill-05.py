from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')


def move_1_to_2():
    x1, y1, x2, y2 = 203,535,132,243
    x_plus=x2-x1
    y_plus=y2-y1
    r=y_plus/x_plus
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
    x1, y1, x2, y2 = 132, 243, 535, 470
    x_plus = x2 - x1
    y_plus = y2 - y1
    r = y_plus / x_plus
    frame = 0
    while (x1 < x2):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x1, y1)
        update_canvas()
        frame = (frame + 1) % 8
        x1 += 5
        y1 += 5 * r
        delay(0.05)
        get_events()

def move_3_to_4():
    x1, y1, x2, y2 = 535, 470, 477, 203
    x_plus = x2 - x1
    y_plus = y2 - y1
    r = y_plus / x_plus
    frame = 0
    while (x1 > x2):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x1, y1)
        update_canvas()
        frame = (frame + 1) % 8
        x1 -= 5
        y1 -= 5 * r
        delay(0.05)
        get_events()

def move_4_to_5():
    x1, y1, x2, y2 = 477, 203, 715, 136
    x_plus = x2 - x1
    y_plus = y2 - y1
    r = y_plus / x_plus
    frame = 0
    while (x1 < x2):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x1, y1)
        update_canvas()
        frame = (frame + 1) % 8
        x1 += 5
        y1 += 5 * r
        delay(0.05)
        get_events()

def move_5_to_6():
    x1, y1, x2, y2 = 715, 136, 316, 225
    x_plus = x2 - x1
    y_plus = y2 - y1
    r = y_plus / x_plus
    frame = 0
    while (x1 > x2):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x1, y1)
        update_canvas()
        frame = (frame + 1) % 8
        x1 -= 5
        y1 -= 5 * r
        delay(0.05)
        get_events()

def move_6_to_7():
    x1, y1, x2, y2 = 316, 225, 510, 92
    x_plus = x2 - x1
    y_plus = y2 - y1
    r = y_plus / x_plus
    frame = 0
    while (x1 < x2):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x1, y1)
        update_canvas()
        frame = (frame + 1) % 8
        x1 += 5
        y1 += 5 * r
        delay(0.05)
        get_events()

def move_7_to_8():
    x1, y1, x2, y2 = 510, 92, 692, 518
    x_plus = x2 - x1
    y_plus = y2 - y1
    r = y_plus / x_plus
    frame = 0
    while (x1 < x2):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x1, y1)
        update_canvas()
        frame = (frame + 1) % 8
        x1 += 5
        y1 += 5 * r
        delay(0.05)
        get_events()

def move_8_to_9():
    x1, y1, x2, y2 = 692, 518, 682, 336
    x_plus = x2 - x1
    y_plus = y2 - y1
    r = y_plus / x_plus
    frame = 0
    while (x1 > x2):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x1, y1)
        update_canvas()
        frame = (frame + 1) % 8
        x1 -= 2
        y1 -= 2 * r
        delay(0.05)
        get_events()

def move_9_to_10():
    x1, y1, x2, y2 = 682, 336, 712, 349
    x_plus = x2 - x1
    y_plus = y2 - y1
    r = y_plus / x_plus
    frame = 0
    while (x1 < x2):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x1, y1)
        update_canvas()
        frame = (frame + 1) % 8
        x1 += 5
        y1 += 5 * r
        delay(0.05)
        get_events()

def move_10_to_1():
    x1, y1, x2, y2 = 712, 349, 203, 535
    x_plus = x2 - x1
    y_plus = y2 - y1
    r = y_plus / x_plus
    frame = 0
    while (x1 < x2):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x1, y1)
        update_canvas()
        frame = (frame + 1) % 8
        x1 += 5
        y1 += 5 * r
        delay(0.05)
        get_events()

def move_character():
    #move_1_to_2()
    #move_2_to_3()
    #move_3_to_4()
    #move_4_to_5()
    #move_5_to_6()
    #move_6_to_7()
    #move_7_to_8()
    #move_8_to_9()
    move_9_to_10()
    move_10_to_1()


while True:
    move_character()





close_canvas()
