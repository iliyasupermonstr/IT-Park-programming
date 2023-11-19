import tkinter as tk

print("start")
win = tk.Tk()
canvas = tk.Canvas(bg ="#ADFF2F", width=700,height=700)
canvas.create_oval((0, 0), (700, 700), fill="blue",outline="red",width=200)
#canvas.create_line((0, 0), (100, 200), (300, 300), (200, 100), (0, 0), Fill="black")
canvas.pack()
win.mainloop() #Главный цикл(Создает окошко)
print("stop")