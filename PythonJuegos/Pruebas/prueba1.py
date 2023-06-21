import pygame
from colores import *

fondo_juego = (105, 105, 105)
pos_circulo = [100, 100]

pygame.init() # Se inicializa pygame

pantalla = pygame.display.set_mode((500,500)) #Horizontal, vertical/ ancho, alto
pygame.display.set_caption("Juego Hello there") # Nombre del juego que se mostrara arriba de la pantalla

timer_segundos = pygame.USEREVENT # este es un evento que cree yo
pygame.time.set_timer(timer_segundos, 1) # 1000 es 1 segundo

#imagen
imagen_spiderman = pygame.image.load("spiderman.webp")
imagen_spiderman = pygame.transform.scale(imagen_spiderman,(80,80))
poscion_spiderman = [30, 100]
#texto
fuente = pygame.font.SysFont("Arial", 30)
texto = fuente.render("Hello there", True, BLACK)


flag_running = True

while flag_running: # Mientras que el juego continue:
    lista_eventos = pygame.event.get() #Los eventos se van a guardar en esta lista 
    for evento in lista_eventos: #Por cada evento que suceda:
        if evento.type == pygame.QUIT: #Si se presion el boton de salida (quit)
            flag_running = False # El juego acaba
        if evento.type == pygame.KEYDOWN: # Si se presiona algun boton
            if evento.key == pygame.K_RIGHT: #Si se presiona la flecha derecha
                pos_circulo[0] = pos_circulo[0] + 10
            if evento.key == pygame.K_LEFT: # si se presiona la flecha izquiera:
                pos_circulo[0] = pos_circulo[0] - 10

    lista_teclas = pygame.key.get_pressed()
    if True in lista_teclas: # Pregunta si hay alguna tecla presionada
        if lista_teclas[pygame.K_RIGHT]:
            pos_circulo[0] = pos_circulo[0] + 0.5
        if lista_teclas[pygame.K_LEFT]:
            pos_circulo[0] = pos_circulo[0] - 0.5
    if evento.type == pygame.MOUSEBUTTONDOWN:
        poscion_spiderman = evento.pos

    pantalla.fill(fondo_juego) # Se pinta el fondo de la ventana
    pantalla.blit(imagen_spiderman, (poscion_spiderman)) # Fundir la imagen en la ventana
    pantalla.blit(texto,(300, 300)) #Fundir el texto en la ventana
    # pygame.draw.rect(pantalla, WHITESMOKE, (100, 5, 100, 200))
    pygame.draw.circle(pantalla, YELLOW4, pos_circulo, 50) #Dibuja un circulo en pantalla
    pygame.display.flip() #Muestra los cambios en la pantalla

pygame.quit() # Fin

