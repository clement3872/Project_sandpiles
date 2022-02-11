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

# Listes principales avec toutes les piles de sablese (complétés plus tard)
L_SANDPILES = [
    ["","#","#","#",""],
    ["#","#"],
    ["#","#"],
    ["#","#"],
    ["","#","#","#",""]
]

WIDTH_TERRAIN = 3

#est-ce qu'il faut faire ça ?
def stability_test(l):
    count = 0
    for y in l:
        for x in y:
            if x >3: count +=1

    return count >= 5

def create_table(l_sandpiles, width_terrain=3):
    # Créer une liste qui contient toutes les cases
    for y in range(1,len(l_sandpiles)-1):
        for x in range(width_terrain):
            l_sandpiles[y].insert(1,random.randint(0,3))
    
    return l_sandpiles






L_SANDPILES = create_table(L_SANDPILES)

#Juste afficher dans la console, pour tester
def display_list(l):
    for el in l:
        print(el)
display_list(L_SANDPILES)