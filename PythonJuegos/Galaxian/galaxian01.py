import pygame
import sqlite3
import math
from colores import *
from constantes import *
import funciones
from SQLite_funciones import *
from imagenes import *
from sonidos import *
from Jugador import Player
from enemigos import *

pygame.init()


# Pantalla
screen = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
nombre = pygame.display.set_caption("Galaxian")

#Fondo
fondo = funciones.insertar_imagen(BACKGROUND, ANCHO_FONDO, ALTO_FONDO)
rect_fondo = fondo.get_rect()

cantidad_fondos = math.ceil(ALTO_PANTALLA / rect_fondo.height) + 1

# Imagenes
logo_galaxian = funciones.insertar_imagen(LOGO, LOGO_ANCHO, LOGO_ALTO)
rect_logo = funciones.insertar_rect(logo_galaxian, LOGO_X, LOGO_Y)

imagen_game_over = funciones.insertar_imagen(GAME_OVER_IMAGEN, GAME_OVER_ANCHO, GAME_OVER_ALTO)
rect_game_over = funciones.insertar_rect(imagen_game_over, GAME_OVER_x, GAME_OVER_y)
imagen_game_over.set_colorkey(BLACK)

# Botones
imagen_start = funciones.insertar_imagen(BOTON_START, START_ANCHO, START_ALTO)
rect_start = funciones.insertar_rect(imagen_start, START_X, START_Y)

imagen_scores = funciones.insertar_imagen(BOTON_SCORES, SCORES_ANCHO, SCORES_ALTO)
rect_scores = funciones.insertar_rect(imagen_scores, SCORES_X, SCORES_Y)

imagen_volver = funciones.insertar_imagen(VOLVER, VOLVER_ANCHO, VOLVER_ALTO)
rect_volver = funciones.insertar_rect(imagen_volver, VOLVER_X, VOLVER_Y)

# Jugador
jugador = Player()

# Enemigos
# 1
fila_uno_enemigos = funciones.crear_fila_enemigos_uno()
fila_dos_enemigos = funciones.crear_fila_enemigos_uno()
fila_tres_enemigos = funciones.crear_fila_enemigos_uno()
# 2
fila_cuatro_enemigos = funciones.crear_fila_enemigos_dos()
# 3
fila_cinco_enemigos = funciones.crear_fila_enemigos_tres()
# 4
fila_seis_enemigos = funciones.crear_fila_enemigos_cuatro()

# Ingreso del nombre
font_input = pygame.font.SysFont("Arial", TAMAÑO_LETRA)
ingreso = ""
ingreso_rect = pygame.Rect(INGRESO_LEFT, INGRESO_TOP, INGRESO_ANCHO, INGRESO_ALTO)

# Musica
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.init()
pygame.mixer.music.set_volume(0.8)

sonido_game_over = pygame.mixer.Sound(GAME_OVER)
sonido_boton = pygame.mixer.Sound(BOTON_PRESIONADO)

# Letra
font = pygame.font.SysFont("calibri", TAMAÑO_LETRA)

#clock
clock = pygame.time.Clock()

