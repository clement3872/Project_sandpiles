###################################
# Groupe MI TD4
# DESFONTAINES Alexia
# MURAT Feyzanur
# FATNASSI Matéo
# MARCHAL Clément
# https://github.com/clement3872/Project_sandpiles.git
###################################


# importation des lib
import tkinter as tk
import random
from matplotlib.pyplot import text

from pyparsing import col


# Listes principales avec toutes les piles de sablese (complétés plus tard)
L_SANDPILES = []
WIDTH_TERRAIN = 3 # possible de modifier/générer aléatoirement
SIZE_SANDPILE = 35 # Nombre de pixels pour les carrés des piles de sables dans le canvas


# Vérifie si l'état du sable 
def stability_test(l):
    count = 0
    for y in l:
        for x in y:
            if x >3: count +=1

    return count >= 1

def create_table(l_sandpiles, width_terrain=3):
    l_sandpiles=[
        ["","#","#","#",""],
        ["#","#"],
        ["#","#"],
        ["#","#"],
        ["","#","#","#",""]
    ]
    # Créer une liste qui contient toutes les cases
    for y in range(1,len(l_sandpiles)-1):
        for x in range(width_terrain):
            l_sandpiles[y].insert(1,random.randint(0,3))
    
    return l_sandpiles


def create_sandpile_object(canvas=None, coords=(0,0), text_=""):
    # coords = (x,y)
    global SIZE_SANDPILE
    if canvas is not None:
        return canvas.create_rectangle(
            SIZE_SANDPILE*coords[0],
            SIZE_SANDPILE*coords[1],
            SIZE_SANDPILE*coords[0]+SIZE_SANDPILE,
            SIZE_SANDPILE*coords[1]+SIZE_SANDPILE,
            text=text_
            )
    
    else: return 0


def create_sandpiles_list(l_canvas):
    global L_SANDPILES
    
    for y in range(len(L_SANDPILES)):
        l_canvas.append([])
        for x in range(len(L_SANDPILES[y])):
            pass 
    


def main():
    global L_SANDPILES, WIDTH_TERRAIN

    root = tk.Tk()

    # Creation de frames (+ les afficher avec grid)
    f_buttons = tk.Frame(root)
    f_canvas = tk.Frame(root)
    f_buttons.grid(row=0, column=0)
    f_canvas.grid(row=0, column=1)

    #Création des buttons (+ les afficher, avec pack)
    b_generate_terrain = tk.Button(
        f_buttons, text="Generate terrain"
        )
    b_add_sand = tk.Button(f_buttons, text="Add sand")
    b_generate_terrain.pack()
    b_add_sand.pack()

    # Création d'un Canvas
    can = tk.Canvas(f_canvas, width=35*len(L_SANDPILES[0]), height=35*len(L_SANDPILES) )
    can.pack()

    l_canvas = []
    # création des piles de sables pour le canvas (ajoutées à une liste)
    
    

    root.mainloop()

#Juste afficher dans la console, pour tester


if __name__ == "__main__":

    L_SANDPILES = create_table(L_SANDPILES)

    def display_list(l):
        for el in l:
            print(el)
    display_list(L_SANDPILES)
    main()