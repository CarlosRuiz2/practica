import pygame, sys

pygame.init()
#modificar la pantalla
ancho=960
alto=540

Win=pygame.display.set_mode((ancho,alto))
backgraund_image=pygame.image.load("cuadro.png").convert
backgraund_rect=backgraund_image.get.rect()

#titulo
pygame.display.set_caption("saltar")









correr=True
while correr:
    for event in pygame.event.get():
        if  event.type== pygame.QUIT:
            correr=False
    pygame.display.flip()
pygame.quit()