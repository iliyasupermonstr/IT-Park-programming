import pygame
pygame.init()
win = pygame.display.set_mode((500, 500))
rad = int(input("Введите радиус круга"))
x = 400
y = 300
color = (255, 255, 255)
BLUE = (33,150,243)
win.fill(color)
while True:
    pygame.draw.circle(win,BLUE,(x,y),rad)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("Левая стрелка")
                x -= rad
            elif event.key == pygame.K_RIGHT:
                print("Правая стрелка")
                x += rad
            elif event.key == pygame.K_UP:
                print("Стрелка вверх")
                y -= rad
            elif event.key == pygame.K_DOWN:
                print("Стрелка вниз")
                y += rad
    pygame.display.update()