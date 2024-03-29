from functools import partial
from tkinter import E
import numpy as np 
n = 11



def initialisation_damier():
    damier = np.empty([n,n], dtype=np.object_)
    for i in range(0,n-1):              
        for j in range(0,n-1):
            if (j%2 == 0 and i%2==0) or (j%2==1 and i%2==1):        #condition si j/i sont pair ou si i/j sont impairs 
                damier[i,j]  = "  " 
            elif i<4 : 
                damier[i,j] = "PN"
            elif i>=6 :
                damier[i,j] = "PB" 
            else :
                damier[i,j] = "  "

    #lettrage sur la ligne 0
    for j in range(0,n-1):
            damier[10,j]=str(j)+" "
    damier[10,0] = "0 "
    damier[0,10] = "X "
    damier[n-1,n-1]="  "
    
    # lettrage sur la colonne 0
    for i in range(0,n-1):
        damier[i,10]=chr(i+65)+" "
    
    damier[5,7]="PB"
    damier[6,7]="  "
    
    damier[4,6]="PN"
    damier[3,6]="  "
    
    damier[4,8]="PN"
    
    damier[6,6]="PN"
    
    damier[6,8]="PN"
    
    return damier
        
def verification_position(damier, case_a_obtenir):
    #case à obtenir vérifie quelle case on voudrait avoir sur cet emplacement "PB" "PN" ou "  "
    continuer=False
    while not continuer:
        case_dep_ligne="L"
        while 'A'>case_dep_ligne or case_dep_ligne>'J':
            case_dep_ligne=input("Donner sa ligne : ")
            print(case_dep_ligne)
        case_dep_col='X'
        while not(case_dep_col>'0' and case_dep_col<'X'):
            case_dep_col=input("Donner sa colonne : ")
        #vérifier que depart dans damier
        num_col=int(case_dep_col)
        num_lig=(ord(case_dep_ligne)-65)
        if damier[num_lig,num_col]==case_a_obtenir:#est_blanc=True
            continuer=True
        else:
            print("erreur sur le placement, recommencer")
    return num_lig,num_col
                    
def deplacement_pion(damier,est_blanc):
    if est_blanc==False:
        type_pion="PB"
        type_pion_ennemie="PN"
        coul=-1
    else:
        type_pion="PN"
        type_pion_ennemie="PB"
        coul=1
    #demander la case de départ
    c_est_bon=False
    while c_est_bon ==False:
        print("Quelle est le pion que vous voulez déplacer?")
        lig_d,col_d=verification_position(damier, type_pion) 
        posibilité=[5]
        while not posibilité==[]:
            posibilité=verifaction_prise(damier,lig_d,col_d,coul,type_pion,type_pion_ennemie)
            if not posibilité==[]:
                damier,posibilité=prise(damier,coul,lig_d,col_d,type_pion,posibilité)
                c_est_bon=True
                posibilité=[]
            if posibilité==[] and c_est_bon==False:
                print("où voulez-vous placer votre pion?")
                lig_a,col_a=verification_position(damier, "  ")
                if ((col_a==col_d -1) or (col_a==col_d+1)) and (lig_a==lig_d+coul):
                    c_est_bon=True
                    damier[lig_a,col_a]=type_pion 
                    damier[lig_d,col_d]="  "
                else:
                    print("Il y a une erreur dans votre déplacement, recommencez ")
    return damier
    

#Prise des pions

