import pygame
pygame.init()
win = pygame.display.set_mode((600,600))
color = (255,255,255)
win.fill(color)
pygame.draw.rect(win,(29,29,29), (250,250,100,100))
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
