import pygame, sys, random
from collections import namedtuple



class Quadradro_Aleatorio:
    # Coordinates
    Coordinate = namedtuple('Coordinate', ['x', 'y'])
    running = True
    background = (234, 234, 234)
    red = (245, 0, 130)

    squares = []

    def __init__(mygame):
        # Game init
        pygame.init()

        mygame.screenSize = mygame.Coordinate(x=800, y=600)
        mygame.screen = pygame.display.set_mode(mygame.screenSize)

        # Change title
        pygame.display.set_caption('Q7')

        # main loop
        mygame.loop()

    def loop(mygame):
        # Game loop
        while mygame.running:
            # events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mygame.handle_quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mygame.handle_mouse(event)
                if event.type == pygame.KEYDOWN:
                    mygame.handle_key_down(event)

            # paint the screen
            mygame.screen.fill(mygame.background)

            for square in mygame.squares:
                pygame.draw.rect(mygame.screen, mygame.red, square)

            # Update the display
            pygame.display.update()

        pygame.display.quit()

    def handle_quit(mygame):
        mygame.running = False
        sys.exit()

    def handle_key_down(mygame, event):
        if event.key == pygame.K_SPACE:
            mygame.squares.append(mygame.draw_square())

    def handle_mouse(mygame, event):
        if event.button == 3:
            mygame.squares.append(mygame.draw_square())

    def draw_square(mygame):
        x = random.randint(25, mygame.screen.get_width() - 25)
        y = random.randint(25, mygame.screen.get_height() - 25)

        return pygame.Rect(x, y, 50, 50)


game = Quadradro_Aleatorio()