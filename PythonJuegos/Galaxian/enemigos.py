import pygame
import funciones
from colores import *
from imagenes import *
from sonidos import *

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.init()

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


class Enemigo:
    def __init__(self) -> None:
        #sprites
        self.stay_sheet = funciones.insertar_imagen(ENEMIGO1_QUIETO, 120, 27)
        self.stay_sheet.set_colorkey(BLACK)
        self.stay = conseguir_animacion(self.stay_sheet, 3, 1)
        self.image_explosion = funciones.insertar_imagen(EXPLOSION_ENEMIGO, 140, 30)
        self.image_explosion.set_colorkey(BLACK)
        self.explosion = conseguir_animacion(self.image_explosion, 4, 1)
        self.frame = 0
        #bala
        self.image_bala = funciones.insertar_imagen(DISPARO_ENEMIGO, 4, 10)
        self.image_bala.set_colorkey(BLACK)
        #sonidos
        self.sonido_explosion = pygame.mixer.Sound(ENEMIGO_EXPLOSION)
        self.sonido_explosion.set_volume(0.3)
        self.flag_explosion = False
        self.sonido_disparo = pygame.mixer.Sound(ENEMIGO_DISPARO)
        self.sonido_disparo.set_volume(0.1)
        self.flag_disparo = False
        # mostrar normalmente y movimiento
        self.mostrar = True
        self.y = 0
        self.x = 300
        self.derecha = True
        self.izquierda = False
        self.movimiento = 0
        #ataque
        self.disparo = False
        self.contacto = False
        #muerte y reaparicion
        self.muerte = False
        self.flag_reaparecer = False
        self.frame_cero = False
        #score
        self.score = 10

        #animacion
        self.animation = self.stay
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.bala = self.image_bala.get_rect()



        self.contador = 0
    def update(self):
        if self.contador % 20 == 0:
            if self.frame < len(self.animation) -1:
                self.frame += 1
            else:
                self.frame = 0
        self.contador += 1

    def draw(self, screen, x, y):
        if self.mostrar:
            self.image = self.animation[self.frame]
            self.rect = funciones.insertar_rect(self.image, x + self.movimiento, y)
            screen.blit(self.image, self.rect)
            if not self.disparo:
                self.x = x + self.movimiento
    
    def explotar(self):
        if self.muerte:
            if not self.flag_explosion:
                self.sonido_explosion.play()
                self.flag_explosion = True
            self.animation = self.explosion
            self.image = self.animation[self.frame]
            self.rect = funciones.insertar_rect(self.image, self.x, self.y)
            if self.frame == 3:
                self.mostrar = False
                self.muerte = False
                self.animation = self.stay
                self.frame = 0
                self.flag_explosion = False


    def moverse(self):
        if self.derecha:
            self.movimiento += 1
            if self.movimiento == 125:
                self.derecha = False
                self.izquierda = True
        elif self.izquierda:
            self.movimiento -= 1
            if self.movimiento == -125:
                self.izquierda = False
                self.derecha = True


    def atacar(self, screen, y):
        if self.disparo:
            if not self.flag_disparo:
                self.sonido_disparo.play()
                self.flag_disparo = True
            self.bala = funciones.insertar_rect(self.image_bala, self.x, y)
            self.bala.y += self.y
            screen.blit(self.image_bala, self.bala)
            self.y += 2
            if self.bala.y > 850 or self.contacto:
                self.disparo = False
                self.y = 0
                self.bala.x = self.x
                self.bala.y = self.rect.y
                self.contacto = False
                self.flag_disparo = False


        


