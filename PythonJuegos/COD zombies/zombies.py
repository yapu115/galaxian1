import pygame

def crear_zombies(x, y, ancho, alto):
    zombie = pygame.image.load("zombies.01.png")
    zombie = pygame.transform.scale(zombie, (ancho, alto)) #200 400
    rect_zombie = zombie.get_rect()
    rect_zombie.centerx = x
    rect_zombie.centery = y
    dict_zombie = {}
    dict_zombie["surface"] = zombie
    dict_zombie["rect"] = rect_zombie
    return dict_zombie

def actualizar_pantalla(lista_zombies, pantalla):
    for zombie in lista_zombies:
        pantalla.blit(zombie["surface"], zombie["rect"])
