import tkinter as tk

print("start")
win = tk.Tk()
canvas = tk.Canvas(bg ="white", width=700,height=700)
canvas.create_polygon()
canvas.pack()#Активация Canvas
win.mainloop() #Главный цикл(Создает окошко)
print("stop")