import random
import pygame
pygame.init()
win = pygame.display.set_mode((500, 500))
list_circles =[]
FPS = 1000
pon = pygame.time.Clock()

class Circle:
    def __init__(self, x, y, rad, col):
        self.x = x
        self.y = y
        self.col = col
        self.rad = rad
        self.isJump = False
        self.jumpCount = 10
        self.dir = "right"
    
    def draw(self):
        pygame.draw.circle(win, self.col, (self.x, self.y), self.rad)
    
    def move_by_keys(self):
        keys = pygame.key.get_pressed()
        self.keys = keys
        if self.y == 500:
            self.y -= 50
        if self.y == 0:
            self.y += 50
        elif keys[pygame.K_UP]:
            self.y -= self.rad
        elif keys[pygame.K_DOWN]:
            self.y += self.rad
    def jump(self):
        if self.keys[pygame.K_SPACE]:
            self.isJump = True

        if self.isJump is True:

            if self.jumpCount >= -10:

                if self.jumpCount < 0:
                    self.y += (self.jumpCount ** 2) / 2
                else:
                    self.y -= (self.jumpCount ** 2) / 2

                self.jumpCount -= 1

            else:
                self.isJump = False
                self.jumpCount = 10
    def horizontal_move(self):
        if self.dir == "right":
            self.x += 1
            if self.x > 500:
                self.dir = "left"
        else:
            self.x -= 1
            if self.x < 0:
                self.dir = "right"

            


for i in range(100):
    list_circles.append(Circle(i * 10,i * 5,30,random.choices(range(256), k = 3)))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    win.fill((255,255,255))
    for circle in list_circles:
        circle.draw()
        circle.horizontal_move()
    pygame.display.flip()
    pon.tick(FPS)
