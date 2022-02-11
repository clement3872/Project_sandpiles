###################################
# Groupe MI TD4
# DESFONTAINES Alexia
# MURAT Feyzanur
# FATNASSI Matéo
# MARCHAL Clément
# https://github.com/clement3872/Project_sandpiles.git
###################################


# importation des libraries
import tkinter as tk
import random


# Listes principales avec toutes les piles de sablese (complétés plus tard)
L_SANDPILES = []
WIDTH_TERRAIN = 3 # possible de modifier/générer aléatoirement
SIZE_SANDPILE = 35 # Nombre de pixels pour les carrés des piles de sables dans le canvas

# Ce ne sont pas des constantes, mais des listes très importantes pour le programme
L_CANVAS_RECTANGLES = []
L_CANVAS_TEXTS = []

# Vérifie si l'état du sable 
def stability_test(l):
    count = 0
    for y in l:
        for x in y:
            if x >3: count +=1

    return count >= 1

def generate_table(width_terrain=3):

    #Création de la structure de la liste
    l_sandpiles=[
        [""]+["#"]*width_terrain+[""],
        [""]+["#"]*width_terrain+[""]
    ]
    for _ in range(width_terrain):
        l_sandpiles.insert(1,["#","#"])
    
    # Création d'une liste qui contient toutes les cases
    for y in range(1,len(l_sandpiles)-1):
        for x in range(width_terrain):
            l_sandpiles[y].insert(1,random.randint(0,6))
    
    return l_sandpiles


def create_sandpile_object(canvas=None, coords=(0,0)):
    # coords = (x,y)
    # Création des carrés dans le canvas (+ les ajouter à une liste)
    global SIZE_SANDPILE
    if canvas is not None:
        return canvas.create_rectangle(
            SIZE_SANDPILE*coords[0],
            SIZE_SANDPILE*coords[1],
            SIZE_SANDPILE*coords[0]+SIZE_SANDPILE,
            SIZE_SANDPILE*coords[1]+SIZE_SANDPILE
            )
    
    else: return 0

def create_sandpile_texts_object(canvas=None, coords=(0,0), text_=""):
    # coords = (x,y)
    # Création des zones de texte dans le canvas (+ les ajouter à une liste)
    global SIZE_SANDPILE
    if canvas is not None:
        return canvas.create_text(
            SIZE_SANDPILE*coords[0] + SIZE_SANDPILE/2,
            SIZE_SANDPILE*coords[1] + SIZE_SANDPILE/2,
            text=text_,
            anchor="center"
            )
    
    else: return 0


def create_sandpiles_list(canvas):
    global L_SANDPILES, L_CANVAS_RECTANGLES, L_CANVAS_TEXTS
    L_CANVAS_TEXTS = []
    L_CANVAS_RECTANGLES = []
    
    # Création et ajouts des rectangles et du text du canvas
    for y in range(len(L_SANDPILES)):
        L_CANVAS_TEXTS.append([])
        L_CANVAS_RECTANGLES.append([])
        for x in range(len(L_SANDPILES[y])):
            L_CANVAS_TEXTS.append(create_sandpile_texts_object(canvas, (x,y),L_SANDPILES[y][x]))
            L_CANVAS_RECTANGLES.append(create_sandpile_object(canvas, (x,y) ))
    

    # Juste au cas où...
    L_CANVAS_RECTANGLES.append(canvas)
    L_CANVAS_TEXTS.append(canvas)
    

def delete_sandpiles(): # TO DO
    global L_SANDPILES, L_CANVAS_RECTANGLES, L_CANVAS_TEXTS, WIDTH_TERRAIN

    # Il faut tout remettre à 0
    L_SANDPILES = generate_table(WIDTH_TERRAIN)


def main():
    global L_SANDPILES, WIDTH_TERRAIN, L_SANDPILES, SIZE_SANDPILE

    # Premier remplissage de la liste pour la génération du terrain
    L_SANDPILES = generate_table(WIDTH_TERRAIN)

    root = tk.Tk()

    # Creation de frames (+ les afficher avec grid)
    f_buttons = tk.Frame(root)
    f_canvas = tk.Frame(root)
    f_buttons.grid(row=0, column=0) # ajouter : sticky="n" si le terrain est trop grand
    f_canvas.grid(row=0, column=1)

    #Création des buttons (+ les afficher, avec pack)
    b_generate_terrain = tk.Button(f_buttons, text="Generate terrain",command=lambda:create_sandpiles_list(can))
    b_add_sand = tk.Button(f_buttons, text="Add sand")
    
    # Création d'un Canvas
    can = tk.Canvas(f_canvas, width=SIZE_SANDPILE*len(L_SANDPILES[0]), height=SIZE_SANDPILE*len(L_SANDPILES) )
    
    b_generate_terrain.pack()
    b_add_sand.pack()
    can.pack(padx=50, pady=50)  
    

    root.mainloop()

#Juste afficher dans la console, pour tester


if __name__ == "__main__":
    main()