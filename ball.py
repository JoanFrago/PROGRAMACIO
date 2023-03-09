import pygame
import os

ANCHO, ALTO = 900, 500
ANCHO_CACA, ALTO_CACA = 70, 70

BORDER_LEFT = 0
BORDER_RIGHT = ANCHO
BORDER_UP = 0
BORDER_DOWN = ALTO

BLUE = (0,0,255)
BLACK = (0,0,0)

VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('ball game')

FPS = 60

VELOCIDAD = 5
_SALTO_ = 200
SALTO = ALTO - _SALTO_

NUM_SALTO_MAX = 1

CACA_IMAGE = pygame.image.load(os.path.join('Assets', 'caca.jpg'))
CACA = pygame.transform.rotate(pygame.transform.scale(CACA_IMAGE, (
    ANCHO_CACA, ALTO_CACA)), 0)

def draw_window():
    
    VENTANA.fill(BLUE, pygame.Rect(0, 0, ANCHO, ALTO))

    pygame.display.update()

def handle_ball_up():
    pass

def handle_ball_stationary():
    while jumping == False:
        VENTANA.blit(CACA, (ANCHO/2, ALTO), caca, 1)

def main():
    
    jumping = False
    caca = pygame.Rect(ANCHO/2, ALTO, ANCHO_CACA, ALTO_CACA)
    
    time = pygame.time.Clock()
    run = True
    while run:
        time.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                
        keys_pressed = pygame.key.get_pressed()
        draw_window()
        handle_ball_up(keys_pressed, jumping, caca)
        handle_ball_stationary(jumping, caca)
        
if __name__ == '__main__':
    main()