class Enemigo2:
    def __init__(self) -> None:
        # sprite sheets
        self.stay_sheet = funciones.insertar_imagen(ENEMIGO2_QUIETO, 120, 27)
        self.stay_sheet.set_colorkey(BLACK)
        self.stay = conseguir_animacion(self.stay_sheet, 3, 1)
        self.image_explosion = funciones.insertar_imagen(EXPLOSION_ENEMIGO, 140, 30)
        self.image_explosion.set_colorkey(BLACK)
        self.explosion = conseguir_animacion(self.image_explosion, 4, 1)
        self.frame = 0
        # bala
        self.image_bala = funciones.insertar_imagen(DISPARO_ENEMIGO, 4, 10)
        self.image_bala.set_colorkey(BLACK)
        self.bala = self.image_bala.get_rect()
        #sonidos
        self.sonido_explosion = pygame.mixer.Sound(ENEMIGO_EXPLOSION)
        self.sonido_explosion.set_volume(0.3)
        self.flag_explosion = False
        self.sonido_disparo = pygame.mixer.Sound(ENEMIGO_DISPARO)
        self.sonido_disparo.set_volume(0.1)
        self.flag_disparo = False
        # Posicion enemigo y movimiento
        self.mostrar = True
        self.y = 0
        self.x = 300
        self.izquierda = False
        self.derecha = True
        self.movimiento = 0
        # Ataque
        self.contacto = False
        self.disparo = False
        # Muerte y reaparicion
        self.muerte = False
        self.flag_reaparecer = False
        self.frame_cero = False
        # score
        self.score = 20

        self.animation = self.stay
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()

        self.contador = 0
    def update(self,):
            if self.contador % 20 == 0:
                if self.frame < len(self.animation) -1:
                    self.frame += 1
                else:
                    self.frame = 0
            self.contador += 1

    def draw(self, screen, x, y):
        if self.mostrar:
            self.image = self.animation[self.frame]
            self.rect = funciones.insertar_rect(self.image, x + self.movimiento, y)
            screen.blit(self.image, self.rect)
            if not self.disparo:
                self.x = x + self.movimiento

    def explotar(self):
        if self.muerte:
            if not self.flag_explosion:
                self.sonido_explosion.play()
                self.flag_explosion = True
            self.animation = self.explosion
            self.image = self.animation[self.frame]
            self.rect = funciones.insertar_rect(self.image, self.x, self.y)
            if self.frame == 3:
                self.mostrar = False
                self.muerte = False
                self.animation = self.stay
                self.frame = 0
                self.flag_explosion = False


    def moverse(self):
        if self.derecha:
            self.movimiento += 1
            if self.movimiento == 125:
                self.derecha = False
                self.izquierda = True
        elif self.izquierda:
            self.movimiento -= 1
            if self.movimiento == -125:
                self.izquierda = False
                self.derecha = True

    def atacar(self, screen, y):
        if self.disparo:
            if not self.flag_disparo:
                self.sonido_disparo.play()
                self.flag_disparo = True
            self.bala = funciones.insertar_rect(self.image_bala, self.x, y)
            self.bala.y += self.y
            screen.blit(self.image_bala, self.bala)
            self.y += 3
            if self.bala.y > 850 or self.contacto:
                self.disparo = False
                self.y = 0
                self.bala.x = self.x
                self.bala.y = self.rect.y
                self.contacto = False
                self.flag_disparo = False

                


class Enemigo3:
    def __init__(self) -> None:
        # Sprite sheets
        self.stay_sheet = funciones.insertar_imagen(ENEMIGO3_QUIETO, 120, 27)
        self.stay_sheet.set_colorkey(BLACK)
        self.stay = conseguir_animacion(self.stay_sheet, 3, 1)
        self.image_explosion = funciones.insertar_imagen(EXPLOSION_ENEMIGO, 140, 30)
        self.image_explosion.set_colorkey(BLACK)
        self.explosion = conseguir_animacion(self.image_explosion, 4, 1)
        self.frame = 0
        # Bala
        self.image_bala = funciones.insertar_imagen(DISPARO_ENEMIGO, 4, 10)
        self.image_bala.set_colorkey(BLACK)
        self.bala = self.image_bala.get_rect()
        #sonidos
        self.sonido_explosion = pygame.mixer.Sound(ENEMIGO_EXPLOSION)
        self.sonido_explosion.set_volume(0.3)
        self.flag_explosion = False
        self.sonido_disparo = pygame.mixer.Sound(ENEMIGO_DISPARO)
        self.sonido_disparo.set_volume(0.1)
        self.flag_disparo = False
        # Posicion enemigo y movimiento
        self.mostrar = True
        self.y = 0
        self.x = 300
        self.izquierda = False
        self.derecha = True
        self.movimiento = 0
        # Ataque
        self.contacto = False
        self.disparo = False
        # Muerte y reaparicion
        self.muerte = False
        self.flag_reaparecer = False
        self.frame_cero = False
        # Score
        self.score = 30

        # Animacion
        self.animation = self.stay
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()

    

        self.contador = 0
    def update(self,):
        if self.contador % 20 == 0:
            if self.frame < len(self.animation) -1:
                self.frame += 1
            else:
                self.frame = 0
        self.contador += 1

    def draw(self, screen, x, y):
        if self.mostrar:
            self.image = self.animation[self.frame]
            self.rect = funciones.insertar_rect(self.image, x + self.movimiento, y)
            screen.blit(self.image, self.rect)
            if not self.disparo:
                self.x = x + self.movimiento

    def explotar(self):
        if self.muerte:
            if not self.flag_explosion:
                self.sonido_explosion.play()
                self.flag_explosion = True
            self.animation = self.explosion
            self.image = self.animation[self.frame]
            self.rect = funciones.insertar_rect(self.image, self.x, self.y)
            if self.frame == 3:
                self.mostrar = False
                self.muerte = False
                self.animation = self.stay
                self.frame = 0
                self.flag_explosion = False

    
    def moverse(self):
        if self.derecha:
            self.movimiento += 1
            if self.movimiento == 125:
                self.derecha = False
                self.izquierda = True
        elif self.izquierda:
            self.movimiento -= 1
            if self.movimiento == -125:
                self.izquierda = False
                self.derecha = True

    def atacar(self, screen, y):
        if self.disparo:
            if not self.flag_disparo:
                self.sonido_disparo.play()
                self.flag_disparo = True
            self.bala = funciones.insertar_rect(self.image_bala, self.x, y)
            self.bala.y += self.y
            screen.blit(self.image_bala, self.bala)
            self.y += 3.5
            if self.bala.y > 850 or self.contacto:
                self.disparo = False
                self.y = 0
                self.bala.x = self.x
                self.bala.y = self.rect.y
                self.contacto = False
                self.flag_disparo = False
    




