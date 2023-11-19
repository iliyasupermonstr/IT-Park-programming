import pygame

pygame.init()
user_input = input("Введите сначала размера экрана,потом сколько нужно клеток через пробел: ")
user_nums = user_input.split()
if user_nums[0].isdigit() and user_nums[1].isdigit:
    size = int(user_nums[0])
    num_squares = int(user_nums[1])
    if size % num_squares != 0:
        print("Размер должен быть кратен числу клеток")
        exit(-1)
    pixels_per_square = size / num_squares
    white =(255,255,255)
    black = (0,0,0)
    win = pygame.display.set_mode((size, size))
    color = (255,255,255)
    win.fill(color)

    for y in range(0, num_squares):
        for x in range(0, num_squares):
            is_black = (x + y) % 2 == 0
            cx = int(x * pixels_per_square)
            cy = int(size - (y + 1) * pixels_per_square)
            rect = pygame.Rect(cx, cy, pixels_per_square, pixels_per_square)

            if is_black:
                pygame.draw.rect(win, black, rect)

    pygame.display.update()
else:
    print("Ошибка,напишите два числа через пробел")
    exit(-1)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()