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
object_to_draw = "rect"
size = 50
flag = 1
win. fill (WHITE) 
pygame. display.update() 
 

while True:
    keys = pygame.key.get_pressed()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
    if keys[pygame.K_w]:
        object_to_draw = "circle"
    if keys[pygame.K_q]:
        object_to_draw = "rect"

    size += flag
    if size > 200:
        flag = -1
    if size < 50:
        flag = 1
    if object_to_draw == "circle":
        pygame.draw.circle(win,random.choices(range(0,256),k = 3),pygame.mouse.get_pos(),size //2)
        pygame.display.update()
    elif object_to_draw == "rect":
        x,y = pygame.mouse.get_pos()
        pygame.draw.rect(win,random.choices(range(0,256), k = 3),(x- size // 2,y - size // 2,size,size))
        pygame.display.update()
    if keys[pygame.K_SPACE]:
        win.fill(WHITE)
        pygame.display.update()
    pygame. time. delay (20)

