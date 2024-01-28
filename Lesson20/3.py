import pygame as pg
import random
pg.init()
W,H,FPS = 500,500,120
size = (W,H)
clock = pg.time.Clock()
win = pg.display.set_mode(size)

# class Circle:
#     def __init__(self,x,y,rad):
#         self.rad = rad
#         self.x = x
#         self.y = y
#         self.dx = random.choice([-1,-0.5,-0.25,0.25,0.5,1])
#         self.dy = random.choice([-1,-0.5,-0.25,0.25,0.5,1])
#         self.color = random.choices(range(0,256), k=3)
#     def move(self):
#         self.x += self.dx
#         self.y += self.dy
#         if self.x > W or self.x < 0:
#             self.dx = -self.dx + random.randint(-1,1)
#         if self.y > H or self.y < 0:
#             self.dy = -self.dy + random.randint(-1,1)
#     def show(self):
#         pg.draw.circle(win,self.color,(self.x,self.y),self.rad)
# circles = []
# for i in range(100):
#     circles.append(Circle(W // 2,H // 2,50))
    
def load_image(Photo):
    img = pg.image.load(Photo)
    img = img.convert()
    colorkey = img.get_at((0,0))
    img.set_colorkey(colorkey)
    return img

img = load_image("/Users/iliyabezrukov/projects/It-Park Course/Lesson20/Mister_pig.png")
img = pg.transform.scale(img,(100,100))
all_sprites = pg.sprite.Group()

for i in range(100):
    sprite = pg.sprite.Sprite(all_sprites)
    sprite.image = img
    sprite.rect = sprite.image.get_rect()

    sprite.rect.x = random.randrange(W)
    sprite.rect.y = random.randrange(H)
while True:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()
    
    win.fill((255,255,255))
    all_sprites.draw(win)
    # for circle in circles:
    #     circle.move()
    # for circle in circles:
    #     circle.show()
    pg.display.update()
    clock.tick(FPS)