class Enemigo4:
    def __init__(self) -> None:
        # Sprite sheets
        self.stay_sheet = funciones.insertar_imagen(ENEMIGO04, 45, 37)
        self.stay_sheet.set_colorkey(BLACK)
        self.stay = conseguir_animacion(self.stay_sheet, 1, 1) 
        self.mostrar = True
        self.image_explosion = funciones.insertar_imagen(EXPLOSION_ENEMIGO, 180, 40)
        self.image_explosion.set_colorkey(BLACK)
        self.explosion = conseguir_animacion(self.image_explosion, 4, 1)
        self.frame = 0
        # bala
        self.image_bala = funciones.insertar_imagen(DISPARO_ENEMIGO, 6, 16)
        self.image_bala.set_colorkey(BLACK)
        self.bala = self.image_bala.get_rect()
        #sonidos
        self.sonido_explosion = pygame.mixer.Sound(ENEMIGO_EXPLOSION)
        self.sonido_explosion.set_volume(0.3)
        self.flag_explosion = False
        self.sonido_disparo = pygame.mixer.Sound(ENEMIGO_DISPARO)
        self.sonido_disparo.set_volume(0.1)
        self.flag_disparo = False
        # Posicion enemigo y movimiento
        self.mostrar = True
        self.y = 0
        self.x = 300
        self.izquierda = False
        self.derecha = True
        self.movimiento = 0
        # Ataque
        self.contacto = False
        self.disparo = False
        # Muerte
        self.muerte = False
        self.flag_reaparecer = False
        self.frame_cero = False
        self.score = 40

        # Animacion
        self.animation = self.stay
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        

        self.contador = 0
    def update(self,):
            if self.contador % 20 == 0:
                if self.frame < len(self.animation) -1:
                    self.frame += 1
                else:
                    self.frame = 0
            self.contador += 1

    def draw(self, screen, x, y):
        if self.mostrar:
            self.image = self.animation[self.frame]
            self.rect = funciones.insertar_rect(self.image, x + self.movimiento, y)
            screen.blit(self.image, self.rect)
            if not self.disparo:
                self.x = x + self.movimiento
        
    def explotar(self):
        if self.muerte:
            if not self.flag_explosion:
                self.sonido_explosion.play()
                self.flag_explosion = True
            self.animation = self.explosion
            self.image = self.animation[self.frame]
            self.rect = funciones.insertar_rect(self.image, self.x, self.y)
            if self.frame == 3:
                self.mostrar = False
                self.muerte = False
                self.animation = self.stay
                self.frame = 0
                self.flag_explosion = False


    def moverse(self):
        if self.derecha:
            self.movimiento += 1
            if self.movimiento == 125:
                self.derecha = False
                self.izquierda = True
        elif self.izquierda:
            self.movimiento -= 1
            if self.movimiento == -125:
                self.izquierda = False
                self.derecha = True

    def atacar(self, screen, y):
        if self.disparo: 
            if not self.flag_disparo:
                self.sonido_disparo.play()
                self.flag_disparo = True
            self.bala = funciones.insertar_rect(self.image_bala, self.x, y)
            self.bala.y += self.y
            screen.blit(self.image_bala, self.bala)
            self.y += 4 
            if self.bala.y > 850 or self.contacto:
                self.disparo = False
                self.y = 0
                self.bala.x = self.x
                self.bala.y = self.rect.y
                self.contacto = False
                self.flag_disparo = False



