import pygame
import os

FPS = 60
ANCHO, ALTO = 400, 550
WINDOW = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('salto al morabet')

YELLOW = (255,252,201)

ANCHO_BÚHO, ALTO_BÚHO = 40, 55
BÚHO_X, BÚHO_Y = ANCHO/2, ALTO-ALTO_BÚHO-5

BÚHO_IMAGE = pygame.image.load(os.path.join('PERSONAL', 'GAMES', 'DOODLE_JUMP', 'búho_stationary.png'))
BÚHO = pygame.transform.rotate(pygame.transform.scale(BÚHO_IMAGE, (ANCHO_BÚHO, ALTO_BÚHO)), 0)
buho = pygame.Rect(BÚHO_X, BÚHO_Y, ANCHO_BÚHO, ALTO_BÚHO)
VELOCIDAD_BÚHO = 5
GRAVITY = 1


WINDOW.blit(BÚHO, (BÚHO_X, BÚHO_Y), buho, 1)


time = pygame.time.Clock()
run = True
while run:
    time.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
    WINDOW.fill(YELLOW, pygame.Rect(0, 0, ANCHO, ALTO))
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed == pygame.K_SPACE or keys_pressed == pygame.K_UP:
        BÚHO_Y -= VELOCIDAD_BÚHO
        BÚHO_Y -= GRAVITY
        
        
    pygame.display.update()