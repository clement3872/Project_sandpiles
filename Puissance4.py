###################################
# Groupe 3 - MI TD4
# DESFONTAINES Alexia
# MURAT Feyzanur
# FATNASSI Matéo
# MARCHAL Clément
# https://github.com/clement3872/Puissance4.git
###################################

import random
import tkinter as tk


def print_list(l):
    print()
    for el in l:
        print(el)
    print()


def win_win(color):
    w = tk.Tk()
    w.geometry("200x75")
    w.config(bg=color)

    l_win = tk.Label(w, text=f"Team {color} won", font=(20,), bg=color)
    if color == "white":
        w.geometry("300x75")
        l_win.config(text="Nobody won, the grid is full!")
    l_win.place(relx=.5, rely=.5, anchor="center")

    w.mainloop()


def create_grid_list():
    l = []

    for row in range(6):
        l.append([])
        for _ in range(7):
            l[row].append(-1)

    return l



def remove_token_to_list(): # not used
    global l_tokens, l_x_moves
    column = l_moves.pop()

    i = len(l_tokens)-1
    while (l_tokens[i][column]==0 or l_tokens[i][column]==1) and i>0: 
            i -= 1
    
    l_tokens[i][column] = -1

def add_token_to_list(column): # not used
    global canvas, l_tokens, columns_full, team, l_moves

    i = len(l_tokens)-1
    while l_tokens[i][column]!=-1 and i>0: 
            i -= 1
    
    l_tokens[i][column] = team


def get_win_line(l_tokens):

    for j in range(len(l_tokens)):
        tmp = l_tokens[j]
        for i in range(4):
            if tmp[i:i+4] == [0, 0, 0, 0] :
                return "red"
            elif tmp[i:i+4] == [1,1,1,1]:
                return "yellow"
    return "white"

def get_win_col(l_tokens):

    def get_col(l, i):
        col = []

        for j in range(len(l)):
            col.append(l[j][i])
        return col

    for C in range(len(l_tokens[0])):
        col = get_col(l_tokens, C)
        
        for i in range(3):
            if col[i:i+4] == [0, 0, 0, 0] :
                return "red"
            elif col[i:i+4] == [1,1,1,1]:
                return "yellow"
    return "white"

def get_win_diags(l_tokens):

    for x in range(4):
        for y in range(3):
            tmp1, tmp2 = [],[]
            for d in range(4):
                tmp1.append(l_tokens[y+d][x+d])
                tmp2.append(l_tokens[len(l_tokens)-1-y-d][x+d])

            if tmp1 == [0, 0, 0, 0] or tmp2 == [0, 0, 0, 0] :
                return "red"
            elif tmp1 == [1,1,1,1] or tmp2 == [1,1,1,1]:
                return "yellow"
    
    return "white"



def get_win():
    global d_tokens, l_tokens, winning_team, canvas

    if winning_team == "white":
        line_color = get_win_line(l_tokens)
        diags_color = get_win_diags(l_tokens)
        col_color = get_win_col(l_tokens)

        if line_color != "white": 
            winning_team = line_color
            win_win(winning_team)

        elif diags_color != "white":
            winning_team = diags_color
            win_win(winning_team)

        elif col_color != "white": 
            winning_team = col_color
            win_win(winning_team)
    
    return winning_team != "white"
        


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


def add_token(event, base_x=-1):
    global canvas, id_after, l_tokens_obj, team, l_moves, l_tokens

    if base_x == -1:
        x = (event.x- BORDER)//radius
    else:
        x = base_x


    if (x >= 0) and (x <= 6) and (d_tokens[x]<6):
        team = (team + 1) % 2

        column = x 
        i = len(l_tokens)-1
        while l_tokens[i][column]!=-1 and i>0: 
                i -= 1
        
        l_tokens[i][column] = team

        l_x_moves.append(x)
        d_tokens[x] += 1

        
        l_tokens_obj.append(create_token(x* radius,0, team_color[team]))
        fall(l_tokens_obj[-1], HEIGHT-BORDER-((d_tokens[x]-1)*radius))
        
        get_win()

        if len(l_tokens_obj) == 42:
            win_win("white")


def undo(canvas):
    global d_tokens,l_tokens_obj,l_x_moves, team, l_tokens

    if l_x_moves != []:
        column = l_x_moves.pop()

        if d_tokens[column] > 0:
            
            i = 6-d_tokens[column]
            l_tokens[i][column] = -1

            team = (team + 1) % 2
            d_tokens[column] -= 1
            canvas.delete(l_tokens_obj.pop())

def reset(canvas):
    global d_tokens,l_tokens_obj,l_x_moves, team,l_tokens, winning_team
    l_tokens = create_grid_list()
    winning_team = "white"
    for token in l_tokens_obj:
        canvas.delete(token)
    d_tokens,l_tokens_obj,l_x_moves = {i:0 for i in range(7)}, [], []
    team = random.randint(0,1)


def display_l_tokens(l_tokens):
    global canvas, team
    reset(canvas)

    for y in range(len(l_tokens)):
        for x in range(len(l_tokens[y])):
            if l_tokens[len(l_tokens)-1-y][x] != -1:
                team = (l_tokens[len(l_tokens)-1-y][x]+ 1)%2
                add_token(None, x)
            

def save():
    global l_tokens

    with open("save", "w") as file:
        file.write(str(l_tokens))

def load():
    global l_tokens

    with open("save", "r") as file:
        l_tokens = eval(file.readline())

    display_l_tokens(l_tokens)


radius = 75
BORDER = 20
WITDH,HEIGHT = 7*radius + (BORDER*2), 6*radius + (BORDER*2)

d_tokens,l_tokens_obj,l_x_moves = {i:0 for i in range(7)}, [], []
l_tokens = create_grid_list()
winning_team = "white"

team = random.randint(0,1)
team_color = ["red", "yellow"]

root = tk.Tk()

canvas = tk.Canvas(root,bg="blue", width=WITDH, height=HEIGHT)
b_undo = tk.Button(root,text="Undo", command=lambda:undo(canvas))
b_reset = tk.Button(root, text="Reset",command=lambda:reset(canvas))
b_save = tk.Button(root, text="Save",command=lambda:save())
b_load = tk.Button(root, text="Load",command=lambda:load())

canvas.grid(row=0, columnspan=5)
b_undo.grid(row=1, column=0)
b_reset.grid(row=1, column=1)
b_save.grid(row=1, column=2)
b_load.grid(row=1, column=3)

canvas.bind("<Button-1>", lambda event:add_token(event))

create_blanks()

root.mainloop()
