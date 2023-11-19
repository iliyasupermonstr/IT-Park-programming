import tkinter as tk

print("start")
win = tk.Tk()
canvas = tk.Canvas(bg ="white", width=700,height=700)
canvas.create_line((320, 350), (380, 350),(350,300),(320,350), fill='black')
canvas.pack()#Активация Canvas
win.mainloop() #Главный цикл(Создает окошко)
print("stop")