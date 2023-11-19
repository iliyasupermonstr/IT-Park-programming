
from tkinter import *
win = Tk()
win.title("Шашки")
size = 400
amount = 8 
canvas = Canvas(height=size,width = size)
for i in range(0,size,50):
    canvas.create_line((i,0),(i,size),fill="black")
for b in range(0,size,50):
    canvas.create_line((0,b),(size,b),fill="black")
for y in range(3):
    for x in range (4):
        x_real=(2*x + (y%2))* 50
        y_real = y * 50
        canvas.create_oval((x_real,y_real),(x_real + 50),y_real + 50, fill ="black")

        x_real=(2*x + ((7-y)%2))* 50
        y_real = (7 -y) * 50
        canvas.create_oval((x_real,y_real),(x_real + 50),y_real + 50, fill ="white")
canvas.pack()
win.mainloop()