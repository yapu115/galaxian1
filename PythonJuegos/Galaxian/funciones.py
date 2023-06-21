import random
import pygame
from colores import * 
from sonidos import *
from enemigos import Enemigo, Enemigo2, Enemigo3, Enemigo4
from constantes import *



def insertar_imagen(direccion,x, y):
    imagen = pygame.image.load(direccion)
    imagen = pygame.transform.scale(imagen, (x, y))
    return imagen

def insertar_rect(imagen, x, y):
    rect = imagen.get_rect()
    rect.centerx = x
    rect.centery = y
    return rect


def crear_fila_enemigos_uno(): 
    fila_enemigos = []
    for i in range(10):
        enemigo = Enemigo()
        fila_enemigos.append(enemigo)
    return fila_enemigos

def crear_fila_enemigos_dos(): 
    fila_enemigos = []
    for i in range(8):
        enemigo = Enemigo2()
        fila_enemigos.append(enemigo)
    return fila_enemigos

def crear_fila_enemigos_tres(): 
    fila_enemigos = []
    for i in range(6):
        enemigo = Enemigo3()
        fila_enemigos.append(enemigo)
    return fila_enemigos

def crear_fila_enemigos_cuatro(): 
    fila_enemigos = []
    for i in range(2):
        enemigo = Enemigo4()
        fila_enemigos.append(enemigo)
    return fila_enemigos

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.init()



def colision_enemigos(fila, jugador, impacto):
    for enemigo in fila:
        if enemigo.mostrar and jugador.bala.colliderect(enemigo.rect):
            jugador.scores += enemigo.score
            jugador.segundos += 0.5
            enemigo.muerte = True
            enemigo.frame = 0
            impacto = True
            jugador.enemigos_derrotados += 1
        if enemigo.bala.colliderect(jugador.rect):
            jugador.muerte = True
            enemigo.contacto = True
            enemigo.golpeo = True
    return impacto


def dibujar_filas_enemigos(fila, x, y, screen, jugador, m=50):
    distancia = 0
    numero = random.randint(0, NUMERO_RANDOM_DIFICULTAD)
    for posicion,enemigo in enumerate(fila):
        if jugador.mostrar:
            if posicion == numero and enemigo.mostrar:
                enemigo.disparo = True
        enemigo.draw(screen,x + (m*distancia), y)
        enemigo.moverse()
        enemigo.atacar(screen, y)
        enemigo.explotar()
        enemigo.update()
        distancia += 1

        if jugador.enemigos_derrotados % 46 == 0 and jugador.enemigos_derrotados != 0:
            enemigo.mostrar = True
            

sonido_boton = pygame.mixer.Sound(BOTON_PRESIONADO)
def click_boton(lista_click, rect_boton):
    retorno = False
    if lista_click[0] > rect_boton[0] and lista_click[0] < rect_boton[0] + rect_boton[2]:
        if lista_click[1] > rect_boton[1] and lista_click[1] < rect_boton[1] + rect_boton[3]:
            sonido_boton.play()
            retorno = True
    return retorno

def crear_ranking(lista_ranking, screen):
    font = pygame.font.SysFont("calibri", TAMAÑO_LETRA)
    rank = font.render("Rank:", True, GREEN4)
    name = font.render("Name:", True, GREEN4)
    score = font.render("Score:", True, GREEN4)
    for i, columna in enumerate(lista_ranking):
        if i < 10:
            columna = list(columna)        
            fila_rank = font.render(f"{i+1}:", True, RED3)
            fila_name = font.render(f"{columna[1]}", True, RED3)
            fila_score = font.render(f"{columna[2]}", True, RED3)
            screen.blit(fila_rank, (FILA_RANK_X, FILA_Y + (i * 60)))
            screen.blit(fila_name, (FILA_NAME_X, FILA_Y + (i * 60))) 
            screen.blit(fila_score, (FILA_SCORE_X, FILA_Y + (i * 60)))
    screen.blit(rank, (POS_RANK_X, POS_Y))
    screen.blit(name, (POS_NAME_X, POS_Y))
    screen.blit(score, (POS_SCORE_X, POS_Y))