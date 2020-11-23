import pygame
from collections import namedtuple

# Coordinates
Position = namedtuple('Position', ['x', 'y'])

# Game init
pygame.init()
pygame.font.init()

screenSize = Position(x=800, y=600)
screen = pygame.display.set_mode(screenSize)

# Colors
background = (232,232,232)
blue = (41,59,136)

# Change title and logo
pygame.display.set_caption('Círculo Azul')

def draw_circle():
    pygame.draw.circle(screen, blue, (screen.get_width() // 2, screen.get_height() // 2), 50)

# Game loop
running = True
while running:
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # paint the screen
    screen.fill(background)

    draw_circle()

    # Update the display
    pygame.display.update()

pygame.display.quit()