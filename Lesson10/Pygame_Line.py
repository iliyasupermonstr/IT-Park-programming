import pygame
pygame.init()
win = pygame.display.set_mode((600,600))
color = (255,255,255)
win.fill(color)
pygame.draw.line(win,(0,255,255),(0,0),(100,100),5)
pygame.draw.lines(win,(0,255,255),True,((200,200),(300,150),(300,250)),10)
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
