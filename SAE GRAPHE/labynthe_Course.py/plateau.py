# -*- coding: utf-8 -*-
'''
:Titre : Module de classe Case(), Grille()
:Auteur : L. Conoir
:Date : 05/2020
'''

class Case() :
    '''Classe définissant une case à partir de sa position : x, y.

Un objet, instance de cette classe, possède plusieurs méthodes :

    construireMur() : construit un mur de la case
    detruireMur() : détruit un mur de la case
    getContenu() : renvoie le contenu de la case
    setContenu() : affecte le contenu de la case
    getposition() : renvoie la position de la case
    getMurs() : renvoie la liste des murs de la case'''
    
    
    def __init__(self, x, y):
        '''Méthode dédiée, constructeur de la classe'''
        
        self.__position = x, y
        self.__est_vide = True
        self.__contenu = None
        self.__murs = ['N', 'S', 'E', 'W']


    def construireMur(self, mur):
        '''Méthode publique, construit un mur de l'objet.'''
        if mur not in self.__murs :
            self.__murs.append(mur)


    def detruireMur(self, mur):
        '''Méthode publique, détruit un mur de l'objet.'''
        if mur in self.__murs :
            self.__murs.remove(mur)


    def setContenu(self, cakechose):
        '''Méthode publique, affecte le contenu de l'objet.'''
        self.__contenu = cakechose


    def getContenu(self):
        '''Méthode publique, renvoie le contenu de l'objet.'''
        return self.__contenu


    def getPosition(self, position):
        '''Méthode publique, renvoie la position de l'objet : tuple (x, y)'''
        return self.__position


    def getMurs(self):
        '''Méthode publique, renvoie la liste des murs.'''
        return self.__murs


    def __setMurs(self):
        '''Méthode privée, construit les 4 murs de l'objet.'''
        self.__murs = ['N', 'S', 'W', 'E']



##########################################################################################       
class Grille() :
    '''Classe définissant une grille à partir de ses dimensions
           largeur : nombre de cases en largeur
           hauteur : nombre de cases en longueur

Un objet, instance de cette classe, possède plusieurs méthodes :

    construireBordure() : construit les murs sur le contour de la grille
    detruireBordure() : détruit les murs sur le contour de la grille
    afficheGrilleVide() : affiche la grille (sans contenu) avec tous les murs
    affichePlateau() : affiche le plateau (avec contenu et murs éventuels des cases)'''
    
    def __init__(self, largeur, hauteur) :
        self.__largeur = largeur
        self.__hauteur = hauteur
        self.__cases = self.__creationGrille()
        
        
    def __creationGrille(self) :
        liste_cases = []
        
        for y in range(self.__hauteur) :
            
            ligne_cases = []
        
            for x in range(self.__largeur) :
                nouvelle_case = Case(x, y)
                ligne_cases.append(nouvelle_case)
            
            liste_cases.append(ligne_cases)
        
        return liste_cases

    def construireAvecGraphe(self, graphe):
        '''Méthode publique, définit les murs à partir d'un graphe.'''
        for case, voisines in graphe.items():
            x1, y1 = case

            for case_voisine in voisines:
                
                x2, y2 = case_voisine

                if y1 == y2 :
                    if x1 < x2 :
                        self.__cases[y1][x1].detruireMur('E')
                    else: 
                        self.__cases[y1][x1].detruireMur('W')
                else :
                    if y1 < y2 :
                        self.__cases[y1][x1].detruireMur('S')
                    else: 
                        self.__cases[y1][x1].detruireMur('N')


    def construireBordure(self) :
        '''Méthode publique, définit une bordure extérieure de la grille.'''
        for colonne in range(self.__largeur) :
            self.__cases[0][colonne].construireMur('N')
            self.__cases[self.__hauteur - 1][colonne].construireMur('S')
        
        for ligne in range(self.__hauteur) :
            self.__cases[ligne][0].construireMur('W')
            self.__cases[ligne][self.__largeur - 1].construireMur('E')
    
    
    def detruireBordure(self) :
        '''Méthode publique, enlève une bordure extérieure de la grille.'''
        for colonne in range(self.__largeur) :
            self.__cases[0][colonne].detruireMur('N')
            self.__cases[self.__hauteur - 1][colonne].detruireMur('S')
        
        for ligne in range(self.__hauteur) :
            self.__cases[ligne][0].detruireMur('W')
            self.__cases[ligne][self.__largeur - 1].detruireMur('E')
    
    
    def afficheGrilleVide(self) :
        '''Méthode publique, affiche la grille vide avec tous les murs.'''                                
        for ligne in range(self.__hauteur) :
            print('+---' * self.__largeur + '+')
            print('|   ' * self.__largeur + '|')
            
        print('+---' * self.__largeur + '+\n')


    def __str__(self) :
        '''Méthode dédiée, affiche la grille avec son contenu et les murs existants.'''
        affichage = ''
        
        for ligne in range(self.__hauteur) :
        
            affiche_ligne1 = ''
            affiche_ligne2 = ''
        
            for colonne in range(self.__largeur) :
            
                liste_murs = self.__cases[ligne][colonne].getMurs()
                
                if 'N' in liste_murs :
                    affiche_ligne1 = affiche_ligne1 + '+---'
                else :
                    affiche_ligne1 = affiche_ligne1 + '+   '
                
                contenu = self.__cases[ligne][colonne].getContenu()
                if contenu != None :
                    contenu = str(contenu)[0]
                else :
                    contenu = ' '
                
                if 'W' in liste_murs :
                    affiche_ligne2 = affiche_ligne2 + '| ' + contenu + ' '
                else :
                    affiche_ligne2 = affiche_ligne2 + '  ' + contenu + ' '

            if 'E' in liste_murs :
                affiche_ligne2 = affiche_ligne2 + '|'
            
            affichage = affichage + affiche_ligne1 + '+\n' + affiche_ligne2 + '\n'
            
        affiche_ligne1 = ''
            
        for colonne in range(self.__largeur) :
            
            liste_murs = self.__cases[self.__hauteur - 1][colonne].getMurs()
                
            if 'S' in liste_murs :
                affiche_ligne1 = affiche_ligne1 + '+---'
            else :
                affiche_ligne1 = affiche_ligne1 + '+   '
                
        affichage = affichage + affiche_ligne1 + '+\n'
        
        return affichage
        

##########################################################################################
if __name__ == '__main__' :
    laby = Grille(8,8)
    laby.construireBordure()
    graphe = {(0,7): {(0,6)}, (0,6): {(0,7), (0,5)}, (0,5): {(0,6), (0,4)},
              (0,4): {(0,5), (0,3)}, (0,3): {(1,3), (0,4)},
              (1,3): {(0,3), (1,4)}, (1,4): {(1,3), (2,4)},
              (2,4): {(1,4), (2,3), (2,5)}, (2,3): {(2,4), (2,2)},
              (2,5): {(2,4)}, (2,2): {(2,3), (1,2)}, (1,2): {(0,2), (1,2)},
              (0,2): {(1,2)}, (2,5): {(2,4), (1,5)}, (1,5): {(1,6), (2,5)},
              (1,6): {(1,7), (1,5)}, (1,7): {(2,7), (1,6)}, 
              (2,7): {(3,7), (1,7)}, (3,7): {(1,7), (4,7)},
              (4,7): {(3,7)},}
    laby.construireAvecGraphe(graphe)
    print(laby)