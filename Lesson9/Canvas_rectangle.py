import tkinter as tk

print("start")
win = tk.Tk()
canvas = tk.Canvas(bg ="yellow", width=700,height=700)
canvas.create_rectangle(175,175,525,525)
canvas.pack()#Активация Canvas
win.mainloop() #Главный цикл(Создает окошко)
print("stop")