import pygame
import colores

ANCHO_VENTANA = 500
ALTO_VENTANA = 500
score = 0

pygame.init()
pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Mi primer juego")

#imagen rana
imagen_rana = pygame.image.load("jugador.jpg")
imagen_rana = pygame.transform.scale(imagen_rana,(100,100))
rect_rana = pygame.Rect(30,100,101,101)

#creo la lista de moscas
lista_moscas = elementos.crear_lista_moscas(10)


flag_correr = True
while flag_correr:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_correr = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            lista_posicion = list(evento.pos)

            rect_rana[0] = lista_posicion[0] #modifico el left del rect
            rect_rana[1] = lista_posicion[1] #modifico el top del rect
        
    pantalla.fill(colores.COLOR_CELESTE)

    #dibujar la moscas
    score = elementos.actualizar_pantalla(lista_moscas, pantalla, rect_rana, score)
 
    font = pygame.font.SysFont("Arial", 50)
    texto = font.render("SCORE: {0}".format(score), True, colores.BLACK)
    pantalla.blit(texto,(10,10))

    #DIBUJAR la rana
    pygame.draw.rect(pantalla, colores.RED1, rect_rana)
    pantalla.blit(imagen_rana,rect_rana)

    pygame.display.flip()

pygame.quit()



import pygame
import colores
from personaje import Personaje

ANCHO_VENTANA = 600
ALTO_VANTANA = 600

pygame.init()
pantalla = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VANTANA))
pygame.display.set_caption("Mi primer bosque")
reloj = pygame.time.Clock()

imagen_bosque = pygame.image.load("bosque.jpg")
imagen_bosque = pygame.transform.scale(imagen_bosque,(ANCHO_VENTANA, ALTO_VANTANA))

#Creacion de mi personaje (constructor)
personaje1 = Personaje()

flag_correr = True
while flag_correr:
    lista_evento = pygame.event.get()
    for evento in lista_evento:
        if evento.type == pygame.QUIT:
            flag_correr = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            personaje1.rect.x = personaje1.rect.x + 20
            personaje1.actualizar()
        if keys[pygame.K_LEFT]:
            personaje1.rect.x = personaje1.rect.x - 20
            personaje1.actualizar()
        if keys[pygame.K_DOWN]:
            personaje1.rect.y = personaje1.rect.y + 20
            personaje1.actualizar()
        if keys[pygame.K_UP]:
            personaje1.rect.y = personaje1.rect.y - 20
            personaje1.actualizar()

    milis = reloj.tick(60) #cada 8 miliss da una vuelta al while
    pantalla.blit(imagen_bosque,imagen_bosque.get_rect())
    #dibujar mi personaje
    personaje1.dibujar(pantalla)

    pygame.display.flip()

pygame.quit


