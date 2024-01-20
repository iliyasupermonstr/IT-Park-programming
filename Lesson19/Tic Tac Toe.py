import pygame as pg

BLACK = (0,0,0)
GRAY = (100,100,100)
WHITE = (255,255,255)
RED = (255,0,0)
W,H = 600,600
pg.init()
screen =pg.display.set_mode((W,H))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.QUIT()
            exit()

    screen.fill(WHITE)
    pg.display.update()