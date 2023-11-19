import tkinter as tk

print("start")
win = tk.Tk()
canvas = tk.Canvas(bg ="#ADFF2F", width=640,height=480)
#bg - background
canvas.pack()
win.mainloop() #Главный цикл(Создает окошко)
print("stop")