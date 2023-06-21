import pygame
import funciones
from colores import *
from sonidos import *
from imagenes import *
from constantes import *

pygame.mixer.init()


class Player:
    def __init__(self) -> None:
        # imagen normal
        self.image = funciones.insertar_imagen(PLAYER, 45, 50)
        self.rect = funciones.insertar_rect(self.image, 375, 770)
        self.image_bala = funciones.insertar_imagen(DISPARO_JUGADOR, 5, 15)
        self.bala = funciones.insertar_rect(self.image_bala, 375, 740) 
       #sprite explosion
        self.image_explosion = funciones.insertar_imagen(EXPLOSION_JUGADOR, 300, 90)
        self.image_explosion.set_colorkey(BLACK)        
        self.explosion = conseguir_animacion(self.image_explosion, 4, 1)
        self.frame = 0
        #vida y puntos
        self.lives = 3
        self.scores = 0
        # muerte
        self.muerte = False
        self.mostrar = True
        self.posicion_explosion = 375
        #sonidos
        self.sonido_explosion = pygame.mixer.Sound(JUGADOR_EXPLOSION)
        self.sonido_explosion.set_volume(0.8)
        self.flag_explosion_sonido = True
        self.sonido_disparo = pygame.mixer.Sound(JUGADOR_DISPARO)
        self.flag_disparo_sonido = True
        # Otros
        self.disparo = False
        self.segundos = 60 
        self.enemigos_derrotados = 0

        self.animation = self.explosion
        
        self.contador = 0
    def update(self):
        if self.muerte:
            if self.contador % 7 == 0:
                if self.frame < len(self.animation) -1:
                    self.frame += 1
            self.contador += 1

    def explotar(self):
        if self.muerte:
            if self.frame == 0 and self.flag_explosion_sonido:
                self.sonido_explosion.play()
                self.flag_explosion_sonido = False
            self.image = self.animation[self.frame]
            self.rect = funciones.insertar_rect(self.image, self.posicion_explosion + 20, 770)
            if self.frame == 3:
                pygame.time.delay(70)
                self.mostrar = False
                self.muerte = False
                self.rect.x = -100
                self.lives -= 1
                self.frame = 0
                self.flag_explosion_sonido = True
                
    def movimiento(self, x):
        if self.mostrar and not self.muerte:
            self.rect.x += x
            if not self.muerte:
                self.posicion_explosion = self.rect.x
            if not self.disparo:
                self.bala.x += x 

    def limites(self, minimo, maximo):
        if self.mostrar:
            if self.rect.x > maximo:
                self.rect.x = maximo
                if not self.disparo:
                    self.bala.x = maximo + 20
            if self.rect.x < minimo:
                self.rect.x = minimo
                if not self.disparo:
                    self.bala.x = minimo + 20

    def reaparecer(self):
        self.mostrar = True
        self.image = funciones.insertar_imagen(PLAYER, 45, 50)
        self.rect = funciones.insertar_rect(self.image, 375, 770)
        self.image_bala = funciones.insertar_imagen(DISPARO_JUGADOR, 5, 15)
        self.bala = funciones.insertar_rect(self.image_bala, 375, 740)
        self.posicion_explosion = self.rect.x 
    
    def disparar(self):
        if self.disparo and self.mostrar:
            if self.flag_disparo_sonido:
                self.sonido_disparo.play()
                self.flag_disparo_sonido = False
            self.bala.y -= VELOCIDAD_BALA

    def reaparicion_bala(self, choques):
        if self.bala.y < 30 or choques: 
            self.bala.x = self.rect.x + 20
            self.bala.y = self.rect.y - 13
            self.disparo = False
            choques = False
            self.flag_disparo_sonido = True
            return choques






def conseguir_animacion(surface_imagen, columnas, filas):
    lista = []
    fotograma_ancho = int(surface_imagen.get_width() / columnas)
    fotograma_alto = int(surface_imagen.get_height() / filas)
    for columna in range(columnas):
        for fila in range(filas):
            x = columna * fotograma_ancho
            y = fila * fotograma_alto
            surface_fotograma = surface_imagen.subsurface(x, y, fotograma_ancho, fotograma_alto)
            lista.append(surface_fotograma)
    return lista