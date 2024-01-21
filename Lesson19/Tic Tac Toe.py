import pygame as pg

BLACK = (0,0,0)
GRAY = (100,100,100)
WHITE = (255,255,255)
RED = (255,0,0)
W,H = 600,600
CROSS = "#046582"
CIRCLE = "e4bad4"
pg.init()
screen =pg.display.set_mode((W,H))

def draw_circle(sc,x,y,size):
    x = (x + 0,5) + size
    y = (y + 0,5) + size
    pg.draw.circle(sc,CIRCLE,(x,y),(size - 3) // 2, 3)
def draw_cross(sc,x,y,size):
    x = x * size + 3
    y = y * size + 3
    pg.draw.line(sc,CROSS,(x,y),(x + size - 3,y + size - 3),3)
    pg.draw.line(sc,CROSS,(x + size - 3,y-3),(x,y + size - 3),3)
def is_end(board):
    check_i_line = lambda x,i: True if x[i][0] == x[i][1] == x[i][2] != 0 else False
    check_i_col = lambda x,i:True if x[0][i] == x[1][i] == x[2][i] != 0 else False
    check_main_diag = lambda x : True if x[0][0] == x[1][1] == x[2][2] != 0 else False
    check_second_diag = lambda x: True if x[0][2] == x[1][1] == x[2][0] !=0 else False
    for i in range(3):
        if check_i_col(board,i):
            return "col",i
        if check_i_line(board,i):
            return "line",i
    if check_main_diag(board,i):
        return "diag",1
    if check_second_diag(board,i):
        return "diag",2
    
class Board:
    def __init__(self,W,H,size):
        self.W = W
        self.H = H
        self.size = size
        self.board = [
            [0,0,0],
            [0,0,0],
            [0,0,0]
        ]
        self.move = 1
    def click(self,mouse_pos):
        x = mouse_pos[0] // self.size
        y = mouse_pos[1] // self.size
        self.board[y][x] = self.move
        self.move = -self.move

    def render(self,screen):
        pg.draw.line(screen,GRAY,(0,200),(self.W,200))
        pg.draw.line(screen,GRAY,(0,400),(self.W,400))
        pg.draw.line(screen,GRAY,(200,0),(200,self.H))
        pg.draw.line(screen,GRAY,(400,0),(400,self.W))
        for y in range(3):
            for x in range(3):
                if self.board[y][x] == 1:
                    draw_cross(screen,x,y,self.size)
                elif self.board[y][x] == -1:
                    draw_circle(screen,x,y,self.size)

board = Board(W,H,200)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.QUIT()
            exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            board.click(event.pos)
    
    screen.fill(WHITE)
    board.render(screen)
    pg.display.update()