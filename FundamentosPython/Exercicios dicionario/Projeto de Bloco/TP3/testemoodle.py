import pygame
import psutil
import cpuinfo

# Obtém informações da CPU
info_cpu = cpuinfo.get_cpu_info()
# Cores:
preto = (0, 0, 0)
branco = (255, 255, 255)
cinza = (100, 100, 100)
vermelho = (255,0,0)
azul = (0,0,255)

# Iniciando a janela principal
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Informações de CPU")
pygame.display.init()
# Superfície para mostrar as informações:
s1 = pygame.surface.Surface((largura_tela, altura_tela))

# Para usar na fonte
pygame.font.init()
font = pygame.font.Font(None, 24)
    
# Cria relógio
clock = pygame.time.Clock()
# Contador de tempo
cont = 60
core = psutil.cpu_percent(interval=1, percpu=True)
def mostra_uso_cpu(s, l_cpu_percent):
    s.fill(cinza)
    num_cpu = len(l_cpu_percent)
    x = y = 10
    desl = 10
    alt = s.get_height() - 2*y
    larg = (s.get_width()-2*y - (num_cpu+1)*desl)/num_cpu
    d = x + desl
    l_cpu_percent = psutil.cpu_percent(interval=1, percpu=True)
    for i in l_cpu_percent:
                pygame.draw.rect(s, vermelho, (d, y, larg, alt))
                pygame.draw.rect(s, azul, 	(d, y, larg, (1-i/100)*alt))
                d = d + larg + desl
    # parte mais abaixo da tela e à esquerda
    tela.blit(s, (0, altura_tela/5))

terminou = False
# Repetição para capturar eventos e atualizar tela
while not terminou:
    # Checar os eventos do mouse aqui:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminou = True

    # Fazer a atualização a cada segundo:
    if cont == 60:
            mostra_uso_cpu(s1,core)
            cont = 0

    # Atualiza o desenho na tela
    pygame.display.update()

    # 60 frames por segundo
    clock.tick(60)
    cont = cont + 1

# Finaliza a janela
pygame.display.quit()