from tkinter import *
from frame_1 import FrameOne
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"

window = Tk()
window.title("Flashy")
window.minsize(850, 700)
window.maxsize(850, 700)

f1 = Frame(window, bg=YELLOW)
f1.config(padx=20, pady=60)
f1.grid(row=0, column=0, sticky="news")
f2 = Frame(window, bg=GREEN)
f2.config(padx=25, pady=20)
f2.grid(row=0, column=0, sticky="news")

frame_1 = FrameOne(f1, color1=PINK, color2=YELLOW, frame2=f2, color3=GREEN)

f1.tkraise()
window.mainloop()

