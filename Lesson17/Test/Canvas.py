from tkinter import *

def move_by_keys(event):
    if event.keysym == "Up":
        canvas.move(oval, 0, -20)
    elif event.keysym == "Down":
        canvas.move(oval,0 ,  20)
    elif event.keysym == "Left":
        canvas.move(oval,-20,0)
    elif event.keysym == "Right":
        canvas.move(oval,20,0)
win = Tk()
label = Label(win,text="IT-Park")
label.pack()
canvas = Canvas(win,bg="#fff",width=700,height=700)
oval=canvas.create_oval((300,300),(400,400),fill="yellow")
canvas.pack()
win.bind("<KeyPress>",move_by_keys)
win.mainloop()