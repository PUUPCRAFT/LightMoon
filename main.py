from tkinter import Tk,Button
import tkinter as tk
main_win = Tk()
main_win.title('LightMoon')
width = 450 
height = 450 
main_win.geometry(f'{width}x{height}')

var = tk.StringVar()
l = tk.Label(main_win, textvariable=var,font=('Arial', 12),width=15,height=2)
l.pack()
def hit():
  var.set('hello')
b = tk.Button(main_win, text='点我', width=15, height=2, command=hit)
b.pack()


main_win.mainloop()
