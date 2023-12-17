import pygame
import sys
import random

class Circle:
    def __init__(self, x, y, rad, color, direction):
        self.x = x
        self.y = y
        self.rad = rad
        self.color = color
        self.dir_x = random.choice([-1, 1])
        self.dir_y = random.choice([-1, 1])

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.rad)

    def move(self):
        self.x += self.dir_x
        self.y += self.dir_y
        if self.x > screen_width or self.x < 0:
            self.dir_x *= -1
        if self.y > screen_height or self.y < 0:
            self.dir_y *= -1

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

circles = []

running = True
circle_timer = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_time = pygame.time.get_ticks()
    if current_time - circle_timer > 3000:
        circle = Circle(random.randint(0, screen_width), random.randint(0, screen_height), 30,
                        (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), "")
        circles.append(circle)
        circle_timer = current_time
    screen.fill((255, 255, 255))

    for circle in circles:
        circle.move()
        circle.draw(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()