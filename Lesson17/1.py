import pygame 
import sys
import random 
 
WHITE = (255, 255, 255) 
RED = (225, 0, 50) 
GREEN = (0, 225, 0) 
BLUE = (0, 0, 225)
BLACK = (0,0,0)
W,H = 500,500
win = pygame. display. set_mode((W,H)) 
win. fill (BLACK) 
pygame. display.update() 
 

while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
    
     
    pygame.draw.circle(win,WHITE,(random.randint(0,W),random.randint(0,H)),1)
    pygame.display.update()
    pressed =pygame.mouse.get_pressed()
    pos = pygame.mouse.get_pos()

    if pressed[0]:
        pygame.draw.circle(win,BLUE,pos,10)
        pygame.display.update()
        
    pygame. time. delay (20)

