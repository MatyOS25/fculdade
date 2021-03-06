import pygame
from collections import namedtuple

# Coordinates
Position = namedtuple('Position', ['x', 'y'])

# Game init
pygame.init()
pygame.font.init()

screen_size = Position(x=800, y=600)
screen = pygame.display.set_mode(screen_size)
game_speed = 1
square_size = 50

# Colors
background = (232, 232, 232)
color = (100, 0, 75)

# Change title and logo
pygame.display.set_caption('Quadrado Mouse')

square_position_x = screen.get_width() // 2 - square_size
square_position_y = screen.get_height() // 2 - square_size

square_move_to_position_x = screen.get_width() // 2 - square_size
square_move_to_position_y = screen.get_height() // 2 - square_size


def draw_square(position, width=50, height=50):
    square = pygame.Rect(position.x, position.y, width, height)
    pygame.draw.rect(screen, color, square)


# Game loop
running = True
clock = pygame.time.Clock()

while running:
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            click_position = pygame.mouse.get_pos()
            square_move_to_position_x = click_position[0]
            square_move_to_position_y = click_position[1]

    # paint the screen
    screen.fill(background)

    if square_position_x != square_move_to_position_x:
        square_position_x += game_speed if square_move_to_position_x > square_position_x else -game_speed

    if square_position_y != square_move_to_position_x:
        square_position_y += game_speed if square_move_to_position_y > square_position_y else -game_speed

    draw_square(Position(x=square_position_x, y=square_position_y), square_size, square_size)

    # Update the display
    pygame.display.update()
    clock.tick(60)

pygame.display.quit()