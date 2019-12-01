import pygame
import datetime
import math
from pygame.locals import *
from math import pi
angle = pi
SIZE = 660, 660
pygame.init()
screen = pygame.display.set_mode(SIZE)
FPSCLOCK = pygame.time.Clock()
done = False
screen.fill((255, 255, 255))
t = datetime.datetime.now()
degree=0
d=t.hour*30-95
dg = t.minute*6-95
font = pygame.font.SysFont("comicsansms", 72)
text12 = font.render("12", True, (130, 80, 0))
text3 = font.render("3", True, (130, 80, 0))
text6 = font.render("6", True, (130, 80, 0))
text9 = font.render("9", True, (130, 80, 0))

while not done:
    screen.fill(255)
    for e in pygame.event.get():
        if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
            done = True
            break
        
    screen.fill((255,255,255))
    pygame.draw.rect(screen,(0,0,0),[100,100,460,460], 2)
    pygame.draw.arc(screen, (0,0,0), (100,100,560,820), pi/2, pi, 3)
    pygame.draw.arc(screen, (0,0,0), (150,100,410,400), 2*pi, pi/2, 3)
    pygame.draw.arc(screen, (0,0,0), (361,205,200,200), 3*pi/2, 0, 3)
    pygame.draw.arc(screen, (0,0,0), (397,275,130,130), pi, 3*pi/2, 3)
    pygame.draw.arc(screen, (0,0,0), (397,310,75,75), pi/2, pi, 3)
    pygame.draw.arc(screen, (0,0,0), (410,310,50,50), 2*pi, pi/2, 3)
    pygame.draw.arc(screen, (0,0,0), (436,320,25,25), 3*pi/2, 0, 3)
    radar = (436,330)
    radar_len = 115
    rlen=90

    x = radar[0] + math.cos(math.radians(degree)) * radar_len
    y = radar[1] + math.sin(math.radians(degree)) * radar_len
    
    a = radar[0] + math.cos(math.radians(d)) * rlen
    b = radar[1] + math.sin(math.radians(d)) * rlen
    
    p = radar[0] + math.cos(math.radians(dg)) * rlen
    q = radar[1] + math.sin(math.radians(dg)) * rlen
    
    screen.blit(text12,
        (400 - text12.get_width() // 2, 150 - text12.get_height() // 2))
    screen.blit(text3,
        (540 - text3.get_width() // 2, 325 - text3.get_height() // 2))
    screen.blit(text6,
        (400 - text6.get_width() // 2, 475 - text6.get_height() // 2))
    screen.blit(text9,
        (180 - text9.get_width() // 2, 325 - text9.get_height() // 2))
    
    pygame.draw.line(screen, Color("red"), radar, (x,y), 2)
    pygame.draw.line(screen, Color("blue"), radar, (a,b), 5)
    pygame.draw.line(screen, Color("green"), radar, (p,q), 5)
    pygame.display.flip()   
    degree+=5
    d+=0.00694444
    dg+= 0.0833333
    FPSCLOCK.tick(1)