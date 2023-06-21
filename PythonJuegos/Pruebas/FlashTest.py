import pygame
from colores import *
# EN CADA CLASE USAR UN ARCHIVO DIFERENTE

pygame.init()
pygame.display.set_caption("Flash running") # Nombre del juego que se mostrara arriba de la pantalla

fondo_juego = SKYBLUE

ANCHO = 1000
LARGO = 1000
screen = pygame.display.set_mode((ANCHO, LARGO))
#posicion_circulo = [100,100]
#posicion_pasto = (0, 700, 1000, 400)

#Flash parado
imagen_flash = pygame.image.load("flash01.png")
imagen_flash = pygame.transform.scale(imagen_flash, (200, 300))
posicion_flash = [450, 500]
rect_flash = imagen_flash.get_rect()
rect_flash.centerx = 200
rect_flash.centery = 100

#flash corriendo
imagen_flash_corriendo = pygame.image.load("flash02.webp")
imagen_flash_corriendo = pygame.transform.scale(imagen_flash_corriendo, (300, 225))
posicion_rect_flash_corriendo = [450, 500]
rect_flash_corriendo = imagen_flash_corriendo.get_rect()
rect_flash_corriendo.centerx = 200
rect_flash_corriendo.centery = 100


#Reverse flash
imagen_reverse = pygame.image.load("reverse.png")
imagen_reverse = pygame.transform.scale(imagen_reverse, (125, 275))
posicion_rect_reverse = [100, 500]
rect_reverse = imagen_reverse.get_rect()
rect_reverse.centerx = 200
rect_reverse.centery = 100


#fondo
background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, (1000, 1000))
posicion_background = [0,0]

izquierda = True
derecha = False

# timer
timer_segundos = pygame.USEREVENT
pygame.time.set_timer(timer_segundos, 1000)

#musica
pygame.mixer.init()
pygame.mixer.music.set_volume(0.7)
sonido_fondo = pygame.mixer.Sound("flashTheme.mp3")

aux = imagen_flash
aux2 = rect_flash

running = True

while running:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            running = False


    lista_teclas = pygame.key.get_pressed()
    if True in lista_teclas:
        if lista_teclas[pygame.K_RIGHT]:
            if derecha:
                imagen_flash_corriendo = pygame.transform.flip(imagen_flash_corriendo, True, False)
                derecha = False
                izquierda = True
            posicion_rect_flash_corriendo[0] += 5
        if lista_teclas[pygame.K_LEFT]:
            if izquierda:
                imagen_flash_corriendo = pygame.transform.flip(imagen_flash_corriendo, True, False)
                derecha = True
                izquierda = False
            posicion_rect_flash_corriendo[0] -= 5
        if lista_teclas[pygame.K_UP]:
            posicion_rect_flash_corriendo[1] -= 5
        if lista_teclas[pygame.K_DOWN]:
            posicion_rect_flash_corriendo[1] += 5
    
        if posicion_rect_flash_corriendo[0] > ANCHO + 80:
            posicion_rect_flash_corriendo[0] = -80
        if posicion_rect_flash_corriendo[0] < -100:
            posicion_rect_flash_corriendo[0] = 1000
        
        if posicion_rect_flash_corriendo[1] > LARGO + 80:
            posicion_rect_flash_corriendo[1] = -80
        if posicion_rect_flash_corriendo[1] < -100:
            posicion_rect_flash_corriendo[1] = 1000

        aux2 = rect_flash
        imagen_flash = imagen_flash_corriendo
        rect_flash = posicion_rect_flash_corriendo

        sonido_fondo.set_volume(0.2)
        sonido_fondo.play()
    

    else:
        imagen_flash = aux
        posicion_rect_flash = aux2
    
    if rect_flash.colliderect(rect_reverse):
        print("My golds are beyond your understandment")
            
    screen.fill(fondo_juego)

    screen.blit(background, posicion_background)
    screen.blit(imagen_flash, rect_flash)
    screen.blit(imagen_reverse,posicion_rect_reverse)
    #screen.blit(imagen_flash_corriendo, (posicion_flash_corriendo))

    #pygame.draw.circle(screen, YELLOW1, posicion_circulo, 200)
    #pygame.draw.rect(screen, GREEN, posicion_pasto)
    pygame.display.flip()

pygame.quit()