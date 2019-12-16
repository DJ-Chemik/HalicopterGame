import pygame
import time
import os
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

copokazuje = "menu"
while True:
    for event in pygame.event.get(): #przejdź po wszystkich elementach listy zdarzeń
        if event.type==pygame.QUIT: #jeśli naciśniemy klawisz X w oknie
            pygame.quit() #zamyka okno gry
            #quit() #zamyka IDLE
    if copokazuje=="menu":
        napisz("Naciśnij Spacje by zacząć",80,150,20,True)
        grafika = pygame.image.load(os.path.join('logo.png'))
        screen.blit(grafika, (80,30))
    pygame.display.update()
    
