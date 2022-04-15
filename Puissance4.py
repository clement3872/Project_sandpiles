###################################
# Groupe MI TD4
# DESFONTAINES Alexia
# MURAT Feyzanur
# FATNASSI Matéo
# MARCHAL Clément
# https://github.com/clement3872/Puissance4.git
###################################

import tkinter as tk


def create_token(x,y,color="white", outline_=""):
    global canvas
    x0,y0, x1,y1 = x+BORDER,y+BORDER, x+radius+BORDER, y+radius+BORDER
    canvas.create_oval(x0,y0, x1,y1, fill=color, outline="blue")


radius = 75
BORDER = 20
WITDH,HEIGHT = 7*radius + BORDER, 6*radius + BORDER


root = tk.Tk()
canvas = tk.Canvas(root,bg="blue", width=WITDH, height=HEIGHT)
canvas.pack()

create_token(0,0)

root.mainloop()