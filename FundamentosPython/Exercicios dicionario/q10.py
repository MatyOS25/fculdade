import pygame
from collections import namedtuple

# Coordinates
Position = namedtuple('Position', ['x', 'y'])

# Game init
pygame.init()
pygame.font.init()

screen_size = Position(x=1200, y=720)
screen = pygame.display.set_mode(screen_size)
game_speed = 2

# Colors
background = (232, 232, 0)
red = (153, 5, 31)

# Change title and logo
pygame.display.set_caption('Quadrado vermelho 1.0')

square_position_x = screen.get_width() // 2 - 50
square_position_change_x = 0
square_position_y = screen.get_height() // 2 - 50
square_position_change_y = 0

def draw_square(x, y):
    square = pygame.Rect(x, y, 100, 100)
    pygame.draw.rect(screen, red, square)

# Game loop
running = True
while running:
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                square_position_change_x = -game_speed

            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                square_position_change_x = game_speed

            if event.key == pygame.K_UP or event.key == pygame.K_w:
                square_position_change_y = -game_speed

            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                square_position_change_y = game_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_a:
                square_position_change_x = 0

            if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_w or event.key == pygame.K_s:
                square_position_change_y = 0

    # paint the screen
    screen.fill(background)
    square_position_x += square_position_change_x
    square_position_y += square_position_change_y
    draw_square(square_position_x, square_position_y)
    # Update the display
    pygame.display.update()

pygame.display.quit()