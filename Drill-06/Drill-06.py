from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

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
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                mx, my = event.x, KPU_HEIGHT -1 -event.y

def move_character():
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
frame = 0

while running:
    handle_events()
    move_character()
    make_cursor()


close_canvas()
