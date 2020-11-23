import pygame, random

pygame.init()
largura_tela = 800
altura_tela = 600

tempo_inicial = 10 # 10 segundos

#Variavel para contar quantas esperas de 50Hz ou 0,02s
conta_clocks = 0
#Conta quantos quadradinhos clicou
pontos = 0
#Variavel para contar regressivamente os quantos segundos se passaram
conta_segundos = tempo_inicial

lightBlue = (11, 158, 217)
blue = (3, 44, 166)
darkBlue = (2, 24, 89)
white = (255,255,255)
black = (0,0,0)
pink = (242, 92, 162)
cores = [lightBlue, blue, darkBlue, white, pink] 

tela = pygame.display.set_mode((largura_tela, altura_tela))

clock = pygame.time.Clock()

tela.fill(black)

#Para imprimir o texto com o tempo e a pontuação corrente
def mostra_tempo(tempo, pontos):
    font = pygame.font.Font(None, 24)
    text = font.render("Tempo: " + str(tempo) + "s | Pontuação: " + str(pontos), 1, white)
    textpos = text.get_rect(centerx=tela.get_width()//2)
    tela.blit(text, textpos)

def gera_cor_aleatoria():
    return (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))


def gera_posicao_aleatoria():
    return (random.randint(0, largura_tela - 20),random.randint(0, altura_tela -20))

terminou = False
while not terminou:
	# Checar os eventos do mouse aqui
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:    
            #Obtem as coordenadas do mouse na tela
            pos = pygame.mouse.get_pos()
            #Checa se clicou em algum dos quadrados
            for q in lista:
                if q.collidepoint(pos):
                    #efeito.play()
                    lista.remove(q)
                    pontos = pontos + 1
        if event.type == pygame.QUIT:
            terminou = True
    
    conta_clocks = conta_clocks + 1
    
    #A cada 50 cont_clocks, temos 1s (0,02s x 50 = 1s)
    if conta_clocks == 50:
        if conta_segundos >= 0:
            conta_segundos = conta_segundos - 1
        conta_clocks = 0
        if conta_segundos >= 0: # Neste caso, ainda tem tempo 
            #Limpar tela para atualizar o texto
            tela.fill(black)
            lista = []
            for i in range(0,20):
                x,y = gera_posicao_aleatoria()
                q = pygame.Rect(x, y, 20,20)
                pygame.draw.rect(tela, gera_cor_aleatoria(), q)
                lista.append(q)
            #Mostra o tempo atualizado
            mostra_tempo(conta_segundos, pontos)
        else:
            terminou = True

    # Atualiza o desenho na tela
    pygame.display.update()
    # Configura 50 atualizações de tela por segundo
    clock.tick(50)
# Finaliza a janela do jogo
pygame.display.quit()
# Finaliza o pygame
pygame.quit()