running = True
while running:
    lista_eventos = pygame.event.get()

    #pantalla inicio
    if PANTALLA == 0:
        if flag_squlite:
            crear_DB()
            crear_tabla()
            flag_squlite = False
            pygame.mixer.music.load(MUSICA_INICIO)
            pygame.mixer.music.play(-1)
        
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                running = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                lista_click = list(evento.pos)

                if funciones.click_boton(lista_click, rect_start):
                    pygame.mixer.music.load(MUSICA_FONDO)
                    pygame.mixer.music.set_volume(5.9)
                    pygame.mixer.music.play(-1)
                    PANTALLA = 1

                if funciones.click_boton(lista_click, rect_scores):
                    PANTALLA = 2 

        screen.blit(fondo, rect_fondo)
        screen.blit(logo_galaxian, rect_logo)
        screen.blit(imagen_start, rect_start)
        screen.blit(imagen_scores, rect_scores)

        pygame.display.flip()

    elif PANTALLA == 2:
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                running = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                lista_click = list(evento.pos)
            
        screen.blit(fondo, rect_fondo)
        lista_ranking = listar_filas()
        funciones.crear_ranking(lista_ranking, screen)            

        if funciones.click_boton(lista_click, rect_volver):
            PANTALLA = 0

        screen.blit(imagen_volver, rect_volver)
        pygame.display.flip()


    elif PANTALLA == 1:
        for evento in lista_eventos:
            #Salir
            if evento.type == pygame.QUIT:
                running = False
            
            #Disparar la bala
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP or evento.key == pygame.K_SPACE:
                    jugador.disparo = True
            
        # Movimiento
        lista_teclas = pygame.key.get_pressed()
        if True in lista_teclas:

            #Movimiento del jugador
            if lista_teclas[pygame.K_RIGHT]:
                jugador.movimiento(MOVIMIENTO_DER_JUGADOR)

            if lista_teclas[pygame.K_LEFT]:
                jugador.movimiento(MOVIMIENTO_IZQ_JUGADOR)

            #limites
            jugador.limites(LIMITE_JUGADOR_IZQ, LIMITE_JUGADOR_DER)
        
        # Jugador elimina enemigo
        CHOQUE = funciones.colision_enemigos(fila_uno_enemigos, jugador, CHOQUE)
        CHOQUE = funciones.colision_enemigos(fila_dos_enemigos, jugador, CHOQUE)
        CHOQUE = funciones.colision_enemigos(fila_tres_enemigos, jugador, CHOQUE)
        CHOQUE = funciones.colision_enemigos(fila_cuatro_enemigos, jugador, CHOQUE)
        CHOQUE = funciones.colision_enemigos(fila_cinco_enemigos, jugador, CHOQUE)
        CHOQUE = funciones.colision_enemigos(fila_seis_enemigos, jugador, CHOQUE)
        
        #fondo
        for i in range(0, cantidad_fondos):
            screen.blit(fondo, (0, i * rect_fondo.height + movimiento_fondo))        
        movimiento_fondo -= 1.5
        # Reset 
        if abs(movimiento_fondo) > rect_fondo.height:
            movimiento_fondo = 0


        #jugador
        if jugador.mostrar:
            jugador.tiempo_inicio = pygame.time.get_ticks()
            screen.blit(jugador.image, jugador.rect)
            jugador.explotar()
            jugador.update()
            jugador.disparar()
            CHOQUE = jugador.reaparicion_bala(CHOQUE)
            if not jugador.muerte:
                screen.blit(jugador.image_bala, jugador.bala)
        else:
            jugador.tiempo_actual = pygame.time.get_ticks()
            if jugador.lives > 0:
                if jugador.tiempo_actual - jugador.tiempo_inicio >= 5000:
                    jugador.reaparecer()

        #SCORE
        texto = font.render("SCORE: {0}".format(jugador.scores), True, RED3)
        screen.blit(texto, (CONTADOR_SCORE_X,CONTADOR_SCORE_Y))

        # Vidas
        vidas = font.render("Vidas: {0}".format(jugador.lives), True, RED3)
        screen.blit(vidas, (CONTADOR_VIDAS_X,CONTADOR_VIDAS_Y))
        
        # Tiempo
        tiempo = font.render("TIEMPO: {0}".format(jugador.segundos), True, WHITE)
        screen.blit(tiempo, (TIEMPO_X, TIEMPO_Y))
        TIEMPO += 1
        if TIEMPO == FPS:
            TIEMPO = 0
            jugador.segundos -= 1


        # Dibujar enemigos en fila
        funciones.dibujar_filas_enemigos(fila_uno_enemigos, FILA_UNO_X, FILA_UNO_Y, screen, jugador)
        funciones.dibujar_filas_enemigos(fila_dos_enemigos, FILA_UNO_X, FILA_DOS_Y, screen, jugador)
        funciones.dibujar_filas_enemigos(fila_tres_enemigos, FILA_UNO_X, FILA_TRES_Y, screen, jugador)
        funciones.dibujar_filas_enemigos(fila_cuatro_enemigos,FILA_CUATRO_X, FILA_CUATRO_Y, screen, jugador)
        funciones.dibujar_filas_enemigos(fila_cinco_enemigos, FILA_CINCO_X, FILA_CINCO_Y, screen, jugador)
        funciones.dibujar_filas_enemigos(fila_seis_enemigos, FILA_SEIS_X, FILA_SEIS_Y, screen, jugador, 150)
        
        # Game Over
        if jugador.lives == 0 or jugador.segundos == -0:
            pygame.mixer.music.stop()
            sonido_game_over.play()
            PANTALLA = 3 # Pregunar el nombre y guardarlo

        # FPS
        print(clock.tick(FPS))

        pygame.display.flip()
    
    elif PANTALLA == 3:
        # Ingreso del nombre
        screen.blit(fondo, rect_fondo)
        screen.blit(imagen_game_over, rect_game_over)
        texto_ingreso = font.render("Ingrese su nombre (solo 3 letras): ", True, WHITESMOKE)
        texto_score = font.render(f"Final score: {jugador.scores}", True, RED4)
        screen.blit(texto_score, (TEXTO_SCORE_X,TEXTO_SCORE_Y))
        screen.blit(texto_ingreso, (INGRESO_X,INGRESO_Y))

        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                running = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_BACKSPACE:
                    ingreso = ingreso[0:-1]
                
                elif evento.key == pygame.K_RETURN:
                    if len(ingreso) == 3 and ingreso.isupper():
                        insertar_fila(ingreso, jugador.scores)    
                        PANTALLA = 4
                else:
                    ingreso += evento.unicode
            
        texto_final = font.render("GRACIAS POR JUGAR!", True, WHITESMOKE)            
        screen.blit(texto_final, (TEXTO_FINAL_X, TEXTO_FINAL_Y))

        pygame.draw.rect(screen, WHITE, ingreso_rect, 2)
        font_input_surface = font_input.render(ingreso, True, WHITE)
        screen.blit(font_input_surface, (ingreso_rect.x + 5, ingreso_rect.y +5))

        pygame.display.flip()
    
    elif PANTALLA == 4:
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                running = False
            
        screen.blit(fondo, rect_fondo)
        lista_ranking = listar_filas()
        funciones.crear_ranking(lista_ranking, screen)            
        pygame.display.flip()


pygame.quit()

