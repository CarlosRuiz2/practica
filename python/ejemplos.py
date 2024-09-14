import pygame, sys
from pygame.locals import *
pygame.init()
bloqueto=pygame.image.load("C:\Users\Usuario\Desktop\programa\imagen/slime.png")
img=pygame.image.load("C:\Users\Usuario\Desktop\programa\imagen/slime.png")
isjump=False
x=10
y=10
x_1=50
y_2=50
ancho=1000
alto=600
white=(255,255,255)
lado=20

pygame.display.set_caption("Mother")
win=pygame.display.set_mode((ancho, alto))




while True:
    win.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if event.type==pygame.KEYDOWN:
        if event.key==K_DOWN:
            y=y+0.5
        if event.key==K_UP:
            y=y-0.5
        if event.key==K_RIGHT:
            x=x+0.5
        if event.key==K_LEFT:
            x=x-0.5
    win.fill(white)
    win.blit(bloqueto,(x,y))
    pygame.display.update()