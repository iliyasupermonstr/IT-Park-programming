import pygame
pygame.init()
win = pygame.display.set_mode((500, 500))
rad = int(input("Введите радиус круга"))
x = 250
y = 250
center_x = 250
center_y = 250
color = (255, 255, 255)
BLUE = (33,150,243)
moving = False
win.fill(color)
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= rad
    if keys[pygame.K_RIGHT]:
        x += rad
    if keys[pygame.K_UP]:
        y -= rad
    if keys[pygame.K_DOWN]:
        y += rad
    if x < rad:
        x = rad
        moving = True
    elif x > 500-rad:
        x = 500-rad
        moving = True
    elif y < rad:
        y = rad
        moving = True
    elif y > 500-rad:
        y = 500-rad
        moving = True
    if moving:
        x += (center_x - x) // 20
        y += (center_y - y) // 20

    win.fill(color)
    pygame.draw.circle(win,BLUE,(x,y),rad)
    pygame.display.update()
    pygame.time.delay(50)