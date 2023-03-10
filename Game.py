

import pygame
from math import *
from Corpo import Corpo
import random

pygame.init()

WIDTH = 1200
HEIGTH = 600

AMARELO = (255, 255, 0)
VERMELHO = (255, 0, 0)

BACKGROUND = pygame.image.load('pexels-limonovich-9166321.jpg')

G = 1
txt_format = 0
TELA = pygame.display.set_mode((WIDTH, HEIGTH), vsync=1)
fonte = pygame.font.SysFont('arial', 20, True, True)

corpo = Corpo(1000, AMARELO, 1200/2, 600 / 2, 0, 0, 110)
corpo2 = Corpo(1000, VERMELHO, corpo.pos_x + corpo.radios + 30, corpo.pos_y, 0, 2.719, 10)

star_x = 12
star_y = 70

CLOCK = pygame.time.Clock()

def gravidade():
    hip = sqrt((corpo.pos_x - corpo2.pos_x) ** 2 + (corpo.pos_y - corpo2.pos_y) ** 2)
    
    if hip < 1:
        hip = 1
    
    produto_massas = corpo.massa * corpo2.massa
    produto_distancia = hip ** 2
    
    forca = G * produto_massas / produto_distancia
    
    sen = (corpo.pos_y - corpo2.pos_y) / hip
    coss = (corpo.pos_x - corpo2.pos_x) / hip
    
    fx = coss  * forca 
    fy = sen  * forca 
    
    acel_x = fx / corpo2.massa
    acel_y = fy / corpo2.massa
    
    acel_geral = sqrt(acel_x ** 2 + acel_y ** 2)
    
    corpo2.defini_aceleracao(acel_x, acel_y)
    colisao(hip)
    corpo2.pint_corpo(TELA)
    
    corpo.pint_corpo(TELA)
    
    velocida_geral = sqrt((corpo2.velocidade_x) ** 2 + (corpo2.velocidade_y) ** 2)
    
    txt_format = fonte.render(f'Distancia: {hip:,.2f} || Força: {forca:,.2f} || Aceleraçao x: {acel_x:,.2f} || Aceleraçao y: {acel_y:,.2f} || Aceleração Geral: {acel_geral:,.5f}', True, (255, 255, 255))
    txt_format2 = fonte.render(f'Velocidade x: {corpo2.velocidade_x:,.2f} || Velocidade y: {corpo2.velocidade_x:,.2f} || Velocidade Geral: {velocida_geral:,.2f}', True, (255, 255, 255))
    
    TELA.blit(txt_format, (10, 10))
    TELA.blit(txt_format2, (10, 40))
    
    
    
def colisao(hip):
        if(hip < corpo.radios + corpo2.radios):
            corpo2.pos_x = corpo2.pos_x
            corpo2.pos_y = corpo2.pos_y
            corpo2.velocidade_x = 0
            corpo2.velocidade_y = 0
            corpo2.aceleracao_x = 0
            corpo2.aceleracao_y = 0
        
while True:
    TELA.fill((0, 0, 0))
    BACKGROUND  = pygame.transform.scale(BACKGROUND, (1200, 600))
    
    TELA.blit(BACKGROUND, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        pygame.draw.line(TELA, (0, 255, 0), (corpo.pos_x, corpo.pos_y), (corpo2.pos_x, corpo2.pos_y))
    
    for i in range(1000):
        pygame.draw.circle(TELA, (255, 255, 255), (star_x, star_x), 1)
    
    gravidade()
    
    CLOCK.tick(60)
    
    pygame.display.update()
    
