# import tkinter
# import random
# from tkinter import PhotoImage

# def repair_and_start():
#     global player 
#     canvas.delete("all")
#     player_pos = (random.randint(1,N_X -1)* step,
#                   random.randint(1, N_Y - 1) * step)
#     player=canvas.create_image((player_pos[0],player_pos[0]),image = player_pic,anchor="nw")
#     master.bind("<KeyPress>",key_pressed)

# def move_wrap(obj,move_x,move_y):
#     xy = canvas.coords(obj)
#     canvas.move(obj,move_x,move_y)
#     print(xy)
#     if xy[0] <= 0:
#         canvas.move(obj,WIDTH,0)
#     if xy[0] >= 0:
#         canvas.move(obj,-WIDTH,0)
#     if xy[1] <= 0:
#         canvas.move(obj,0,HEIGHT)
#     if xy[1] >= 0:
#         canvas.move(obj,0,-HEIGHT)
# def key_pressed(event):
#     if event.keysym == "Up":
#         move_wrap(player,0,-step)
#     if event.keysym == "Down":
#         move_wrap(player,0,step)
#     if event.keysym == "Right":
#         move_wrap(player,step,0)
#     if event.keysym == "Left":
#         move_wrap(player,-step,0)
# master = tkinter.Tk()
# step = 32
# N_X = 20
# N_Y = 20
# WIDTH = step * N_X
# HEIGHT = step * N_Y
# player_pic = tkinter.PhotoImage(file =r"/Users/iliyabezrukov/projects/It-Park Course/Lesson10/pixil-frame-0.png")
# restart = tkinter.Button(master,text = "Начать заново",command = repair_and_start)

# canvas = tkinter.Canvas(bg = "green", width = WIDTH,height = HEIGHT)
# label = tkinter.Label(text = "Найди выход!")
# restart.pack()
# label.pack()
# canvas.pack()
# repair_and_start()
# master.bind("KeyPress",key_pressed)
# tkinter.mainloop()
import tkinter 
import random 
from tkinter import PhotoImage 
 
 
# Функция для подготовки и запуска игры 
def prepare_and_start(): 
    global player 
    global circle 
    canvas.delete("all") # Очищаем холст 
    player_pos = (random.randint(1, N_X - 1) * step, 
    random.randint(1, N_Y - 1) * step) # Получаем случайную позицию игрока 
    player = canvas.create_image((player_pos[0], player_pos[1]), image=player_pic, anchor='nw') # Создаем изображение игрока на холсте 
    label.config(text="Найди выход") # Меняем текст метки 
    master.bind("<KeyPress>", key_pressed) # Привязываем функцию key_pressed к событию нажатия клавиши 
    circle_pos = (random.randint(1, N_X - 1) * step, 
    random.randint(1, N_Y - 1) * step) # Получаем случайные координаты для круга 
    circle = canvas.create_oval( 
    circle_pos[0], circle_pos[1], circle_pos[0]+step, circle_pos[1]+step, 
    outline="black", fill="red") # Создаем круг на холсте 
    
def check_collision(): 
    global circle 
    overlap = canvas.find_overlapping(*canvas.bbox(player)) # Находим пересечение между игроком и другими объектами на холсте 
    if circle in overlap: # Если круг присутствует в пересечении 
        label.config(text="Победа!") # Изменяем текст метки на "Победа!" 
    canvas.delete(circle) # Удаляем круг с холста 
 
 
# Функция для перемещения объекта с обработкой обертывания 
def move_wrap(obj, move_x, move_y): 
    xy = canvas.coords(obj) # Получаем текущие координаты объекта 
    canvas.move(obj, move_x, move_y) # Перемещаем объект на указанное расстояние  
    if xy[0] <= 0: 
        canvas.move(obj, WIDTH, 0) # Если объект перешел за границу холста, оборачиваем его на другую сторону 
    if xy[0] >= WIDTH: 
        canvas.move(obj, -WIDTH, 0) 
    if xy[1] <= 0: 
        canvas.move(obj, 0, HEIGHT) 
    if xy[1] >= HEIGHT: 
        canvas.move(obj, 0, -HEIGHT) 
    
# Функция обработки нажатия клавиш 
def key_pressed(event): 
    if event.keysym == 'Up': 
        move_wrap(player, 0, -step) # Если нажата клавиша "Вверх", перемещаем игрока вверх 
    elif event.keysym == 'Down': 
        move_wrap(player, 0, step) # Если нажата клавиша "Вниз", перемещаем игрока вниз 
    elif event.keysym == 'Right': 
        move_wrap(player, step, 0) # Если нажата клавиша "Вправо", перемещаем игрока вправо 
    elif event.keysym == 'Left': 
        move_wrap(player, -step, 0) # Если нажата клавиша "Влево", перемещаем игрока влево 
    check_collision() 
 
 
 
master = tkinter.Tk() # Создаем окно 
step = 32 # Размер одного шага игрока 
N_X = 20 # Количество клеток по горизонтали 
N_Y = 20 # Количество клеток по вертикали 
WIDTH = step * N_X # Ширина холста в пикселях 
HEIGHT = step * N_Y # Высота холста в пикселях 
player_pic = tkinter.PhotoImage(file=r"/Users/iliyabezrukov/projects/It-Park Course/Lesson10/pixil-frame-0.png") # Загружаем изображение игрока 
 
canvas = tkinter.Canvas(master, bg="blue", width=WIDTH, height=HEIGHT) # Создаем холст 
label = tkinter.Label(master, text="Не попадись") # Создаем метку с текстом 
restart = tkinter.Button(master, text="Начать заново", command=prepare_and_start) # Создаем кнопку 
restart.pack() # Размещаем кнопку на окне 
label.pack() 
canvas.pack() # Размещаем холст на окне 
prepare_and_start() # Подготавливаем и запускаем игру 
master.bind("<KeyPress>", key_pressed) # Привязываем функцию key_pressed к событию нажатия клавиши 
master.mainloop() # Запускаем главный цикл программы