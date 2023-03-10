
import pygame

pygame.init()

class Corpo:
    def __init__(self, massa, cor, posx, posy, velx, vely, radios):
        self.massa = massa
        self.radios = radios
        self.cor = cor
        self.pos_x = posx
        self.pos_y = posy
        self.velocidade_x = velx
        self.velocidade_y = vely
        self.aceleracao_x = 0
        self.aceleracao_y = 0
        
        
    def desenha_corpo(self, tela):
        pygame.draw.circle(tela, self.cor, (self.pos_x, self.pos_y), self.radios)
       
        self.velocidade_x += self.aceleracao_x
        self.velocidade_y += self.aceleracao_y
        self.pos_x += self.velocidade_x
        self.pos_y += self.velocidade_y
        
    def defini_aceleracao(self, acel_x, acel_y):
        self.aceleracao_x = acel_x
        self.aceleracao_y = acel_y
        
    def rastro(self, tela):
        pygame.draw.circle(tela, (0, 255, 0), (self.pos_x, self.pos_y), self.radios / 2)
        
    def pint_corpo(self, tela):
        self.desenha_corpo(tela)