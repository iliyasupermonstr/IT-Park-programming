import pygame as pg  
 
BLACK = (0,0,0) 
GRAY = (100, ) * 3 
WHITE = (255,) * 3  
RED = (255, 0, 0) 
 
CROSS = '#046582' 
CIRCLE = '#e4bad4' 
 
pg. init() 
W, H = 600, 600 
screen = pg.display.set_mode((W, H)) 
 
def draw_circle(sc, x, y, size): 
    x = (x + 0.5) * size 
    y = (y + 0.5) * size 
    pg.draw.circle(sc, CIRCLE, (x, y), (size - 3) // 2, 3) 
     
def draw_cross(sc, x, y, size): 
    x = x * size + 3 
    y = y * size + 3 
    pg.draw.line(sc, CROSS, (x, y), (x + size - 3, y + size - 3), 3) 
    pg.draw.line(sc, CROSS, (x + size - 3, y - 3), (x, y+ size - 3), 3) 
    
def is_end(board): 
    check_i_line = lambda x, i: True if x[i][0] == x[i][1] == x[i][2] != 0 else False 
    check_i_col = lambda x, i: True if x[0][i] == x[1][i] == x[2][i] != 0 else False 
    check_main_diag = lambda x: True if x[0][0] == x[1][1] == x[2][2] != 0 else False 
    check_secondary_diag = lambda x: True if x[0][2] == x[1][1] == x[2][0] != 0 else False 
 
    for i in range(3): 
        if check_i_col(board, i): 
            return 'col', i 
        if check_i_line(board, i): 
            return 'line', i 
    if check_main_diag(board): 
        return 'diag', 1 
    if check_secondary_diag(board): 
        return 'diag', 2 
    return None 
 
# def check_secondary_diag(x): 
#     if x[0][2] == x[1][1] == x[2][0] != 0: 
#         return True 
#     else: 
#         return False 
 
# def check_i_line(x, i): 
#     if x[i][0] == x[i][1] == x[i][2] != 0: 
#         return True 
#     else: 
#         return False 
 
# def check_i_col(x, i): 
#     if x[i][0] == x[i][1] == x[i][2] != 0: 
#         return True 
#     else: 
#         return False 
 
# def check_main_diag(x, i): 
#     if x[0][0] == x[1][1] == x[2][2] != 0: 
#         return True 
#     else: 
#         return False 
 
# def check_secondary_diag(x, i): 
#     if x[0][2] == x[1][1] == x[2][0] != 0: 
#         return True 
#     else: 
#         return False 
 
class Board: 
    def __init__(self, W, H, size): 
        self.W, self.H = W, H 
        self.size = size 
        self.board = [ 
            [0, 0, 0], 
            [0, 0, 0], 
            [0, 0, 0] 
        ] 
        self.move = 1 
    def click(self, mouse_pos): 
        x = mouse_pos[0] // self.size 
        y = mouse_pos[1] // self.size 
        self.board[y][x] = self.move 
        self.move = -self.move 
     
    def render(self, screen):    
        for i in range(1, 3): 
            pg.draw.line(screen, GRAY, (i * self.size, 0), (i * self.size, self.H), 3) 
            pg.draw.line(screen, GRAY, (0, i * self.size), (self.W, i * self.size), 3) 
        for y in range(3): 
            for x in range(3): 
                if  self.board[y][x] == 1: 
                    draw_cross(screen, x, y, self.size) 
                elif self.board[y][x] == -1: 
                    draw_circle(screen, x, y, self.size) 
     
    def check_end(self): 
        is_end_info = is_end(self.board) 
        shift = self.W // 10 
        if is_end_info is not None: 
            type_end = is_end_info[0] 
            number = is_end_info[1] 
            if type_end == 'col': 
                x0, y0 = (number + 0.5) * self.size, shift   
                x1, y1 = (number + 0.5) * self.size, 3 * self.size - shift   
            elif type_end == 'line':   
                x0, y0 = shift, (number + 0.5) * self.size   
                x1, y1 = 3 * self.size - shift, (number + 0.5) * self.size   
            elif type_end == 'diag':   
                if number == 1:   
                    x0, y0 = shift, shift 
                    x1, y1 = 3 * self.size - shift, 3 * self.size - shift 
                else:   
                    x0, y0 = 3 * self.size - shift, shift 
                    x1, y1 = shift, 3 * self.size - shift 
            pg.draw.line(screen, RED, (x0, y0), (x1, y1), 10) 
            pg.display.update() 
            pg.time.delay(3000) 
            return True 
        else: 
            return False 
 
board = Board(W, H, 200) 
while True: 
    for event in pg.event.get(): 
        if event.type == pg.QUIT:
            pg.quit() 
            exit() 
        if event.type == pg.MOUSEBUTTONDOWN: 
            board.click(event.pos) 
 
    screen.fill(WHITE) 
    board.render(screen) 
    pg.display.update() 
     
    keys = pg.key.get_pressed() 
    if keys[pg.K_ESCAPE] or board.check_end(): 
        pg.quit() 
        exit()