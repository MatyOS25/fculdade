import math, pygame
from collections import namedtuple

# Coordinates
Position = namedtuple('Position', ['x', 'y'])

# Game init
pygame.init()
pygame.font.init()

screenSize = Position(x=800, y=600)
screen = pygame.display.set_mode(screenSize)

# Colors
background = (232, 232, 232)
blue = (41, 59, 136)

# Change title and logo
pygame.display.set_caption('Circulo azul')


def draw_star(screen, color, sides, radius, position):
    points = []

    for n in range(sides * 2):
        rad = radius if n % 2 == 0 else radius // 2
        angle = (n * math.pi / sides) + (90 * math.pi / 60)

        point = (
            int(math.cos(angle) * rad + position[0]),
            int(math.sin(angle) * rad + position[1])
        )

        points.append(point)

    return pygame.draw.polygon(screen, color, points)


# Game loop
running = True
clock = pygame.time.Clock()

while running:
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # paint the screen
    screen.fill(background)

    # draw my star
    draw_star(screen, blue, 5, 100, [screen.get_width() // 2, screen.get_height() // 2])

    # Update the display
    pygame.display.update()
    clock.tick(60)

pygame.display.quit()