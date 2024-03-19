#Nota do aluno : Estimado professor como solicitado devo falar qual
#nota pretendo alcançar , acredito que pelo esforço de desenhar a pista e desenhar a Nave
#apesar de não ser uma pista que faça um lopping e a movimentação da Nave não ter sido
# complemtamente fluida acredito que uma nota de (90) seja o suficiente desde já
#agradeço a sua consideração 
import pygame, sys
from pygame.locals import *
from math import cos, sin, pi

pygame.init()

naveImageRight = pygame.image.load("naveRight.png")
naveImageTop = pygame.image.load("naveTop.png")
naveImageLeft = pygame.image.load("naveLeft.png")
naveImageBottom = pygame.image.load("naveBottom.png")


musica_de_fundo = pygame.mixer.music.load('arcade-party.mp3')
pygame.mixer.music.play(-1)

largura = 532
altura  = 410
tamanho = (largura, altura)
janela  = pygame.display.set_mode(tamanho)
pygame.display.set_caption('Car Race do Paulo')

frame_rate = 10

clock = pygame.time.Clock()

pista = pygame.image.load("circuito_51247.jpg")
carro = naveImageRight


t=0.0

font_size = 25
font = pygame.font.Font(None, font_size)
antialias = True 
WHITE = (255, 255, 255)

def parametrizacao (t):
    global carro

    if t >= 0:
        carro = naveImageRight
        resultado=(40,225)
        
    if 0 < t <= 0.5:
        carro = naveImageRight
        resultado=(40+150*t, 225-40*t)
        # Velocidade de 0.5

    if 0.5 < t <=1.7:
        carro = naveImageTop
        variacao_de_x = 40 * cos(2 * (t -1.17))
        variacao_de_y = 60 * sin(2 * (t -1.17))
        resultado = (90 + variacao_de_x, 150 - variacao_de_y)
         # Velocidade de 1.2

    if 1.7 < t <= 2.3:
        carro = naveImageRight
        variacao_de_x = 60 * cos((-1.17 + t))
        variacao_de_y = 90 * sin((-1.17 + t))
        resultado = (90 + variacao_de_x, 150 - variacao_de_y)
        # Velocidade de 0.6

    if 2.3 < t <= 2.5:
        carro = naveImageRight
        resultado = (160 + 150 * (t - 2.3), 70)
        # Velocidade de 0.2

    if 2.5 < t <= 3:
        carro = naveImageBottom
        variacao_de_x = 100 * cos(2 * (t - 3))
        variacao_de_y = 30 * sin(2 * (t - 3))
        resultado = (125 + variacao_de_x, 100 + variacao_de_y)
        # Velocidade de 0.5
     

    if 3 < t <= 4.7:
        carro = naveImageBottom
        variacoes =  50 * (t - 3)  
        resultado = (225 + variacoes, 100 + variacoes)
        # Velocidade de 1.7


    if 4.7 < t <= 5.2:
        carro = naveImageLeft
        variacao_de_x = 40 * cos(3 * (t - 4.7))
        variacao_de_y = 100 * sin(3 * (t - 4.7))
        resultado = (278 + variacao_de_x, 180 + variacao_de_y)
        # Velocidade de 0.5

    if 5.2 < t <= 5.7:
        carro = naveImageTop
        variacao_de_x = 68 * cos(3 * (t - 4.7))
        variacao_de_y = 100 * sin(3 * (t - 4.7))
        resultado = (260 + variacao_de_x, 180 + variacao_de_y)
        # Velocidade de 0.5


    if 5.7 < t <= 6.2:
        carro = naveImageTop
        variacao_de_x = 100 * cos(3 * (t - 4.7))
        variacao_de_y = 100 * sin(3 * (t - 4.7))
        resultado = (300 + variacao_de_x, 180 + variacao_de_y)
        # Velocidade de 0.5

    if 6.2 < t <= 6.9:
        carro = naveImageRight
        variacao_de_x = 137 * cos(3 * (t - 4.7))
        variacao_de_y = 100 * sin(3 * (t - 4.7))
        resultado = (300 + variacao_de_x, 170 + variacao_de_y)
        # Velocidade de 0.7
    
 
    return resultado 

while True:
    tempo = font.render(f"t={t:.2f}", antialias, WHITE)
    janela.blit(pista, (0, 0))  #(B) se descomentar aqui (e comentar (A)) vejo movimento
    janela.blit(carro, parametrizacao(t))
    janela.blit(tempo, (10, 10))
    pygame.display.update()
    clock.tick(frame_rate)
    t=t+0.1
    

    
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()


        elif event.type== pygame.MOUSEBUTTONUP and event.button == 1:
            t = 0
