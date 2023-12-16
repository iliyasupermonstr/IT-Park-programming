
import pygame
pygame.init()
win = pygame.display.set_mode((500, 500))

class Circle:
    def __init__(self, x, y, rad, col):
        self.x = x
        self.y = y
        self.col = col
        self.rad = rad
    
    def draw(self):
        pygame.draw.circle(win, self.col, (self.x, self.y), self.rad)
    
    def move_by_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.rad
        if keys[pygame.K_RIGHT]:
            self.x += self.rad
        if keys[pygame.K_UP]:
            self.y -= self.rad
        if keys[pygame.K_DOWN]:
            self.y += self.rad

circle = Circle(400, 300, 50, (33, 150, 243))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    circle.move_by_keys()
    
    win.fill((0, 0, 0))
    circle.draw()
    
    pygame.display.update()
    pygame.time.delay(50)