def verifaction_prise(damier,num_lig,num_col,coul,type_pion,type_pion_ennemie):
    posibilité_pris=[]
    ligne_arrivé=num_lig
    colonne_arrivé=num_col
    
    verificaction_case_haut_droite=(int(ligne_arrivé)+(1*coul),int(colonne_arrivé)+1)
    verificaction_case_haut_gauche=(int(ligne_arrivé)+(1*coul),int(colonne_arrivé)-1)
    verificaction_case_bas_droite=(int(ligne_arrivé)-(1*coul),int(colonne_arrivé)+1)
    verificaction_case_bas_gauche=(int(ligne_arrivé)-(1*coul),int(colonne_arrivé)-1)
    
    if 0<=int(ligne_arrivé)+(1*coul)<=9 and 0<=int(colonne_arrivé)+1<=9:
        verificaction=damier[verificaction_case_haut_droite]
        if type_pion_ennemie==verificaction:
            posibilité_pris.append(1)
    
    if 0<=int(ligne_arrivé)+(1*coul)<=9 and 0<=int(colonne_arrivé)-1<=9:
        verificaction=damier[verificaction_case_haut_gauche]
        if type_pion_ennemie==verificaction:
            posibilité_pris.append(2)
    
    if 0<=int(ligne_arrivé)-(1*coul)<=9 and 0<=int(colonne_arrivé)+1<=9:
        verificaction=damier[verificaction_case_bas_droite]
        if type_pion_ennemie==verificaction:
            posibilité_pris.append(3)

    if 0<=int(ligne_arrivé)-(1*coul)<=9 and 0<=int(colonne_arrivé)-1<=9:
        verificaction=damier[verificaction_case_bas_gauche]
        if type_pion_ennemie==verificaction:
            posibilité_pris.append(4)
    return posibilité_pris
    
#on donne les coordonnées du point a bouger 
def prise(damier,coul,lig_d,col_d,type_pion,posibilité):
    case_dep_ligne=lig_d
    case_dep_col=col_d
    prise_fait=False
    choix_valide=False
    choix_joeur=0
    #on vérifie la diagonale
    while prise_fait==False and not posibilité==[]:
        if not posibilité==[]:
            print("prise obligatoire trouvé")
            choix_face=input("Donner sa ligne : ")
            choix_face=(ord(choix_face)-65)
            choix_cote=input("Donner sa colonne : ")
            pion_choisit=int(choix_face),int(choix_cote)

            if choix_face==case_dep_ligne-1 and int(choix_cote)==int(case_dep_col-1):
                if damier[pion_choisit]=='PN':
                    choix_valide=True
                    choix_joeur=1
            else:
                if choix_face==case_dep_ligne-1 and int(choix_cote)==int(case_dep_col+1):
                    if damier[pion_choisit]=='PN':
                        choix_valide=True
                        choix_joeur=2
                else:
                    if choix_face==case_dep_ligne+1 and int(choix_cote)==int(case_dep_col+1):
                        if damier[pion_choisit]=='PN':
                            choix_valide=True
                            choix_joeur=3
                    else:
                        if choix_face==case_dep_ligne+1 and int(choix_cote)==int(case_dep_col-1):
                            if damier[pion_choisit]=='PN':
                                choix_valide=True
                                choix_joeur=4

            print(choix_valide,choix_joeur)
            if choix_valide==True and choix_joeur==1:
                damier[case_dep_ligne+(2*coul),case_dep_col-2]=type_pion 
                damier[case_dep_ligne+(1*coul),case_dep_col-1]="  " 
                damier[case_dep_ligne,case_dep_col]="  " 
                prise_fait=True

            if choix_valide==True and choix_joeur==2:
                damier[case_dep_ligne+(2*coul),case_dep_col+2]=type_pion 
                damier[case_dep_ligne+(1*coul),case_dep_col+1]="  " 
                damier[case_dep_ligne,case_dep_col]="  "
                prise_fait=True

            if choix_valide==True and choix_joeur==3:
                damier[case_dep_ligne-(2*coul),case_dep_col+2]=type_pion 
                damier[case_dep_ligne-(1*coul),case_dep_col+1]="  " 
                damier[case_dep_ligne,case_dep_col]="  " 
                prise_fait=True

            if choix_valide==True and choix_joeur==4:
                damier[case_dep_ligne-(2*coul),case_dep_col-2]=type_pion 
                damier[case_dep_ligne-(1*coul),case_dep_col-1]="  " 
                damier[case_dep_ligne,case_dep_col]="  " 
                prise_fait=True
    return damier,posibilité
            
                  
if __name__ == '__main__':
    i=0
    damier  = initialisation_damier()
    while i<=10:
        print(damier)
        joue_avec_blanc=False
        damier=deplacement_pion(damier,joue_avec_blanc)
        print(damier)
        joue_avec_blanc=True
        damier=deplacement_pion(damier,joue_avec_blanc)
        print(damier)
        i=i+1