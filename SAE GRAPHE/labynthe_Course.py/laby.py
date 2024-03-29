# -*- coding: utf-8 -*-
'''
:Titre : SAE
:Date : 03/2023
:Outils : plateau.py (module de classe d'un plateau (ou grille) avec affichage dans terminal)
          filepile.py (module de classes File et Pile)
'''

from random import randint, choice
from plateau import *
from filepile import *


def initialisation(largeur:int, hauteur: int)-> dict:
    '''La fonction renvoie un dictionnaire contenant chaque case du labyrinthe (clés)
et la liste de leur cases voisines (valeurs) initialement vide.
Une case est définie comme un tuple de ses coordonnées sur le labyrinthe.'''
    dico_graphe = {}

    for x in range(largeur):
        for y in range(hauteur):
            dico_graphe[(x,y)] = []   # déclaration d'une clé (x, y) avec pour valeur []

    return dico_graphe


def sur_bordure(case: tuple, dimensions: tuple)-> bool:
    '''La fonction précise si la case est sur la bordure du labyrinthe.'''
    x, y = case
    lim_x, lim_y = dimensions

    return (x == 0 or x == lim_x or y == 0 or y == lim_y)



def voisine_possible(case: tuple, dico: dict, contraintes: tuple)-> bool:
    '''La fonction précise si la case peut être définie comme une case voisine,
en tenant compte de sa position dans le labyrinthe et du nombre de cases voisines
q'uelle possède déjà.'''
    limite = 3    # nombre maximal de cases voisines 

    if sur_bordure(case, contraintes):   # si la case est sur le bord
        limite = 2                           # la limite diminue
    
    limite = limite - len(dico[case])    # la limite diminue en fonction du nombre actuel de voisines
    
    return limite > 1                    # si la limite est supérieur à 1


def voisines_possibles(case: tuple, dico: dict, taille: tuple)-> list:
    '''La fonction renvoie la liste des cases voisines qu'il est possible de déclarer
    à la case définie dans le dictionnaire.'''
    liste2 = []
    x, y = case

    if x != 0 and voisine_possible((x-1, y), dico, taille):             # case de gauche
        liste2.append((x-1, y))
    
    if x != taille[0]-1 and voisine_possible((x+1, y), dico, taille):   # case de droite
        liste2.append((x+1, y))
    
    if y != 0 and voisine_possible((x, y-1), dico, taille):             # case de dessus
        liste2.append((x, y-1))
    
    if y != taille[1]-1 and voisine_possible((x, y+1), dico, taille):   # case de dessous
        liste2.append((x, y+1))
    
    return liste2

def labyrinthe(largeur: int, hauteur: int)-> dict:
    '''La fonction renvoie un dictionnaire constitués contenant chaque case du labyrinthe (clé)
    et la liste de leur cases voisines définies aléatoirement (valeur).
    Une case est définie comme un tuple de ses coordonnées sur le labyrinthe.'''

    dico_laby = initialisation(largeur, hauteur)    # création du dictionnaire initial des cases
    pile = Pile(largeur * hauteur)                  # création d'une pile stockant les chemins à explorer
    pile.empiler([(0,0)])                           # empilement du premier chemin :
                                                       # chemin partant de la case (0, 0)
    while not pile.est_vide():

        chemin_actuel = pile.depiler()              # dépilement d'un chemin
        case_actuelle = chemin_actuel[-1]           # dernière case du chemin
        
        possibilites = voisines_possibles(case_actuelle,        # cases permettant de prolonger le chemin
                                          dico_laby,
                                          (largeur, hauteur))
        limite = len(possibilites)                              # nombre de cases possibles

    for y in range(2):
        for i in range(12):
            dico_laby[(1+(y*2), 1+i)].append((1+(y*2), 2+i)) 
            dico_laby[(1+(y*2), 2+i)].append((1+(y*2), 1+i))

    for y in range(3):
        for i in range(10):
            dico_laby[(1+i, 1+(y*5))].append((2+i, 1+(y*5)))
            dico_laby[(2+i, 1+(y*5))].append((1+i, 1+(y*5)))
    
    for i in range(12):
        dico_laby[(0+i, 13)].append((1+i, 13))
        dico_laby[(1+i, 13)].append((0+i, 13))

    for i in range(12):
        dico_laby[(11, 1+i)].append((11, 2+i)) 
        dico_laby[(11, 2+i)].append((11, 1+i))

    for y in range(3):
        for i in range(10):
            dico_laby[(5+(y*2), 1+i)].append((5+(y*2), 2+i)) 
            dico_laby[(5+(y*2), 2+i)].append((5+(y*2), 1+i))

    for y in range(3):
        for i in range(2):
            dico_laby[(1+i, 4+(y*2))].append((2+i, 4+(y*2)))
            dico_laby[(2+i, 4+(y*2))].append((1+i, 4+(y*2)))

    dico_laby[(0, 12)].append((1, 12))
    dico_laby[(1, 12)].append((0, 12))

    dico_laby[(0, 12)].append((0, 13))
    dico_laby[(0, 13)].append((0, 12))

    dico_laby[(0, 13)].append((1, 13))
    dico_laby[(1, 13)].append((0, 13))

    dico_laby[(0, 13)].append((1, 13))
    dico_laby[(1, 13)].append((0, 13))

    dico_laby[(0, 13)].append((1, 13))
    dico_laby[(1, 13)].append((0, 13))

    dico_laby[(0, 7)].append((1, 7))
    dico_laby[(1, 7)].append((0, 7))

    for i in range(2):
        dico_laby[(11, 6+(i*5))].append((12, 6+(i*5)))
        dico_laby[(12, 6+(i*5))].append((11, 6+(i*5)))

    for y in range(2):
        for i in range(2):
            dico_laby[(3+i+(y*6), 2)].append((4+i+(y*6), 2))
            dico_laby[(4+i+(y*6), 2)].append((3+i+(y*6), 2))
        for i in range(1):
            dico_laby[(4+(y*6), 1)].append((4+(y*6), 2))
            dico_laby[(4+(y*6), 2)].append((4+(y*6), 1))

    return dico_laby






def deplacement(arrivéL: int, arrivél: int)-> str:
    dico_laby = labyrinthe(13, 14)
    depart = (0, 12)
    print(depart)







    
    


def affichage_laby(largeur: int, hauteur: int):
    '''La fonction affiche un labyrinthe correspondant aux dimensions largeur x hauteur,
généré de façon aléatoire.'''
    graphe = labyrinthe(largeur, hauteur)  # création du dictionnaire du graphe modélisant le labyrinthe
    laby = Grille(largeur, hauteur)        # création d'une grille
    laby.construireBordure()               # avec une bordure
    laby.construireAvecGraphe(graphe)      # création des murs sur la grille, en suivant le graphe
    print(laby)


## Programme principal
if __name__ == '__main__':
    affichage_laby(13,14)