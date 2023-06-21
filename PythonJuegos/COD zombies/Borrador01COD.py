import pygame
from colores import *



"""
TO DO LIST:
- Cuando hago click que se muestren las coordenadas
- Que se pueda subir las escaleras
- Dos imagenes mas: Una para cuando  camina, otra para cuando dispara
- Zombies
"""




pygame.init()

# Pantalla
screen = pygame.display.set_mode((1200, 600))
fondo = pygame.display.set_caption("Kino der toten")

# Fondo
fondo = pygame.image.load("zombiesKino1.webp")
fondo = pygame.transform.scale(fondo, (1200, 600))
posicion_fondo = [0, 0]

# Richtofen
richtofen = pygame.image.load("Richtofen01.png")
richtofen = pygame.transform.scale(richtofen, (200, 400))
posicion_richtofen = [600, 200]

richtofen_walking = pygame.image.load("Richtofen02.webp").convert()
richtofen_walking = pygame.transform.scale(richtofen_walking, (200, 400))
posicion_richtofen_walking = [600, 200]
richtofen_walking.set_colorkey(WHITE)


derecha = False
izquierda = True

aux1 = richtofen
aux2 = posicion_richtofen

running = True

while running:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        #salir
        if evento.type == pygame.QUIT:
            running = False

    # Movimiento
    lista_teclas = pygame.key.get_pressed()
    if True in lista_teclas:
        if lista_teclas[pygame.K_RIGHT]:
            if derecha:
                derecha = False
                izquierda = True
                richtofen_walking = pygame.transform.flip(richtofen_walking, True, False)
            posicion_richtofen[0] += 0.5
        if lista_teclas[pygame.K_LEFT]:
            if izquierda:
                izquierda = False
                derecha = True
                richtofen_walking = pygame.transform.flip(richtofen_walking, True, False)
                           
            posicion_richtofen[0] -= 0.5        

        aux2 = posicion_richtofen
        richtofen = richtofen_walking
        posicion_richtofen = posicion_richtofen_walking

    else:
        richtofen = aux1
        posicion_richtofen = aux2

    screen.blit(fondo, posicion_fondo )
    screen.blit(richtofen, posicion_richtofen)

    pygame.display.flip()



pygame.quit()


"""
RICHTOFENVIDA = 30


IF CONTADOR == 5: 
    FLAGZOMBIE = TRUE
    IF FLAGZOMBIE:
        IF POSICION ZOMBIE == POSICION RICHTOFEN
            RICHTOFENVIDA -= 5
        ELSE:
            POSICION ZOMBIE[0] += 0.5

    IF RICHTOFENDISPARA:
        IF IZQUIERDA: 
            CONTADORBALA -= 1

        POSICIONBALA[0] = CONTADORBALA
        
                        
IF FLAGZOMBIE
    screen.blit(imagen_reverse,posicion_rect_reverse)

IF RICHTOFENDISPARA
    screen.blit(imagen_reverse,posicion_rect_reverse)
    
"""