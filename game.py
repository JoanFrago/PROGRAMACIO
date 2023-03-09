import pygame
import sys

tecla_w = sys.stdin.read(1)
tecla_a = sys.stdin.read(1)
tecla_s = sys.stdin.read(1)
tecla_d = sys.stdin.read(1)

pygame.init()

ventana = pygame.display.set_mode((800,500))
pygame.display.set_caption("SOMOS SWRIKERS")


while True:
    
    for event in pygame.event.get():
        que_color = str(input("Escribe un color "))
        '''
            vamos a hacer que se modifique el color de fondo
            cuando se pulsen algunas teclas en concreto.
        '''
        #Cuando el evento es presionar una tecla...
        if event.type == pygame.KEYDOWN:
            #Obtenemos el mapping de teclas presionadas
            
            if tecla_a == True:
                #Rellenamos la ventana con un color de Pygame
                ventana.fill(pygame.Color("blue"))
            if tecla_w == True:
                ventana.fill(pygame.Color("red"))
            if tecla_s == True:
                ventana.fill(pygame.Color("green"))
            if tecla_d == True:
                ventana.fill(pygame.Color("green"))
    
    for event in pygame.event.get():    #Cuando ocurre un evento...
        if event.type == pygame.QUIT:   #Si el evento es cerrar la ventana
            pygame.quit()               #Se cierra pygame
            sys.exit()                  #Se cierra el programa

    pygame.display.flip()               #Genera la ventana
