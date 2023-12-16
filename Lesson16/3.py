
import pygame
pygame.init()
win = pygame.display.set_mode((500, 500))

class Circle:
    def __init__(self, x, y, rad, col):
        self.x = x
        self.y = y
        self.col = col
        self.rad = rad
        self.isJump = False
        self.jumpCount = 10
    
    def draw(self):
        pygame.draw.circle(win, self.col, (self.x, self.y), self.rad)
    
    def move_by_keys(self):
        keys = pygame.key.get_pressed()
        self.keys = keys
        if keys[pygame.K_LEFT]:
            self.x -= self.rad
        if keys[pygame.K_RIGHT]:
            self.x += self.rad
        if keys[pygame.K_UP]:
            self.y -= self.rad
        if keys[pygame.K_DOWN]:
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


            

circle = Circle(400, 300, 50, (33, 150, 243))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    circle.move_by_keys()
    
    win.fill((0, 0, 0))
    circle.draw()

    circle.jump()
        
    
    pygame.display.update()
    pygame.time.delay(50)
