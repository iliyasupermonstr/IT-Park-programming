import pygame
pygame.init()
win = pygame.display.set_mode((600,600))
color = (255,255,255)
win.fill(color)
pygame.draw.polygon(win,(0,0,0),[(0,100),(100,50),(100,150)],False)
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
