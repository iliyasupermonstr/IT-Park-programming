
import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))
color = (255, 255, 255)

f_c = True
s_c = False
f = True
s = False
x_c = 0
y_c = 150
x = 250
y = 475

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    win.fill(color)

    if f == True:
        y -= 1
        pygame.draw.circle(win, (29, 29, 29), (x, y), 25)
        if y == 25:
            f = False
            s = True

    if s == True:
        y += 1
        pygame.draw.circle(win, (29, 29, 29), (x, y), 25)
        if y == 475:
            f = True
            s = False

    if f_c == True:
        x_c += 1
        pygame.draw.rect(win, (29, 29, 29), (x_c, y_c, 100, 150))
        if x_c == 400:  # Изменено на 400, чтобы учесть ширину прямоугольника
            f_c = False
            s_c = True

    if s_c == True:
        x_c -= 1
        pygame.draw.rect(win, (29, 29, 29), (x_c, y_c, 100, 150))
        if x_c == 0:
            f_c = True
            s_c = False

    pygame.display.flip()
    clock.tick(60)