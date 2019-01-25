import tdl

# actual size of the window
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50

LIMIT_FPS = 20  # 20 frames-per-second maximum

tdl.set_font('arial10x10.png', greyscale=True, altLayout=True)

console = tdl.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="Roguelike", fullscreen=False)

tdl.setFPS(LIMIT_FPS)

while not tdl.event.is_window_closed():
    console.draw_char(1, 1, '@', bg=None, fg=(255, 255, 255))

    tdl.flush()
