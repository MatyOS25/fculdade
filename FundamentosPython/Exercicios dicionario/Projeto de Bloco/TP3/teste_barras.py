import pygame
import psutil
from collections import namedtuple
import platform
import cpuinfo


# Game init
pygame.init()
pygame.font.init()
font = pygame.font.Font(None, 24)

# Coordinates
Coordinate = namedtuple('Coordinate', ['x', 'y'])

# Configs
screenSize = Coordinate(x=800, y=600)
screen = pygame.display.set_mode(screenSize)

info = cpuinfo.get_cpu_info()

# Change title
pygame.display.set_caption('Monitoring System')

core = psutil.cpu_percent(interval=1, percpu=True)
# Colors
background = (232,232,232)
backgroundContrast = (196,182,182)
darkBlue = (48,71,94)
white = (255,255,255)
black = (0,0,0)
darkGrey = (53,56,57)
blueWater = (127,255,213)
red = (240,84,84)
Roxo = (75,0,130)
LightGrey = (34,40,49)
colors = [background, black, darkBlue, darkGrey, white]

def memory_usage():
    memory = psutil.virtual_memory()
    memory_total = round(psutil.virtual_memory().total/(1024*1024*1024), 2)

    width = screen.get_width() - 2 * 20
    percentage_used = width * memory.percent/100

    pygame.draw.rect(screen, LightGrey, (20, 50, width, 45))
    pygame.draw.rect(screen, Roxo, (20, 50, percentage_used, 45))
    text = font.render(f"Uso de memória (total: {str(memory_total)}GB): {memory.percent}%", 1, darkBlue)
    screen.blit(text, (20, 30))

def cpu_usage():
    cpu_percent = psutil.cpu_percent(interval=1)
    cpu_freq = round(psutil.cpu_freq().current/1000,1)
    width = screen.get_width() - 2 * 20
    percentage_used = width * cpu_percent/100

    pygame.draw.rect(screen, LightGrey, (20, 170, width, 45))
    pygame.draw.rect(screen, Roxo, (20, 170, percentage_used, 45))
    text = font.render(f"Uso de CPU: {cpu_percent}%", 1, darkGrey)
    screen.blit(text, (20, 150))
    text5 = font.render(f"Atual: {cpu_freq}Ghz", 1, darkGrey)
    screen.blit(text5, (200, 150))
    text1 = font.render(f"Processador: {platform.processor()}.", 1, darkGrey)
    screen.blit(text1, (20, 250))
    text1 = font.render(f"Processador: {info['brand_raw']}.", 1, darkGrey)
    screen.blit(text1, (20, 230))
    text5 = font.render(f"Arquitetura: {info['arch']}.", 1, darkGrey)
    screen.blit(text5, (600, 230)) 
    text5 = font.render(f"Núcleos: {psutil.cpu_count()} ({psutil.cpu_count(logical=False)}).", 1, darkGrey)
    screen.blit(text5, (500, 230))
    text2 = font.render(f"Node: {platform.node()}.", 1, darkGrey)
    screen.blit(text2, (20, 270))
    text4 = font.render(f"Sistema: {platform.system()} ({platform.platform()}).", 1, darkGrey)
    screen.blit(text4, (20, 290))

core = psutil.cpu_percent(interval=1, percpu=True)
def mostra_uso_cpu(s, l_cpu_percent):
    s.fill(LightGrey)
    num_cpu = len(l_cpu_percent)
    x = y = 10
    desl = 10
    alt = s.get_height() - 2*y
    larg = (s.get_width()-2*y - (num_cpu+1)*desl)/num_cpu
    d = x + desl
    l_cpu_percent = psutil.cpu_percent(interval=1, percpu=True)
    for i in l_cpu_percent:
                pygame.draw.rect(s, darkGrey, (d, y, larg, alt))
                pygame.draw.rect(s, blueWater, 	(d, y, larg, (1-i/100)*alt))
                d = d + larg + desl
    # parte mais abaixo da tela e à esquerda
    screen.blit(s, (0, 600/5))

def cpu_info():
    info = cpuinfo.get_cpu_info()
    for i in info:
        print(i, ":", info[i])
    
def disk_usage():
    hard_drive = psutil.disk_usage('.')
    hard_drive_percent = hard_drive.percent

    width = screen.get_width() - 2 * 20
    percentage_used = width * hard_drive_percent/100

    pygame.draw.rect(screen, LightGrey, (20, 375, width, 45))
    pygame.draw.rect(screen, Roxo, (20, 375, percentage_used, 45))
    text = font.render(f"Uso de Disco: {hard_drive_percent}%", 1, darkBlue)
    screen.blit(text, (20, 355))
    diskusage = psutil.disk_usage('/')
    total = (f"Total:  {round(diskusage.total/(1024*1024*1024), 2)}GB")
    text = font.render(total , 1, darkBlue)
    screen.blit(text, (450, 430))
    emuso = (f"Em uso: {round(diskusage.used/(1024*1024*1024), 2)}GB")
    text1 = font.render(emuso, 1, darkBlue)
    screen.blit(text1, (20, 430))
    livre = (f"Livre: {round(diskusage.free/(1024*1024*1024), 2)}GB")
    text2 = font.render(livre, 1, darkBlue)
    screen.blit(text2, (600, 430))

def draw_ip_info():
    addr = psutil.net_if_addrs()['Ethernet'][0].address
    ip = psutil.net_if_addrs()['Ethernet'][1].address
    text = font.render(f"Seu IP é: {addr}", 1, darkGrey)
    screen.blit(text, (20, 550))
    text = font.render(f"IPV4 é: {ip}", 1, darkGrey)
    screen.blit(text, (20, 575))




# Game loop
running = True
clock = pygame.time.Clock()
counter = 0

while running:
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    if counter == 60:
        # paint the screen
        screen.fill(blueWater)
        mostra_uso_cpu(screen, core)

        counter = 0

    # Update the display
    pygame.display.update()

    # Update the display
    clock.tick(150)
    counter += 1

pygame.display.quit()