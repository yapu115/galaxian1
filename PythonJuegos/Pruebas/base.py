#pip install pygame
"""
import pygame

pygame.init()

pantalla = pygame.display.set_mode((500, 500))
pygame.display.set_caption("juego")
flag_correr = True
while flag_correr:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_correr = False
    pantalla.fill((0,0,128))
    pygame.draw.circle(pantalla,(255, 255, 0), (100, 100), 50)
    pygame.display.flip()
pygame.quit()
"""

import pygame
from colores import *

fondo_game = (104, 125, 151)
pos_circulo = [100, 100]

pygame.init()
timer_segundos = pygame.USEREVENT # este es un evento que cree yo

pygame.time.set_timer(timer_segundos, 1) # 1000 es 1 segundo


pantalla = pygame.display.set_mode((500,500))

pygame.display.set_caption("Game")

flag_game = True

while flag_game:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_game = False
        if evento.type == pygame.USEREVENT:
            if evento.type == timer_segundos:   
                if pos_circulo[0] < 580:
                    pos_circulo[0] = pos_circulo[0] + 10
                else:
                    pos_circulo[0] = 0

    pantalla.fill(fondo_game)
    # pygame.draw.rect(pantalla, WHITESMOKE, (100, 5, 100, 200))
    pygame.draw.circle(pantalla, YELLOW4, pos_circulo, 50)
    pygame.display.flip()

pygame.quit()
