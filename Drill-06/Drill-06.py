from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

global cx, cy

def handle_events():
    global running
    global x, y
    global mx, my
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event. type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running=False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, KPU_HEIGHT -1 -event.y
            make_cursor()
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                mx, my = event.x, KPU_HEIGHT -1 -event.y
                move_character()

def move_character():
    move_to_right()
    move_to_left()

def move_to_right():
    x1, y1, x2, y2 = cx, cy, mx, my
    if(x1<x2):
        x_plus = x2 - x1
        y_plus = y2 - y1
        r = y_plus / x_plus
        frame = 0
        while (x1 < x2):
            clear_canvas()
            kpu_ground.draw(KPU_WIDTH//2, KPU_HEIGHT//2)
            character.clip_draw(frame * 100, 0, 100, 100, x1, y1)
            update_canvas()
            frame = (frame + 1) % 8
            x1 += 5
            y1 += 5 * r
            delay(0.05)
            handle_events()

def move_to_left():
    pass

def make_cursor():
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH/2,KPU_HEIGHT/2)
    hand_arrow.draw(x, y)
    update_canvas()
    delay(0.05)
    handle_events()



open_canvas(KPU_WIDTH, KPU_HEIGHT)

kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

running=True



while running:
    handle_events()






close_canvas()
