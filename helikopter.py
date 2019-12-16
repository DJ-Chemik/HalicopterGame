import pygame
import time
def napisz(tekst, x, y, rozmiarCzcionki, czyWysrodkowany=True):
    cz=pygame.font.SysFont("Arial", rozmiarCzcionki,0,0)
    rend=cz.render(tekst,1,(255,100,100))
    xx=x
    yy=y
    if(czyWysrodkowany==True):
        xx=(szer-rend.get_rect().width)/2
        yy=(wys-rend.get_rect().height)/2
    screen.blit(rend, (xx,yy))

pygame.init()
szer = 600
wys = 600
screen = pygame.display.set_mode((szer,wys))
napisz("Naciśnij Spacje by zacząć",80,150,20,True)
pygame.display.update()
