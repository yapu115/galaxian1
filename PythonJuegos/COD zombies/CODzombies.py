import pygame
import zombies
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
nombre = pygame.display.set_caption("Kino der toten")

# Fondo
fondo = pygame.image.load("zombiesKino1.webp")
fondo = pygame.transform.scale(fondo, (1200, 600))
posicion_fondo = [0, 0]

# Richtofen
richtofen = pygame.image.load("Richtofen01.png")
richtofen = pygame.transform.scale(richtofen, (200, 400))
rect_richtofen = richtofen.get_rect()
rect_richtofen.centerx = 600
rect_richtofen.centery = 400

richtofen_vida = 50

#Zombies
lista_zombies = []
for i in range(5):
    lista_zombies.append(zombies.crear_zombies(100 +(i*80), 400, 200, 400))

#balas
bala = pygame.image.load("bala01.webp")
bala = pygame.transform.scale(bala, (20, 15))
rect_bala = bala.get_rect()
rect_bala.centerx = 100
rect_bala.centery = 100
#richtofen_walking = pygame.image.load("Richtofen02.webp").convert()
#richtofen_walking = pygame.transform.scale(richtofen_walking, (200, 400))
#posicion_richtofen_walking = [600, 200]
#richtofen_walking.set_colorkey(WHITE)


derecha = False
izquierda = True

#zombie_derecha = False
#zombie_izquierda = True

perdiendo_vida = False

disparo = False
flag = True
running = True

while running:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        #salir
        if evento.type == pygame.QUIT:
            running = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_f:
                if flag:
                    contadorbala1 = rect_richtofen.x
                    contadorbala2 = rect_richtofen.y
                    flag = False
                if izquierda:
                    contadorbala1 += 100
                if derecha:
                    contadorbala1 -= 100
                rect_bala[0] = contadorbala1
                rect_bala[1] = contadorbala2
                disparo = True


    

    #if not perdiendo_vida: 
    for zombie in lista_zombies:
        
        if rect_richtofen.colliderect(zombie["rect"]):
            richtofen_vida -= 10
            perdiendo_vida = True
        else:
            perdiendo_vida = False
        
        if rect_bala.colliderect(zombie["rect"]):
            zombie["rect"].x = 10000
        
        zombie_derecha = False
        zombie_izquierda = True

        if zombie["rect"][0] > rect_richtofen.x:
            zombie["rect"][0] -= 0.5
            if zombie_izquierda:
                zombie_izquierda = False
                zombie_derecha = True
                zombie["surface"] = pygame.transform.flip(zombie["surface"], True, False)
        else:
            zombie["rect"].x += 0.5
            if zombie_derecha:
                zombie_derecha = False
                zombie_izquierda = True
                zombie["surface"] = pygame.transform.flip(zombie["surface"], True, False)

        
    
    
    # Presionar teclas
    lista_teclas = pygame.key.get_pressed()
    if True in lista_teclas:
        #Movimiento

        if lista_teclas[pygame.K_RIGHT]:
            if derecha:
                derecha = False
                izquierda = True
                richtofen = pygame.transform.flip(richtofen, True, False)
            rect_richtofen.x += 3

        if lista_teclas[pygame.K_LEFT]:
            if izquierda:
                izquierda = False
                derecha = True
                richtofen = pygame.transform.flip(richtofen, True, False)
            rect_richtofen[0] -= 3        

        if rect_richtofen.x > 1000:
            rect_richtofen.x = 1000

        if rect_richtofen.x < -10:
            rect_richtofen.x = -10
        
        # Disparo



    
            


    
    print(richtofen_vida)

    screen.blit(fondo, posicion_fondo )
    screen.blit(richtofen, rect_richtofen)
    zombies.actualizar_pantalla(lista_zombies, screen)
    
    if disparo:
        screen.blit(bala, rect_bala)

    pygame.display.flip()



pygame.quit()


"""


    IF RICHTOFENDISPARA:
        IF IZQUIERDA: 
            CONTADORBALA -= 1

        POSICIONBALA[0] = CONTADORBALA
        
                        
IF FLAGZOMBIE
    screen.blit(imagen_reverse,posicion_rect_reverse)

IF RICHTOFENDISPARA
    screen.blit(imagen_reverse,posicion_rect_reverse)
    
"""