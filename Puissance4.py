###################################
# Groupe MI TD4
# DESFONTAINES Alexia
# MURAT Feyzanur
# FATNASSI Matéo
# MARCHAL Clément
# https://github.com/clement3872/Puissance4.git
###################################

import random
import tkinter as tk

def win_win(color):
    w = tk.Tk()
    w.geometry("200x75")
    w.config(bg=color)

    l_win = tk.Label(w, text=f"Team {color} won", font=(20,), bg=color)
    l_win.place(relx=.5, rely=.5, anchor="center")

    w.mainloop()


def create_grid_list():
    l = []

    for row in range(6):
        l.append([])
        for _ in range(7):
            l[row].append(-1)

    return l



def test():
    global canvas, l_tokens, COLUMNS_FULL, TEAM, l_moves

    i = len(l_tokens)-1
    if column > 6: column = 6
    elif column < 0: column = 0

    while l_tokens[i][column]!=0 and i>0: 
            i -= 1
    
    if column not in COLUMNS_FULL: 
        l_tokens[i][column%7] = TEAM
        TEAM = (TEAM)%2 + 1

    else: print("Column is full!")
        
    if i == 0: COLUMNS_FULL.append(column)


def get_win_diags(lines, team):
    pass

def get_win_line(line, team):
    pass


def do_won():
    global d_tokens
# pour gagner idée:
# si la jeton + la somme de son coin i +1 j+1 or j+1 i-1 or i-1 j-1 or i+1 j-1 == 4 alors gagner
    
    




def create_token(x,y,color="white", outline_=""):
    global canvas
    x0,y0, x1,y1 = x+BORDER,y+BORDER, x+radius+BORDER, y+radius+BORDER
    token = canvas.create_oval(x0,y0, x1,y1, fill=color, outline="blue")
    return token


def create_blanks():
    
    for i in range(6):
        for j in range(7):
            create_token(j*radius,i*radius)

def fall(token, y_max, id_after=None):
    global canvas

    dy = 30
    latency = 20
    y = canvas.coords(token)[3]

    if y > y_max:
        canvas.after_cancel(id_after)
    elif y+dy > y_max : 
        canvas.move(token,0, y_max-y)
    else:
        canvas.move(token,0,dy)
        id_after = canvas.after(latency, lambda:fall(token,y_max, id_after))


def add_token_to_list(y):
    global l_tokens_list



def add_token(event):
    global canvas, id_after, l_tokens_obj, team, l_moves, l_tokens
    x = (event.x- BORDER)//radius


    if (x >= 0) and (x <= 6) and (d_tokens[x]<6):

        ######## TEST
        """
        column = x 
        i = len(l_tokens)-1
        while l_tokens[i][column]!=-1 and i>0: 
                i -= 1
        """
        ########

        l_x_moves.append(x)
        d_tokens[x] += 1

        team = (team + 1) % 2
        l_tokens_obj.append(create_token(x* radius,0, team_color[team]))
        fall(l_tokens_obj[-1], HEIGHT-BORDER-((d_tokens[x]-1)*radius))


def undo(canvas):
    global d_tokens,l_tokens_obj,l_x_moves, team
    
    if l_x_moves != []:
        if d_tokens[l_x_moves[-1]] > 0:
            team = (team + 1) % 2
            d_tokens[l_x_moves.pop()] -= 1
            canvas.delete(l_tokens_obj.pop())

def reset(canvas):
    global d_tokens,l_tokens_obj,l_x_moves, team
    for token in l_tokens_obj:
        canvas.delete(token)
    d_tokens,l_tokens_obj,l_x_moves = {i:0 for i in range(7)}, [], []
    team = random.randint(0,1)



radius = 75
BORDER = 20
WITDH,HEIGHT = 7*radius + (BORDER*2), 6*radius + (BORDER*2)

d_tokens,l_tokens_obj,l_x_moves, l_tokens = {i:0 for i in range(7)}, [], [], []

team = random.randint(0,1)
team_color = ["red", "yellow"]

root = tk.Tk()

canvas = tk.Canvas(root,bg="blue", width=WITDH, height=HEIGHT)
b_undo = tk.Button(root,text="Undo", command=lambda:undo(canvas))
b_reset = tk.Button(root, text="Reset",command=lambda:reset(canvas))

canvas.grid(row=0, columnspan=2)
b_undo.grid(row=1, column=0)
b_reset.grid(row=1, column=1)

canvas.bind("<Button-1>", lambda event:add_token(event))

create_blanks()

root.mainloop()
