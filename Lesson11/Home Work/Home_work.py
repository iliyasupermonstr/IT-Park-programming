import pygame
import random

pygame.init()

# Установка размеров окна
width=800
height = 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("DVD")

# Загрузка изображения DVD
dvd_logo = pygame.image.load("/Users/iliyabezrukov/projects/It-Park Course/Lesson11/Home Work/dvd-logo.png")
dvd_logo = pygame.transform.scale(dvd_logo, (50, 50))  

# Начальные координаты и скорости движения
x= random.randint(0, width - 50)
y=random.randint(0, height - 50)
speed_x, speed_y = 5, 5

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


    x += speed_x
    y += speed_y

    if x <= 0 or x >= width - 50:
        speed_x = -speed_x
    if y <= 0 or y >= height - 50:
        speed_y = -speed_y


    win.fill((255, 255, 255))


    win.blit(dvd_logo, (x, y))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()