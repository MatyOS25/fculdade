import psutil
import pygame
from collections import namedtuple

# Game init
pygame.init()
pygame.font.init()
font = pygame.font.Font(None, 32)

# Coordinates
Coordinate = namedtuple('Coordinate', ['x', 'y'])
x = 1200
y = 720

tela_tamanho = Coordinate(x, y)
screen = pygame.display.set_mode(tela_tamanho)

# Colors
background = (232,232,232)
backgroundContrast = (196,182,182)
darkBlue = (48,71,94)
white = (255,255,255)
black = (0,0,0)
darkGrey = (34,40,49)
red = (240,84,84)

def draw_memory_usage(self, position: Coordinate, color):
    """
    Este método desenha no pygame o grafico em barra do uso de memória
    """
    pass

def draw_cpu_usage(self, position: Coordinate, color):
    """
    Este método desenha no pygame o grafico em barra do uso de memória
    """
    pass

def draw_cpu_info(self, position: Coordinate, color):
    """
    Este método desenha no pygame o grafico em barra do uso de memória
    """
    pass

def draw_disk_usage(self, position: Coordinate, color):
    """
    Este método desenha no pygame o grafico em barra do uso de memória
    """
    pass

def draw_ip_info(self, position: Coordinate, color):
    """
    Este método desenha no pygame o IP atual do usuário
    """
    addr = psutil.net_if_addrs()['en0'][0].address
    text = font.render(f"Seu IP é: {addr}", 1, darkGrey)
    screen.blit(text, (20, 150))

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

    # Update the display
    pygame.display.update()

    # Update the display
    clock.tick(150)

pygame.display.quit()