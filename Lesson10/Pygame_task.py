import pygame
pygame.init()
a = input("Введите два числа размера экрана через пробел:")
num1 = a.split()
if num1[0].isdigit() and num1[1].isdigit:
    c = int(num1[0])
    d = int(num1[1])

    win = pygame.display.set_mode((c,d))
    color = (0,0,0)
    win.fill(color)
    pygame.draw.line(win,(238,238,238),(0,0),(c,d),5)
    pygame.display.update()
    pygame.draw.line(win,(238,238,238),(c,0),(0,d),5)

    pygame.display.update()
    pygame.display.update()
else:
    print("Ошибка,напишите два числа через пробел")
    exit()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()