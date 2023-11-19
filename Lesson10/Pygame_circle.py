import pygame
pygame.init()
win = pygame.display.set_mode((600,600))
color = (255,255,255)
win.fill(color)
pygame.draw.circle(win,(254,200,51), (300,300),50)
pygame.draw.circle(win,(249,76,53), (300,450),50)
pygame.draw.circle(win,(45,200,68), (300,150),50)
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
