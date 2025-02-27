# programme développer par Dupuis Brian, Payen Alexis, Mazuier Eve et Lhote Florian

# se programme utilise les informations d'une base SQL pour fonctionné il affiche le nombre de kg de CO2 produit
# en fonction de la distance, pour plus d'information je vous recommandes de regardé le pdf fournie avec le programme

################################################ importation ###########################################################

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout,QPushButton, QHBoxLayout, QLabel, QPushButton
import matplotlib
matplotlib.use('QtAgg')
from PyQt6 import QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import psycopg2

############################## connection a la base SQL #########################""

conn = psycopg2.connect(
    host="localhost",
    database=input("nom de la database : "),
    port="5432",
    user=input("votre nom d'utilisateur : "),
    password=input("votre mot de passe : ")
)

######################################### récupération des valeurs de la base de donnée #################################################

def aerop(y):   # cette fonctionne permet d'accéder aux multiples dictionnaires contenant le co2 produit par les avions en KG (CO2_avions) puis les distantces parcourus en km (distance_avions)
    
######################################### partie 1 : les 10 plus grand aéroports ######################################################

   
    # en fonction du y on aura accés aux dictionnaires désirés 
    if y==0:                # il permet de mettre à zéro le programme à son lancement
        distance_avions=([0])
        CO2_avions=([0])

    elif y==1:              # son fonctionnement est le même pour la totalité des if de cette fonction
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_1 ;")     # on éxécute la commandes SQL qui nous donne la totalité de la distance
        distance_avions = cursor.fetchall()                 # on stock les donnés dans une variable de type dictionnaire

        cursor.execute("SELECT emissions_co2/100 FROM aero_1 ;") # on éxécute la commandes SQL qui nous donne la totalité du CO2 on divise par 100 pour transformé le gramme de Co2 en kilogramme de CO2
        CO2_avions = cursor.fetchall()                      # on stock les données dans une variable de type dictionnaire

    elif y==2:    
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_2 ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_2 ;")
        CO2_avions = cursor.fetchall()

    elif y==3:    
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_3 ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_3 ;")
        CO2_avions = cursor.fetchall()

    elif y==4:    
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_4 ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_4 ;")
        CO2_avions = cursor.fetchall()

    elif y==5:    
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_5 ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_5 ;")
        CO2_avions = cursor.fetchall()

    elif y==6:    
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_6 ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_6 ;")
        CO2_avions = cursor.fetchall()

    elif y==7:    
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_7 ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_7 ;")
        CO2_avions = cursor.fetchall()
    
    elif y==8:    
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_8 ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_8 ;")
        CO2_avions = cursor.fetchall()

    elif y==9:    
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_9 ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_9 ;")
        CO2_avions = cursor.fetchall()

    elif y==10:            # on prend tout les valeurs des 9 aéroports pour les stockés en 2 variables
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_1 ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_1 ;")
        CO2_avions = cursor.fetchall()
 
        cursor.execute("SELECT distance FROM aero_2 ;")
        distance_avions_1 = cursor.fetchall()

        distance_avions = distance_avions + distance_avions_1       # on ajoute les valeurs de distance_avions_1 à distance_avions et on recommence pour les 9 aéroports

        cursor.execute("SELECT emissions_co2/100 FROM aero_2 ;")
        CO2_avions_2 = cursor.fetchall()

        CO2_avions = CO2_avions + CO2_avions_2

        cursor.execute("SELECT distance FROM aero_3 ;")
        distance_avions_1 = cursor.fetchall()

        distance_avions = distance_avions + distance_avions_1

        cursor.execute("SELECT emissions_co2/100 FROM aero_3 ;")
        CO2_avions_2 = cursor.fetchall()

        CO2_avions = CO2_avions + CO2_avions_2

        cursor.execute("SELECT distance FROM aero_4 ;")
        distance_avions_1 = cursor.fetchall()

        distance_avions = distance_avions + distance_avions_1

        cursor.execute("SELECT emissions_co2/100 FROM aero_4 ;")
        CO2_avions_2 = cursor.fetchall()

        CO2_avions = CO2_avions + CO2_avions_2

        cursor.execute("SELECT distance FROM aero_5 ;")
        distance_avions_1 = cursor.fetchall()

        distance_avions = distance_avions + distance_avions_1

        cursor.execute("SELECT emissions_co2/100 FROM aero_5 ;")
        CO2_avions_2 = cursor.fetchall()

        CO2_avions = CO2_avions + CO2_avions_2

        cursor.execute("SELECT distance FROM aero_6 ;")
        distance_avions_1 = cursor.fetchall()

        distance_avions = distance_avions + distance_avions_1

        cursor.execute("SELECT emissions_co2/100 FROM aero_6 ;")
        CO2_avions_2 = cursor.fetchall()

        CO2_avions = CO2_avions + CO2_avions_2

        cursor.execute("SELECT distance FROM aero_7 ;")
        distance_avions_1 = cursor.fetchall()

        distance_avions = distance_avions + distance_avions_1

        cursor.execute("SELECT emissions_co2/100 FROM aero_7 ;")
        CO2_avions_2 = cursor.fetchall()

        CO2_avions = CO2_avions + CO2_avions_2
    
        cursor.execute("SELECT distance FROM aero_8 ;")
        distance_avions_1 = cursor.fetchall()

        distance_avions = distance_avions + distance_avions_1

        cursor.execute("SELECT emissions_co2/100 FROM aero_8 ;")
        CO2_avions_2 = cursor.fetchall()

        CO2_avions = CO2_avions + CO2_avions_2

        cursor.execute("SELECT distance FROM aero_9 ;")
        distance_avions_1 = cursor.fetchall()

        distance_avions = distance_avions + distance_avions_1       # C02_avions posséde maintenant la totalité des valeurs de distance en kiloMètre des 9 aéroports

        cursor.execute("SELECT emissions_co2/100 FROM aero_9 ;")
        CO2_avions_2 = cursor.fetchall()

        CO2_avions = CO2_avions + CO2_avions_2                      # C02_avions posséde maintenant la totalité des valeurs de CO2 en KiloGramme des 9 aéroports 

######################################### partie 2 : aéroports français ######################################################

    elif y==11:
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_fr where aero_arr like 'ATL' ;")      #c'est la même que les commandes d'avant a la différence qu'on prend les valeurs d'un aéroports spécifiquement
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_fr where aero_arr like 'ATL' ;")
        CO2_avions = cursor.fetchall()

    elif y==12:    
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL

        cursor.execute("SELECT distance FROM aero_fr where aero_arr like 'PEK' ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_fr where aero_arr like 'PEK' ;")
        CO2_avions = cursor.fetchall()

    elif y==13:    
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_fr where aero_arr like 'DXB' ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_fr where aero_arr like 'DXB' ;")
        CO2_avions = cursor.fetchall()

    elif y==14:    
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_fr where aero_arr like 'LAX' ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_fr where aero_arr like 'LAX' ;")
        CO2_avions = cursor.fetchall()

    elif y==15:    
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_fr where aero_arr like 'HND' ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_fr where aero_arr like 'HND' ;")
        CO2_avions = cursor.fetchall()

    elif y==16:    
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_fr where aero_arr like 'LHR' ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_fr where aero_arr like 'LHR' ;")
        CO2_avions = cursor.fetchall()

    elif y==17:    
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_fr where aero_arr like 'FRA' ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_fr where aero_arr like 'FRA' ;")
        CO2_avions = cursor.fetchall()

    elif y==18:    
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_fr where aero_arr like 'CDG' ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_fr where aero_arr like 'CDG' ;")
        CO2_avions = cursor.fetchall()

    elif y==19:    
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_fr where aero_arr like 'ISL' ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_fr where aero_arr like 'ISL' ;")
        CO2_avions = cursor.fetchall()

    elif y==20:            # en fonction du y on aura accés au dictionnaire désirés 
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_fr where aero_arr like 'ORY' ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_fr where aero_arr like 'ORY' ;")
        CO2_avions = cursor.fetchall()

    elif y==21:
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_fr where aero_arr like 'LYS' ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_fr where aero_arr like 'LYS' ;")
        CO2_avions = cursor.fetchall()

    elif y==22:    
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL

        cursor.execute("SELECT distance FROM aero_fr where aero_arr like 'MRS' ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_fr where aero_arr like 'MRS' ;")
        CO2_avions = cursor.fetchall()

    elif y==23:    
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_fr where aero_arr like 'TLS' ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_fr where aero_arr like 'TLS' ;")
        CO2_avions = cursor.fetchall()

    elif y==24:    
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_fr where aero_arr like 'BSL' ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_fr where aero_arr like 'BSL' ;")
        CO2_avions = cursor.fetchall()

    elif y==25:    
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_fr where aero_arr like 'BOD' ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_fr where aero_arr like 'BOD' ;")
        CO2_avions = cursor.fetchall()

    elif y==26:    
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_fr where aero_arr like 'NTE' ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_fr where aero_arr like 'NTE' ;")
        CO2_avions = cursor.fetchall()

    elif y==27:    
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_fr where aero_arr like 'BVA' ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_fr where aero_arr like 'BVA' ;")
        CO2_avions = cursor.fetchall()

    elif y==28:    
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_fr where aero_arr like 'PTP' ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_fr where aero_arr like 'PTP' ;")
        CO2_avions = cursor.fetchall()

    elif y==29:    
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_fr where aero_arr like 'RUN' ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_fr where aero_arr like 'RUN' ;")
        CO2_avions = cursor.fetchall()

    elif y==30:            # en fonction du y on aura accés au dictionnaire désirés 
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_fr where aero_arr like 'LIL' ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_fr where aero_arr like 'LIL' ;")
        CO2_avions = cursor.fetchall()

    elif y==31:
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_fr where aero_arr like 'FDF' ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_fr where aero_arr like 'FDF' ;")
        CO2_avions = cursor.fetchall()

    elif y==32:    
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_fr where aero_arr like 'MPL' ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_fr where aero_arr like 'MPL' ;")
        CO2_avions = cursor.fetchall()

    elif y==33:    
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_fr where aero_arr like 'AJA' ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_fr where aero_arr like 'AJA' ;")
        CO2_avions = cursor.fetchall()

    elif y==34:    
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_fr where aero_arr like 'BIA' ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_fr where aero_arr like 'BIA' ;")
        CO2_avions = cursor.fetchall()

    elif y==35:    
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_fr where aero_arr like 'SXB' ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_fr where aero_arr like 'SXB' ;")
        CO2_avions = cursor.fetchall()
        
    elif y==36:    
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_fr where aero_arr like 'BES' ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_fr where aero_arr like 'BES' ;")
        CO2_avions = cursor.fetchall()
    
    elif y==37:    
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_fr where aero_arr like 'BIQ' ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_fr where aero_arr like 'BIQ' ;")
        CO2_avions = cursor.fetchall()
        
    elif y==38:    
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_fr where aero_arr like 'RNS' ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_fr where aero_arr like 'RNS' ;")
        CO2_avions = cursor.fetchall()

    elif y==39:    
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_fr where aero_arr like 'FSC' ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_fr where aero_arr like 'FSC' ;")
        CO2_avions = cursor.fetchall()

    elif y==40:            # en fonction du y on aura accés au dictionaire désirés 
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_fr where aero_arr like 'PUF' ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_fr where aero_arr like 'PUF' ;")
        CO2_avions = cursor.fetchall()

    elif y==41:
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_fr where aero_arr like 'NOU' ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_fr where aero_arr like 'NOU' ;")
        CO2_avions = cursor.fetchall()

    elif y==42:   
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_fr where aero_arr like 'CAY' ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_fr where aero_arr like 'CAY' ;")
        CO2_avions = cursor.fetchall()

    elif y==43:    
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_fr where aero_arr like 'TLN' ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_fr where aero_arr like 'TLN' ;")
        CO2_avions = cursor.fetchall()

    elif y==44:    
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_fr where aero_arr like 'LDE' ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_fr where aero_arr like 'LDE' ;")
        CO2_avions = cursor.fetchall()

    elif y==45:    
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_fr where aero_arr like 'GEA' ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_fr where aero_arr like 'GEA' ;")
        CO2_avions = cursor.fetchall()

    elif y==46:    
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_fr where aero_arr like 'PGF' ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_fr where aero_arr like 'PGF' ;")
        CO2_avions = cursor.fetchall()

    elif y==47:    
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_fr where aero_arr like 'CFE' ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_fr where aero_arr like 'CFE' ;")
        CO2_avions = cursor.fetchall()

    elif y==48:    
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_fr where aero_arr like 'DZA' ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_fr where aero_arr like 'DZA' ;")
        CO2_avions = cursor.fetchall()

    elif y==49:    
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_fr where aero_arr like 'CCF' ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_fr where aero_arr like 'CCF' ;")
        CO2_avions = cursor.fetchall()

    elif y==50:            # en fonction du y on aura accés au dictionaire désirés 
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_fr where aero_arr like 'CLY' ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_fr where aero_arr like 'CLY' ;")
        CO2_avions = cursor.fetchall()

    elif y==51:
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_fr where aero_arr like 'BOB' ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_fr where aero_arr like 'BOB' ;")
        CO2_avions = cursor.fetchall()

    elif y==52:    
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_fr where aero_arr like 'CFR' ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_fr where aero_arr like 'CFR' ;")
        CO2_avions = cursor.fetchall()

    elif y==53:    
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_fr where aero_arr like 'LIG' ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_fr where aero_arr like 'LIG' ;")
        CO2_avions = cursor.fetchall()

    elif y==54:    
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_fr where aero_arr like 'EGC' ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_fr where aero_arr like 'EGC' ;")
        CO2_avions = cursor.fetchall()

    elif y==55:    
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_fr where aero_arr like 'BZR' ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_fr where aero_arr like 'BZR' ;")
        CO2_avions = cursor.fetchall()

    elif y==56:    
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_fr where aero_arr like 'ETZ' ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_fr where aero_arr like 'ETZ' ;")
        CO2_avions = cursor.fetchall()

    elif y==57:    
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_fr where aero_arr like 'RFP' ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_fr where aero_arr like 'RFP' ;")
        CO2_avions = cursor.fetchall()

    elif y==58:    
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_fr where aero_arr like 'LRH' ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_fr where aero_arr like 'LRH' ;")
        CO2_avions = cursor.fetchall()

    elif y==59:    
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_fr where aero_arr like 'FNI' ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_fr where aero_arr like 'FNI' ;")
        CO2_avions = cursor.fetchall()    
        
    elif y==60:            # en fonction du y on aura accés au dictionaire désirés 
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_fr where aero_arr like 'TUF' ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_fr where aero_arr like 'TUF' ;")
        CO2_avions = cursor.fetchall()

    elif y==61:
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_fr where aero_arr like 'LIF' ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_fr where aero_arr like 'LIF' ;")
        CO2_avions = cursor.fetchall()

    elif y==62:    
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_fr where aero_arr like 'SBH' ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_fr where aero_arr like 'SBH' ;")
        CO2_avions = cursor.fetchall()

    elif y==63:    
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_fr where aero_arr like 'HUH' ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_fr where aero_arr like 'HUH' ;")
        CO2_avions = cursor.fetchall()

    elif y==64:    
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_fr where aero_arr like 'DOL' ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_fr where aero_arr like 'DOL' ;")
        CO2_avions = cursor.fetchall()

    elif y==65:    
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_fr where aero_arr like 'PIS' ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_fr where aero_arr like 'PIS' ;")
        CO2_avions = cursor.fetchall()

    elif y==66:    
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_fr where aero_arr like 'IPL' ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_fr where aero_arr like 'IPL' ;")
        CO2_avions = cursor.fetchall()

    elif y==67:    
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_fr where aero_arr like 'DLE' ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_fr where aero_arr like 'DLE' ;")
        CO2_avions = cursor.fetchall()

    elif y==68:    
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_fr where aero_arr like 'LRT' ;")
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_fr where aero_arr like 'LRT' ;")
        CO2_avions = cursor.fetchall()

    elif y==69:    
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_fr ;")            # on prend la totalité des valeurs de distances de aero_fr
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_fr ;")   # on prend la totalité des valeurs de CO2 de aero_fr
        CO2_avions = cursor.fetchall()

    elif y==70:    
        cursor = conn.cursor()  # on prépare à lancé des commandes SQL
        cursor.execute("SELECT distance FROM aero_fr ;")            # on prend la totalité des valeurs de distances de aero_fr
        distance_avions = cursor.fetchall()

        cursor.execute("SELECT emissions_co2/100 FROM aero_fr ;")   # on prend la totalité des valeurs de CO2 de aero_fr
        CO2_avions = cursor.fetchall()

        cursor.execute("SELECT distance FROM aero_1 ;")
        distance_avions_1 = cursor.fetchall()

        distance_avions = distance_avions + distance_avions_1 

        cursor.execute("SELECT emissions_co2/100 FROM aero_1 ;")
        CO2_avions_2 = cursor.fetchall()

        CO2_avions = CO2_avions + CO2_avions_2
 
        cursor.execute("SELECT distance FROM aero_2 ;")
        distance_avions_1 = cursor.fetchall()

        distance_avions = distance_avions + distance_avions_1       # on ajoute les valeurs de distance_avions_1 à distance_avions et on recommence pour les 9 aéroports

        cursor.execute("SELECT emissions_co2/100 FROM aero_2 ;")
        CO2_avions_2 = cursor.fetchall()

        CO2_avions = CO2_avions + CO2_avions_2

        cursor.execute("SELECT distance FROM aero_3 ;")
        distance_avions_1 = cursor.fetchall()

        distance_avions = distance_avions + distance_avions_1

        cursor.execute("SELECT emissions_co2/100 FROM aero_3 ;")
        CO2_avions_2 = cursor.fetchall()

        CO2_avions = CO2_avions + CO2_avions_2

        cursor.execute("SELECT distance FROM aero_4 ;")
        distance_avions_1 = cursor.fetchall()

        distance_avions = distance_avions + distance_avions_1

        cursor.execute("SELECT emissions_co2/100 FROM aero_4 ;")
        CO2_avions_2 = cursor.fetchall()

        CO2_avions = CO2_avions + CO2_avions_2

        cursor.execute("SELECT distance FROM aero_5 ;")
        distance_avions_1 = cursor.fetchall()

        distance_avions = distance_avions + distance_avions_1

        cursor.execute("SELECT emissions_co2/100 FROM aero_5 ;")
        CO2_avions_2 = cursor.fetchall()

        CO2_avions = CO2_avions + CO2_avions_2

        cursor.execute("SELECT distance FROM aero_6 ;")
        distance_avions_1 = cursor.fetchall()

        distance_avions = distance_avions + distance_avions_1

        cursor.execute("SELECT emissions_co2/100 FROM aero_6 ;")
        CO2_avions_2 = cursor.fetchall()

        CO2_avions = CO2_avions + CO2_avions_2

        cursor.execute("SELECT distance FROM aero_7 ;")
        distance_avions_1 = cursor.fetchall()

        distance_avions = distance_avions + distance_avions_1

        cursor.execute("SELECT emissions_co2/100 FROM aero_7 ;")
        CO2_avions_2 = cursor.fetchall()

        CO2_avions = CO2_avions + CO2_avions_2
    
        cursor.execute("SELECT distance FROM aero_8 ;")
        distance_avions_1 = cursor.fetchall()

        distance_avions = distance_avions + distance_avions_1

        cursor.execute("SELECT emissions_co2/100 FROM aero_8 ;")
        CO2_avions_2 = cursor.fetchall()

        CO2_avions = CO2_avions + CO2_avions_2

        cursor.execute("SELECT distance FROM aero_9 ;")
        distance_avions_1 = cursor.fetchall()

        distance_avions = distance_avions + distance_avions_1       # C02_avions posséde maintenant la totalité des valeurs de distance en kiloMetre des 9 aéroports

        cursor.execute("SELECT emissions_co2/100 FROM aero_9 ;")
        CO2_avions_2 = cursor.fetchall()

        CO2_avions = CO2_avions + CO2_avions_2                      # C02_avions posséde maintenant la totalité des valeurs de CO2 en KiloGramme des 9 aéroports

#######################################

    if distance_avions==[] or CO2_avions==[]:       # si l'une des 2 varaible et vide alors on met les deux varaible à 0
        distance_avions=[(0.0,)]
        CO2_avions=[(0.0,)]

    return distance_avions,CO2_avions # on return les dictionnaires

################################################ calcule des moyennes et de la sommes de tout les produits ##############################

def distance_co2(self,x):   # cette fonction permet de faire les calcul pour le total et les moyennes de co2 et de distance
    p0, p1=aerop(x) # on appele les dictionnaires voulus
    i = 0
    self.text1 = 0        # on met à zéro les 4 textes
    self.text2 = 0
    self.text3 = 0
    self.text4 = 0
    while i<=len(p1)-1:                # on va calculé la moyenne et le total de tout les valeur de l'aéroports
        p2=p0[i]    # on récuper les valeurs de p0[i] pour qu'elle soit utilisable 
        p3=p1[i]    #on recuper les valeurs de p1[i] pour qu'elle soit utilisable

        self.text1 = self.text1+p2[0]   # on addictionne les valeurs de text1 avec les valeur de p2
        self.text2 = self.text2+p3[0]   # on addictionne les valeurs de text2 avec les valeur de p3
        i = i+1
    self.text3 = self.text1 // len(p1)  # une fois additioner on calcule la moyenne de CO2 qu'on stock dans text3
    self.text4 = self.text2 // len(p1)  # uneune fois additioner on calcule le moyenne de la distance qu'on stock dans text4 

######################################################### création du graphique ##############################################

class MplCanvas(FigureCanvasQTAgg):                        # permet de crée le graphique
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, x, *args, **kwargs, ):               # permet de crée la courbe du graphique
        super(MainWindow, self).__init__(*args, **kwargs)
        sc = MplCanvas(self, width=5, height=4, dpi=100)

        p0, p1=aerop(x)             # on appelle la fonction aerop pour qu'ils nous donne les valeurs de CO2 et de distance
        sc.axes.plot(p0, p1)        # on donnes les 2 valeurs pour qu'ils crée le graphique
        self.setCentralWidget(sc)   # on met au centre le widget

################################################ programme principale ######################################

class VueAnnuaire(QWidget):
 
    def __init__(self):
        super().__init__()

####################### definiion des varaibles #####################

        self.toutselect="tout selectionner"
        self.toutretire="tout retirer"


        self.text1 = 0.0
        self.text2 = 0.0
        self.text3 = 0.0
        self.text4 = 0.0

############################ création des Layouts #####################

        # la création des layouts vont de gauche à droite

        self.v1layout = QVBoxLayout()       # création du layout tout à gauche il contiendra les widget "france", "autres" et "selectionnée tout"

        self.v2_2_2layout = QVBoxLayout()   # création d'un layout contenant du texte

        self.v2layout = QVBoxLayout()       # création d'un layout contenants des QPushButton des 10 plus grand aéroports

        self.h1_1layout = QHBoxLayout()     # création d'un layout qui va contenir les 3 layouts précedents

        self.v2_2_3layout = QVBoxLayout()   # création d'un layout contenant du texte

        self.v2_1layout = QVBoxLayout()     # création d'un layout contenants des QPushButton des aéroports français (58 QPushButton) 
                                            #mais aussi tout en haut le bouton "sélectionné tout" et tout en bas "suivant qui permetra de changer de page"

        self.h1layout = QHBoxLayout()       # création d'un layout les 2 layouts precendent

        self.v3layout = QVBoxLayout()       # création d'un layout contenant du text

        self.h2layout = QHBoxLayout()       # création du layout principale

        self.h3layout = QHBoxLayout()       # création d'un layout contenant le graphique

        self.setLayout(self.h2layout)       # on définit h2layout en layout principale

        #interface V1
        self.France = QPushButton('France') # création d'un QPushButton
        self.Autre = QPushButton('Autre')   # création d'un QPushButton
        self.tout = QPushButton('tout selectionné') # création d'un QPushButton

        #interface V2
        self.aéroports1 = QPushButton('aéroports1')   # création d'un QPushButton
        self.aéroports2 = QPushButton('aéroports2')   # création d'un QPushButton
        self.aéroports3 = QPushButton('aéroports3')   # création d'un QPushButton
        self.aéroports4 = QPushButton('aéroports4')   # création d'un QPushButton
        self.aéroports5 = QPushButton('aéroports5')   # création d'un QPushButton
        self.aéroports6 = QPushButton('aéroports6')   # création d'un QPushButton
        self.aéroports7 = QPushButton('aéroports7')   # création d'un QPushButton
        self.aéroports8 = QPushButton('aéroports8')   # création d'un QPushButton
        self.aéroports9 = QPushButton('aéroports9')   # création d'un QPushButton
        self.aéroports11 = QPushButton('tout selectionné')   # création d'un QPushButton

        self.Hartsfield_Jackson = QPushButton('Hartsfield_Jackson') # création d'un QPushButton
        self.Pékin_Capitale = QPushButton('Pékin_Capitale') # création d'un QPushButton
        self.Dubaï = QPushButton('Dubaï')   # création d'un QPushButton
        self.Los_Angeles = QPushButton('Los_Angeles')   # création d'un QPushButton
        self.Tokyo_Haneda = QPushButton('Tokyo_Haneda') # création d'un QPushButton
        self.Londres_Heathrow = QPushButton('Londres_Heathrow')   # création d'un QPushButton
        self.Francfort_sur_le_Main = QPushButton('Francfort_sur_le_Main')   # création d'un QPushButton
        self.Paris_Charles_de_Gaulle = QPushButton('Paris_Charles_de_Gaulle')   # création d'un QPushButton
        self.Atatürk = QPushButton('Atatürk')   # création d'un QPushButton
        self.Paris_Orly = QPushButton('Aéroport de Paris_Orly')   # création d'un QPushButton
        self.Lyon_Saint_Exupéry = QPushButton('Aéroport de Lyon_Saint_Exupéry')   # création d'un QPushButton
        self.Marseille_Provence = QPushButton('Aéroport de Marseille Provence')   # création d'un QPushButton
        self.Toulouse_Blagnac = QPushButton('Aéroport de Toulouse_Blagnac')   # création d'un QPushButton
        self.Bâle_Mulhouse_Fribourg = QPushButton('Aéroport de Bâle_Mulhouse_Fribourg')   # création d'un QPushButton
        self.Bordeaux_Mérignac = QPushButton('Aéroport de Bordeaux_Mérignac')   # création d'un QPushButton
        self.Nantes_Atlantique = QPushButton('Aéroport de Nantes Atlantique')   # création d'un QPushButton
        self.Beauvais_Tillé = QPushButton('Aéroport de Beauvais_Tillé')   # création d'un QPushButton
        self.Pointe_à_Pitre_Le_Raizet = QPushButton('Aéroport de Pointe_à_Pitre Le Raizet')   # création d'un QPushButton
        self.La_Réunion_Roland_Garros = QPushButton('Aéroport de La Réunion Roland Garros')   # création d'un QPushButton
        self.Lille_Lesquin = QPushButton('Aéroport de Lille_Lesquin')   # création d'un QPushButton
        self.Fort_de_France_Le_Lamentin = QPushButton('Aéroport de Fort_de_France Le Lamentin')   # création d'un QPushButton
        self.Montpellier_Méditerranée = QPushButton('Aéroport de Montpellier_Méditerranée')   # création d'un QPushButton
        self.Ajaccio_Napoléon_Bonaparte = QPushButton('Aéroport d_Ajaccio Napoléon Bonaparte')   # création d'un QPushButton
        self.Bastia_Poretta  = QPushButton('Aéroport de Bastia Poretta ')   # création d'un QPushButton
        self.Strasbourg_Entzheim = QPushButton('Aéroport de Strasbourg Entzheim')   # création d'un QPushButton
        self.Brest_Bretagne = QPushButton('Aéroport de Brest Bretagne')   # création d'un QPushButton
        self.Biarritz_Pays_Basque = QPushButton('Aéroport de Biarritz_Pays Basque')   # création d'un QPushButton
        self.Rennes_Bretagne = QPushButton('Aéroport de Rennes Bretagne')   # création d'un QPushButton
        self.Figari_Sud_Corse = QPushButton('Aéroport de Figari Sud_Corse')   # création d'un QPushButton
        self.Pau_Pyrénées = QPushButton('Aéroport de Pau Pyrénées')   # création d'un QPushButton
        self.Nouméa_La_Tontouta = QPushButton('Aéroport de Nouméa_La Tontouta')   # création d'un QPushButton
        self.Cayenne_Félix_Eboué  = QPushButton('Aéroport de Cayenne Félix Eboué ')   # création d'un QPushButton
        self.Toulon_Hyères = QPushButton('Aéroport de Toulon_Hyères')   # création d'un QPushButton
        self.Tarbes_Lourdes_Pyrénées = QPushButton('Aéroport de Tarbes_Lourdes_Pyrénées')   # création d'un QPushButton
        self.Nouméa_Magenta = QPushButton('Aéroport de Nouméa_Magenta')   # création d'un QPushButton
        self.Perpignan_Rivesaltes = QPushButton('Aéroport de Perpignan_Rivesaltes')   # création d'un QPushButton
        self.Clermont_Ferrand_Auvergne = QPushButton('Aéroport de Clermont_Ferrand Auvergne')   # création d'un QPushButton
        self.Dzaoudzi_Pamandzi = QPushButton('Aéroport de Dzaoudzi_Pamandzi')   # création d'un QPushButton
        self.Carcassonne_Salvaza = QPushButton('Aéroport de Carcassonne Salvaza')   # création d'un QPushButton
        self.Calvi_Sainte_Catherine  = QPushButton('Aéroport de Calvi_Sainte_Catherine ')   # création d'un QPushButton
        self.Bora_Bora = QPushButton('Aéroport de Bora Bora')   # création d'un QPushButton
        self.Caen_Carpiquet  = QPushButton('Aéroport de Caen Carpiquet ')   # création d'un QPushButton
        self.Lim = QPushButton('Aéroport de Lim')   # création d'un QPushButton
        self.Bergerac_Dordogne_Périgord = QPushButton('Aéroport de Bergerac Dordogne Périgord')   # création d'un QPushButton
        self.Béziers_Cap_d_Agde = QPushButton('Aéroport de Béziers Cap d_Agde')   # création d'un QPushButton
        self.Metz_Nancy_Lorraine  = QPushButton('Aéroport de Metz_Nancy_Lorraine ')   # création d'un QPushButton
        self.Raiatea= QPushButton('Aéroport de Raiatea')   # création d'un QPushButton
        self.La_Rochelle_Île_de_Ré = QPushButton('Aéroport de La Rochelle_Île de Ré')   # création d'un QPushButton
        self.Nîmes_Alès_Camargue_Cévennes = QPushButton('Aéroport de Nîmes_Alès_Camargue_Cévennes')   # création d'un QPushButton
        self.Tours_Val_de_Loire = QPushButton('Aéroport de Tours Val de Loire')   # création d'un QPushButton
        self.Lifou  = QPushButton('Aéroport de Lifou ')   # création d'un QPushButton
        self.Gustaf_III  = QPushButton('Aéroport de Gustaf III ')   # création d'un QPushButton
        self.Huahine  = QPushButton('Aéroport de Huahine ')   # création d'un QPushButton
        self.Deauville_Normandie = QPushButton('Aéroport de Deauville_Normandie')   # création d'un QPushButton
        self.Poitiers_Biard = QPushButton('Aéroport de Poitiers_Biard ')   # création d'un QPushButton
        self.Montluçon_Guéret  = QPushButton('Aéroport de Montluçon - Guéret ')   # création d'un QPushButton
        self.Dole_Jura  = QPushButton('Aéroport de Dole-Jura  ')   # création d'un QPushButton
        self.Lorient_Bretagne_Sud  = QPushButton('Aéroport de Lorient Bretagne Sud ')   # création d'un QPushButton
        self.Montluçon_Guéret  = QPushButton('Aéroport de Montluçon - Guéret ')   # création d'un QPushButton
        self.Dole_Jura  = QPushButton('Aéroport de Dole-Jura  ')   # création d'un QPushButton
        self.Lorient_Bretagne_Sud  = QPushButton('Aéroport de Lorient Bretagne Sud ')   # création d'un QPushButton
        self.toutselectionne = QPushButton('tout selectionné')   # création d'un QPushButton
        self.suivant = QPushButton('suivant')   # création d'un QPushButton
        self.page=1         # cette varaible permet de savoir la page dans la qu'elle on se trouve
        self.autre_page=1   # cette varaible permet de savoir si on doit caché oui ou non les QPushButton des aéroportss étrangers
        self.france_page=1  # cette varaible permet de savoir si on doit caché oui ou non les QPushButton des aéroportss français'

        #interface 3

        self.ligne1 = QLabel("quantité de CO2 émit en total en kilogramme : " + str(self.text1))            #on crée un QLabel
        self.ligne2 = QLabel("distance parcouru en total : " + str(self.text2))                             #on crée un QLabel
        self.ligne3 = QLabel("quantité de CO2 émit en moyenne par vol en kilogramme : " + str(self.text3))  #on crée un QLabel
        self.ligne4 = QLabel("distance en moyenne parcouru en moyenne : " + str(self.text4))                #on crée un QLabel
        self.ligne5 = QLabel("les 10 plus gros aéroports du monde :")                                       #on crée un QLabel
        self.ligne6 = QLabel("la totalité des aéroportss français:")                                        #on crée un QLabel

        self.init()     # on appele la fonction init pour initialisé l'interface

        self.setGeometry(50, 125, 1500, 650)        # on définit la taille de la fenêtre
        self.setWindowTitle('Interface')            # on donne un nom à la fenêtre

        self.show()                                 # on affiche la fenetre

        self.France.clicked.connect(self.changement_france)   # si on appuie sur le bouton on appele la fonctione changement_france
        self.Autre.clicked.connect(self.changement_autres)   # si on appuie sur le bouton on appele la fonctione changement_autres
        self.tout.clicked.connect(self.total)   # si on appuie sur le bouton on appele la fonctione total
        self.suivant.clicked.connect(self.change_page)   # si on appuie sur le bouton on appele la fonctione change_page
        self.aéroports1.clicked.connect(self.change_aéroports1)   # si on appuie sur le bouton on appele la fonctione change_aéroports1
        self.aéroports2.clicked.connect(self.change_aéroports2)   # si on appuie sur le bouton on appele la fonctione change_aéroports2
        self.aéroports3.clicked.connect(self.change_aéroports3)   # si on appuie sur le bouton on appele la fonctione change_aéroports3
        self.aéroports4.clicked.connect(self.change_aéroports4)   # si on appuie sur le bouton on appele la fonctione change_aéroports4
        self.aéroports5.clicked.connect(self.change_aéroports5)   # si on appuie sur le bouton on appele la fonctione change_aéroports5
        self.aéroports6.clicked.connect(self.change_aéroports6)   # si on appuie sur le bouton on appele la fonctione change_aéroports6
        self.aéroports7.clicked.connect(self.change_aéroports7)   # si on appuie sur le bouton on appele la fonctione change_aéroports7
        self.aéroports8.clicked.connect(self.change_aéroports8)   # si on appuie sur le bouton on appele la fonctione change_aéroports8
        self.aéroports9.clicked.connect(self.change_aéroports9)   # si on appuie sur le bouton on appele la fonctione change_aéroports9
        self.aéroports11.clicked.connect(self.change_aéroports10)   # si on appuie sur le bouton on appele la fonctione change_aéroports10

        self.Hartsfield_Jackson.clicked.connect(self.change_aéroports11)   # si on appuie sur le bouton on appele la fonctione change_aéroports11
        self.Pékin_Capitale.clicked.connect(self.change_aéroports12)   # si on appuie sur le bouton on appele la fonctione change_aéroports12
        self.Dubaï.clicked.connect(self.change_aéroports13)   # si on appuie sur le bouton on appele la fonctione change_aéroports13
        self.Los_Angeles.clicked.connect(self.change_aéroports14)   # si on appuie sur le bouton on appele la fonctione change_aéroports14
        self.Tokyo_Haneda.clicked.connect(self.change_aéroports15)   # si on appuie sur le bouton on appele la fonctione change_aéroports15
        self.Londres_Heathrow.clicked.connect(self.change_aéroports16)   # si on appuie sur le bouton on appele la fonctione change_aéroports16
        self.Francfort_sur_le_Main.clicked.connect(self.change_aéroports17)   # si on appuie sur le bouton on appele la fonctione change_aéroports17
        self.Paris_Charles_de_Gaulle.clicked.connect(self.change_aéroports18)   # si on appuie sur le bouton on appele la fonctione change_aéroports18
        self.Atatürk.clicked.connect(self.change_aéroports19)   # si on appuie sur le bouton on appele la fonctione change_aéroports19
        self.Paris_Orly.clicked.connect(self.change_aéroports20)   # si on appuie sur le bouton on appele la fonctione change_aéroports20
        self.Lyon_Saint_Exupéry.clicked.connect(self.change_aéroports21)   # si on appuie sur le bouton on appele la fonctione change_aéroports21
        self.Marseille_Provence.clicked.connect(self.change_aéroports22)   # si on appuie sur le bouton on appele la fonctione change_aéroports22
        self.Toulouse_Blagnac.clicked.connect(self.change_aéroports23)   # si on appuie sur le bouton on appele la fonctione change_aéroports23
        self.Bâle_Mulhouse_Fribourg.clicked.connect(self.change_aéroports24)   # si on appuie sur le bouton on appele la fonctione change_aéroports24
        self.Bordeaux_Mérignac.clicked.connect(self.change_aéroports25)   # si on appuie sur le bouton on appele la fonctione change_aéroports25
        self.Nantes_Atlantique.clicked.connect(self.change_aéroports26)   # si on appuie sur le bouton on appele la fonctione change_aéroports26
        self.Beauvais_Tillé.clicked.connect(self.change_aéroports27)   # si on appuie sur le bouton on appele la fonctione change_aéroports27
        self.Pointe_à_Pitre_Le_Raizet.clicked.connect(self.change_aéroports28)   # si on appuie sur le bouton on appele la fonctione change_aéroports28
        self.La_Réunion_Roland_Garros.clicked.connect(self.change_aéroports29)   # si on appuie sur le bouton on appele la fonctione change_aéroports29
        self.Lille_Lesquin.clicked.connect(self.change_aéroports30)   # si on appuie sur le bouton on appele la fonctione change_aéroports30
        self.Fort_de_France_Le_Lamentin.clicked.connect(self.change_aéroports31)   # si on appuie sur le bouton on appele la fonctione change_aéroports31
        self.Montpellier_Méditerranée.clicked.connect(self.change_aéroports32)   # si on appuie sur le bouton on appele la fonctione change_aéroports32
        self.Ajaccio_Napoléon_Bonaparte.clicked.connect(self.change_aéroports33)   # si on appuie sur le bouton on appele la fonctione change_aéroports33
        self.Bastia_Poretta.clicked.connect(self.change_aéroports34)   # si on appuie sur le bouton on appele la fonctione change_aéroports34
        self.Strasbourg_Entzheim.clicked.connect(self.change_aéroports35)   # si on appuie sur le bouton on appele la fonctione change_aéroports35
        self.Brest_Bretagne.clicked.connect(self.change_aéroports36)   # si on appuie sur le bouton on appele la fonctione change_aéroports36
        self.Biarritz_Pays_Basque.clicked.connect(self.change_aéroports37)   # si on appuie sur le bouton on appele la fonctione change_aéroports37
        self.Rennes_Bretagne.clicked.connect(self.change_aéroports38)   # si on appuie sur le bouton on appele la fonctione change_aéroports38
        self.Figari_Sud_Corse.clicked.connect(self.change_aéroports39)   # si on appuie sur le bouton on appele la fonctione change_aéroports39
        self.Pau_Pyrénées.clicked.connect(self.change_aéroports40)   # si on appuie sur le bouton on appele la fonctione change_aéroports40
        self.Nouméa_La_Tontouta.clicked.connect(self.change_aéroports41)   # si on appuie sur le bouton on appele la fonctione change_aéroports41
        self.Cayenne_Félix_Eboué.clicked.connect(self.change_aéroports42)   # si on appuie sur le bouton on appele la fonctione change_aéroports42
        self.Toulon_Hyères.clicked.connect(self.change_aéroports43)   # si on appuie sur le bouton on appele la fonctione change_aéroports43
        self.Tarbes_Lourdes_Pyrénées.clicked.connect(self.change_aéroports44)   # si on appuie sur le bouton on appele la fonctione change_aéroports44
        self.Nouméa_Magenta.clicked.connect(self.change_aéroports45)   # si on appuie sur le bouton on appele la fonctione change_aéroports45
        self.Perpignan_Rivesaltes.clicked.connect(self.change_aéroports46)   # si on appuie sur le bouton on appele la fonctione change_aéroports46
        self.Clermont_Ferrand_Auvergne.clicked.connect(self.change_aéroports47)   # si on appuie sur le bouton on appele la fonctione change_aéroports47
        self.Dzaoudzi_Pamandzi.clicked.connect(self.change_aéroports48)   # si on appuie sur le bouton on appele la fonctione change_aéroports48
        self.Carcassonne_Salvaza.clicked.connect(self.change_aéroports49)   # si on appuie sur le bouton on appele la fonctione change_aéroports49
        self.Calvi_Sainte_Catherine.clicked.connect(self.change_aéroports50)   # si on appuie sur le bouton on appele la fonctione change_aéroports50
        self.Bora_Bora.clicked.connect(self.change_aéroports51)   # si on appuie sur le bouton on appele la fonctione change_aéroports51
        self.Caen_Carpiquet.clicked.connect(self.change_aéroports52)   # si on appuie sur le bouton on appele la fonctione change_aéroports52
        self.Lim.clicked.connect(self.change_aéroports53)   # si on appuie sur le bouton on appele la fonctione change_aéroports53
        self.Bergerac_Dordogne_Périgord.clicked.connect(self.change_aéroports54)   # si on appuie sur le bouton on appele la fonctione change_aéroports54
        self.Béziers_Cap_d_Agde.clicked.connect(self.change_aéroports55)   # si on appuie sur le bouton on appele la fonctione change_aéroports55
        self.Metz_Nancy_Lorraine.clicked.connect(self.change_aéroports56)   # si on appuie sur le bouton on appele la fonctione change_aéroports56
        self.Raiatea.clicked.connect(self.change_aéroports57)   # si on appuie sur le bouton on appele la fonctione change_aéroports57
        self.La_Rochelle_Île_de_Ré.clicked.connect(self.change_aéroports58)   # si on appuie sur le bouton on appele la fonctione change_aéroports58
        self.Nîmes_Alès_Camargue_Cévennes.clicked.connect(self.change_aéroports59)   # si on appuie sur le bouton on appele la fonctione change_aéroports59
        self.Tours_Val_de_Loire.clicked.connect(self.change_aéroports60)   # si on appuie sur le bouton on appele la fonctione change_aéroports60
        self.Lifou.clicked.connect(self.change_aéroports61)   # si on appuie sur le bouton on appele la fonctione change_aéroports61
        self.Gustaf_III.clicked.connect(self.change_aéroports62)   # si on appuie sur le bouton on appele la fonctione change_aéroports62
        self.Huahine.clicked.connect(self.change_aéroports63)   # si on appuie sur le bouton on appele la fonctione change_aéroports63
        self.Deauville_Normandie.clicked.connect(self.change_aéroports64)   # si on appuie sur le bouton on appele la fonctione change_aéroports64
        self.Poitiers_Biard.clicked.connect(self.change_aéroports65)   # si on appuie sur le bouton on appele la fonctione change_aéroports65
        self.Montluçon_Guéret.clicked.connect(self.change_aéroports66)   # si on appuie sur le bouton on appele la fonctione change_aéroports66
        self.Dole_Jura.clicked.connect(self.change_aéroports67)   # si on appuie sur le bouton on appele la fonctione change_aéroports67
        self.Lorient_Bretagne_Sud.clicked.connect(self.change_aéroports68)   # si on appuie sur le bouton on appele la fonctione change_aéroports68
        self.toutselectionne.clicked.connect(self.change_aéroports69)   # si on appuie sur le bouton on appele la fonctione change_aéroports69

    def total(self) :               # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(70)

    def change_aéroports1(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(1)
    
    def change_aéroports2(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(2)
    
    def change_aéroports3(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(3)
    
    def change_aéroports4(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(4)
    
    def change_aéroports5(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(5)
    
    def change_aéroports6(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(6)
    
    def change_aéroports7(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(7)
    
    def change_aéroports8(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(8)
    
    def change_aéroports9(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(9)
    
    def change_aéroports10(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(10)

    def change_aéroports11(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(11)
    
    def change_aéroports12(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(12)
    
    def change_aéroports13(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(13)
    
    def change_aéroports14(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(14)
    
    def change_aéroports15(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(15)
    
    def change_aéroports16(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(16)
    
    def change_aéroports17(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(17)
    
    def change_aéroports18(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(18)
    
    def change_aéroports19(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(19)
    
    def change_aéroports20(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(20)
    
    def change_aéroports21(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(21)
    
    def change_aéroports22(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(22)
    
    def change_aéroports23(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(23)
    
    def change_aéroports24(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(24)
    
    def change_aéroports25(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(25)
    
    def change_aéroports26(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(26)
    
    def change_aéroports27(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(27)
    
    def change_aéroports28(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(28)
    
    def change_aéroports29(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(29)
    
    def change_aéroports30(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(30)
    
    def change_aéroports31(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(31)
    
    def change_aéroports32(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(32)
    
    def change_aéroports33(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(33)
    
    def change_aéroports34(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(34)
    
    def change_aéroports35(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(35)
    
    def change_aéroports36(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(36)
    
    def change_aéroports37(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(37)
    
    def change_aéroports38(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(38)
    
    def change_aéroports39(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(39)
    
    def change_aéroports40(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(40)

    def change_aéroports41(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(41)
    
    def change_aéroports42(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(42)
    
    def change_aéroports43(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(43)
    
    def change_aéroports44(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(44)
    
    def change_aéroports45(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(45)
    
    def change_aéroports46(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(46)
    
    def change_aéroports47(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(47)
    
    def change_aéroports48(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(48)
    
    def change_aéroports49(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(49)
    
    def change_aéroports50(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(50)

    def change_aéroports51(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(51)
    
    def change_aéroports52(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(52)
    
    def change_aéroports53(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(53)
    
    def change_aéroports54(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(54)
    
    def change_aéroports55(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(55)
    
    def change_aéroports56(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(56)
    
    def change_aéroports57(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(57)
    
    def change_aéroports58(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(58)
    
    def change_aéroports59(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(59)
    
    def change_aéroports60(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(60)
    
    def change_aéroports61(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(61)
    
    def change_aéroports62(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(62)
    
    def change_aéroports63(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(63)
    
    def change_aéroports64(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(64)
    
    def change_aéroports65(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(65)
    
    def change_aéroports66(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(66)
    
    def change_aéroports67(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(67)
    
    def change_aéroports68(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(68)
    
    def change_aéroports69(self) :    # cette fonction appele la fonction change_aéroports mais en donnant la valeur du dictionnaire voulu
        self.change_aéroports(69)
                

    def change_aéroports(self,k) :    # cette fonction sert a changer les valeurs du texte mais aussi changé le graphique
        
        self.v3layout.removeWidget(self.ligne1)     # on retire le widget ligne 1
        self.v3layout.removeWidget(self.ligne2)     # on retire le widget ligne 2
        self.v3layout.removeWidget(self.ligne3)     # on retire le widget ligne 3
        self.v3layout.removeWidget(self.ligne4)     # on retire le widget ligne 4

        distance_co2(self,k)                        # on appele la fonction distance_co2 pour qui va changé les valeurs de texte 1, 2, 3 et 4

        # on remet les widget ligne 1,2,3 et 4
        self.ligne1 = QLabel("quantité de CO2 émit en total en kilogramme : " + str(self.text1))
        self.ligne2 = QLabel("distance parcouru en total : " + str(self.text2))
        self.ligne3 = QLabel("quantité de CO2 émit en moyenne par vol en kilogramme : " + str(self.text3))
        self.ligne4 = QLabel("distance en moyenne parcouru en moyenne : " + str(self.text4))

        self.v3layout.addWidget(self.ligne1)
        self.v3layout.addWidget(self.ligne2)
        self.v3layout.addWidget(self.ligne3)
        self.v3layout.addWidget(self.ligne4)

        
        self.h3layout.removeWidget(self.w)  # on enlève le widget w qui est le widget du graphique

        
        self.w = MainWindow(k)  # on appele la fonction MainWindow pour qu'elle nous crée le nouveau graphique avec les nouvelles valeurs

        self.h3layout.addWidget(self.w) # on ajoute aux nouvelles valeurs le widget w



    def init(self):

        # on ajoute les widgets dans le v1layout

        self.v1layout.addWidget(self.France)
        self.v1layout.addWidget(self.Autre)
        self.v1layout.addWidget(self.tout)

        # on ajoute le layout : v1layout dans le layout : h1_1layout

        self.h1_1layout.addLayout(self.v1layout)

        # on ajoute les widget dans le v2_2_2layout

        self.v2_2_2layout.addWidget(self.ligne5)

        # on ajoute le layout : v2_2_2layout dans le layout : h1_1layout

        self.h1_1layout.addLayout(self.v2_2_2layout)

        # on ajoute les widget dans le v2layout

        self.v2layout.addWidget(self.aéroports1)
        self.v2layout.addWidget(self.aéroports2)
        self.v2layout.addWidget(self.aéroports3)
        self.v2layout.addWidget(self.aéroports4)
        self.v2layout.addWidget(self.aéroports5)
        self.v2layout.addWidget(self.aéroports6)
        self.v2layout.addWidget(self.aéroports7)
        self.v2layout.addWidget(self.aéroports8)
        self.v2layout.addWidget(self.aéroports9)
        self.v2layout.addWidget(self.aéroports11)

        # on ajoute le layout : v2layout dans le layout : h1_1layout

        self.h1_1layout.addLayout(self.v2layout)

        # on ajoute les widget dans le v2_2_3layout

        self.v2_2_3layout.addWidget(self.ligne6)

        # on ajoute le layout : v2_2_3layout dans le layout : h1_1layout

        self.h1_1layout.addLayout(self.v2_2_3layout)

        # on ajoute les widgets dans le v2_1layout
        
        self.v2_1layout.addWidget(self.toutselectionne)
        self.v2_1layout.addWidget(self.Hartsfield_Jackson)
        self.v2_1layout.addWidget(self.Pékin_Capitale)
        self.v2_1layout.addWidget(self.Dubaï)
        self.v2_1layout.addWidget(self.Los_Angeles)
        self.v2_1layout.addWidget(self.Tokyo_Haneda)
        self.v2_1layout.addWidget(self.Londres_Heathrow)
        self.v2_1layout.addWidget(self.Francfort_sur_le_Main)
        self.v2_1layout.addWidget(self.Paris_Charles_de_Gaulle)
        self.v2_1layout.addWidget(self.Atatürk)
        self.v2_1layout.addWidget(self.Paris_Orly)
        self.v2_1layout.addWidget(self.Lyon_Saint_Exupéry)
        self.v2_1layout.addWidget(self.Marseille_Provence)
        self.v2_1layout.addWidget(self.Toulouse_Blagnac)
        self.v2_1layout.addWidget(self.Bâle_Mulhouse_Fribourg)
        self.v2_1layout.addWidget(self.Bordeaux_Mérignac)
        self.v2_1layout.addWidget(self.Nantes_Atlantique)
        self.v2_1layout.addWidget(self.Beauvais_Tillé)
        self.v2_1layout.addWidget(self.Pointe_à_Pitre_Le_Raizet)

        self.v2_1layout.addWidget(self.La_Réunion_Roland_Garros)
        self.v2_1layout.addWidget(self.Lille_Lesquin)
        self.v2_1layout.addWidget(self.Fort_de_France_Le_Lamentin)
        self.v2_1layout.addWidget(self.Montpellier_Méditerranée)
        self.v2_1layout.addWidget(self.Ajaccio_Napoléon_Bonaparte)
        self.v2_1layout.addWidget(self.Bastia_Poretta)
        self.v2_1layout.addWidget(self.Strasbourg_Entzheim)
        self.v2_1layout.addWidget(self.Brest_Bretagne)
        self.v2_1layout.addWidget(self.Biarritz_Pays_Basque)
        self.v2_1layout.addWidget(self.Rennes_Bretagne)
        self.v2_1layout.addWidget(self.Figari_Sud_Corse)
        self.v2_1layout.addWidget(self.Pau_Pyrénées)
        self.v2_1layout.addWidget(self.Nouméa_La_Tontouta)
        self.v2_1layout.addWidget(self.Cayenne_Félix_Eboué)
        self.v2_1layout.addWidget(self.Toulon_Hyères)
        self.v2_1layout.addWidget(self.Tarbes_Lourdes_Pyrénées)
        self.v2_1layout.addWidget(self.Nouméa_Magenta)
        self.v2_1layout.addWidget(self.Perpignan_Rivesaltes)

        self.v2_1layout.addWidget(self.Clermont_Ferrand_Auvergne)
        self.v2_1layout.addWidget(self.Dzaoudzi_Pamandzi)
        self.v2_1layout.addWidget(self.Carcassonne_Salvaza)
        self.v2_1layout.addWidget(self.Calvi_Sainte_Catherine)
        self.v2_1layout.addWidget(self.Bora_Bora)
        self.v2_1layout.addWidget(self.Caen_Carpiquet)
        self.v2_1layout.addWidget(self.Lim)
        self.v2_1layout.addWidget(self.Bergerac_Dordogne_Périgord)
        self.v2_1layout.addWidget(self.Béziers_Cap_d_Agde)
        self.v2_1layout.addWidget(self.Metz_Nancy_Lorraine)
        self.v2_1layout.addWidget(self.Raiatea)
        self.v2_1layout.addWidget(self.La_Rochelle_Île_de_Ré)
        self.v2_1layout.addWidget(self.Nîmes_Alès_Camargue_Cévennes)
        self.v2_1layout.addWidget(self.Tours_Val_de_Loire)
        self.v2_1layout.addWidget(self.Lifou)
        self.v2_1layout.addWidget(self.Gustaf_III)
        self.v2_1layout.addWidget(self.Huahine)
        self.v2_1layout.addWidget(self.Deauville_Normandie)
        self.v2_1layout.addWidget(self.Poitiers_Biard)
        self.v2_1layout.addWidget(self.Montluçon_Guéret)
        self.v2_1layout.addWidget(self.Dole_Jura)
        self.v2_1layout.addWidget(self.Lorient_Bretagne_Sud)
        self.v2_1layout.addWidget(self.suivant)

        # on ajoute le layout : v2_1layout dans le layout : h1_1layout

        self.h1_1layout.addLayout(self.v2_1layout)

        # on ajoute le layout : h1_1layout dans le layout : h1layout

        self.h1layout.addLayout(self.h1_1layout)

        # on ajoute les widgets dans le v3layout

        self.v3layout.addWidget(self.ligne1)
        self.v3layout.addWidget(self.ligne2)
        self.v3layout.addWidget(self.ligne3)
        self.v3layout.addWidget(self.ligne4)

        # on ajoute le layout : h1layout dans le layout : h2layout

        self.h2layout.addLayout(self.h1layout)

        # on ajoute le layout : v3layout dans le layout : h2layout

        self.h2layout.addLayout(self.v3layout)

        # on crée une variable w qui contient graphique
        
        self.w = MainWindow(0)

        # on ajoute le graphique dans le h3layout

        self.h3layout.addWidget(self.w)

        # on ajoute le layout : h3layout dans le layout : h2layout

        self.h2layout.addLayout(self.h3layout)

        # on appelle la fonction changement_autres qui va caché les widgets et le texte des aéroports non français

        self.changement_autres()

        # on appelle la fonction changement_france qui va caché les widgets et le texte des aéroports français

        self.changement_france()


    def change_page(self) :     # sa permet de naviguée entre les différentes pages des aéroports français
        self.page=self.page+1
        if self.page==4:        # si page est à 4 alors on le passe à 1
            self.page=1
        if self.page==1:        #si page est à 1 on appele la fonction page1()
            self.page1()
        elif self.page==2:      #si page est à 2 on appele la fonction page2()
            self.page2()
        elif self.page==3:      #si page est à 3 on appele la fonction page3()
            self.page3()


    def page1(self):    # cette fonction permet d'affichée seulement la page 1 des aéroports français

        self.hide_page2()   # on appele la fonction hide_page2() qui va caché la page 2

        self.hide_page3()   # on appele la fonction hide_page2() qui va caché la page 3

        ################# on affiche tout les aéroports suivant ############### 
        self.Hartsfield_Jackson.show() 
        self.Pékin_Capitale.show() 
        self.Dubaï.show() 
        self.Los_Angeles.show() 
        self.Tokyo_Haneda.show() 
        self.Londres_Heathrow.show() 
        self.Francfort_sur_le_Main.show() 
        self.Paris_Charles_de_Gaulle.show() 
        self.Atatürk.show() 
        self.Paris_Orly.show()
        self.Lyon_Saint_Exupéry.show()
        self.Marseille_Provence.show()
        self.Toulouse_Blagnac.show()
        self.Bâle_Mulhouse_Fribourg.show()
        self.Bordeaux_Mérignac.show()
        self.Nantes_Atlantique.show()
        self.Beauvais_Tillé.show()
        self.Pointe_à_Pitre_Le_Raizet.show()

    def page2(self):    # cette fonction permet d'affichée seulement la page 1 des aéroports français

        self.hide_page1()   # on appele la fonction hide_page1() qui va caché la page 1

        ################# on affiche tout les aéroports suivant ############### 

        self.La_Réunion_Roland_Garros.show()
        self.Lille_Lesquin.show()
        self.Fort_de_France_Le_Lamentin.show()
        self.Montpellier_Méditerranée.show()
        self.Ajaccio_Napoléon_Bonaparte.show()
        self.Bastia_Poretta.show()
        self.Strasbourg_Entzheim.show()
        self.Brest_Bretagne.show()
        self.Biarritz_Pays_Basque.show()
        self.Rennes_Bretagne.show()
        self.Figari_Sud_Corse.show()
        self.Pau_Pyrénées.show()
        self.Nouméa_La_Tontouta.show()
        self.Cayenne_Félix_Eboué.show()
        self.Toulon_Hyères.show()
        self.Tarbes_Lourdes_Pyrénées.show()
        self.Nouméa_Magenta.show()
        self.Perpignan_Rivesaltes.show()


    def page3(self):    # cette fonction permet d'affichée seulement la page 3 des aéroports français

        self.hide_page2()   # on appele la fonction hide_page2() qui va caché la page 2

        ################# on affiche tout les aéroports suivant ############### 

        self.Clermont_Ferrand_Auvergne.show()
        self.Dzaoudzi_Pamandzi.show()
        self.Carcassonne_Salvaza.show()
        self.Calvi_Sainte_Catherine.show()
        self.Bora_Bora.show()
        self.Caen_Carpiquet.show()
        self.Lim.show()
        self.Bergerac_Dordogne_Périgord.show()
        self.Béziers_Cap_d_Agde.show()
        self.Metz_Nancy_Lorraine.show()
        self.Raiatea.show()
        self.La_Rochelle_Île_de_Ré.show()
        self.Nîmes_Alès_Camargue_Cévennes.show()
        self.Tours_Val_de_Loire.show()
        self.Lifou.show()
        self.Gustaf_III.show()
        self.Huahine.show()
        self.Deauville_Normandie.show()
        self.Poitiers_Biard.show()
    


    def hide_page1(self):   # cette fonction permet de cachée seulement la page 1 des aéroports français

        ################# on cache tout les aéroportss suivant ############### 

        self.Hartsfield_Jackson.hide()
        self.Pékin_Capitale.hide()
        self.Dubaï.hide()
        self.Los_Angeles.hide()
        self.Tokyo_Haneda.hide()
        self.Londres_Heathrow.hide()
        self.Francfort_sur_le_Main.hide()
        self.Paris_Charles_de_Gaulle.hide()
        self.Atatürk.hide()
        self.Paris_Orly.hide()
        self.Lyon_Saint_Exupéry.hide()
        self.Marseille_Provence.hide()
        self.Toulouse_Blagnac.hide()
        self.Bâle_Mulhouse_Fribourg.hide()
        self.Bordeaux_Mérignac.hide()
        self.Nantes_Atlantique.hide()
        self.Beauvais_Tillé.hide()
        self.Pointe_à_Pitre_Le_Raizet.hide()

    def hide_page2(self):   # cette fonction permet de cachée seulement la page 2 des aéroports français

        ################# on cache tout les aéroportss suivant ############### 

        self.La_Réunion_Roland_Garros.hide()
        self.Lille_Lesquin.hide()
        self.Fort_de_France_Le_Lamentin.hide()
        self.Montpellier_Méditerranée.hide()
        self.Ajaccio_Napoléon_Bonaparte.hide()
        self.Bastia_Poretta.hide()
        self.Strasbourg_Entzheim.hide()
        self.Brest_Bretagne.hide()
        self.Biarritz_Pays_Basque.hide()
        self.Rennes_Bretagne.hide()
        self.Figari_Sud_Corse.hide()
        self.Pau_Pyrénées.hide()
        self.Nouméa_La_Tontouta.hide()
        self.Cayenne_Félix_Eboué.hide()
        self.Toulon_Hyères.hide()
        self.Tarbes_Lourdes_Pyrénées.hide()
        self.Nouméa_Magenta.hide()
        self.Perpignan_Rivesaltes.hide()

    def hide_page3(self):   # cette fonction permet de cachée seulement la page 3 des aéroports français

        ################# on cache tout les aéroportss suivant ############### 

        self.Clermont_Ferrand_Auvergne.hide()
        self.Dzaoudzi_Pamandzi.hide()
        self.Carcassonne_Salvaza.hide()
        self.Calvi_Sainte_Catherine.hide()
        self.Bora_Bora.hide()
        self.Caen_Carpiquet.hide()
        self.Lim.hide()
        self.Bergerac_Dordogne_Périgord.hide()
        self.Béziers_Cap_d_Agde.hide()
        self.Metz_Nancy_Lorraine.hide()
        self.Raiatea.hide()
        self.La_Rochelle_Île_de_Ré.hide()
        self.Nîmes_Alès_Camargue_Cévennes.hide()
        self.Tours_Val_de_Loire.hide()
        self.Lifou.hide()
        self.Gustaf_III.hide()
        self.Huahine.hide()
        self.Deauville_Normandie.hide()
        self.Poitiers_Biard.hide()
        self.Montluçon_Guéret.hide()
        self.Dole_Jura.hide()
        self.Lorient_Bretagne_Sud.hide()
        self.Montluçon_Guéret.hide()
        self.Dole_Jura.hide()
        self.Lorient_Bretagne_Sud.hide()



    def changement_france(self):    # cette fonctionne permet de cachée ou d'affiché les pages des aéroports français
        self.france_page=self.france_page+1

        if self.france_page>=3:  # si france_page est à 3 ou plus grand on la passe à 1
            self.france_page=1

        if self.france_page==1: # si france_page est à 1 alors on affiché la page 1 des aéroportss français
            self.suivant.show()
            self.toutselectionne.show()
            self.ligne6.show()
            self.page1()


        elif self.france_page==2:   # si france_page est à 2 alors on cache toutes les pages des aéroportss français
            self.suivant.hide()
            self.toutselectionne.hide()
            self.ligne6.hide()
            
            self.hide_page1()
            self.hide_page2()
            self.hide_page3()
        
        
    def changement_autres(self):    # cette fonctionne permet de cachée ou d'affiché les aéroports non français
        self.autre_page=self.autre_page+1

        if self.autre_page>=3:  # si autre_page est à 3 ou plus grand on la passe à 1
            self.autre_page=1

        if self.autre_page==1:  # si autre_page est à 1 alors on cache les aéroportss non français
            self.autres_hide()

        elif self.autre_page==2:  # si autre_page est à 2 alors on affiché les aéroportss non français
            self.autres_show()


    def autres_hide(self):  # cette fonctionne permet de cachée les aéroports non français
        self.ligne5.hide()
        self.aéroports1.hide() 
        self.aéroports2.hide() 
        self.aéroports3.hide() 
        self.aéroports4.hide() 
        self.aéroports5.hide() 
        self.aéroports6.hide() 
        self.aéroports7.hide() 
        self.aéroports8.hide() 
        self.aéroports9.hide()
        self.aéroports11.hide() 

    def autres_show(self):  # cette fonctionne permet d'affiché les aéroports non français
        self.ligne5.show()
        self.aéroports1.show() 
        self.aéroports2.show() 
        self.aéroports3.show() 
        self.aéroports4.show() 
        self.aéroports5.show() 
        self.aéroports6.show() 
        self.aéroports7.show() 
        self.aéroports8.show() 
        self.aéroports9.show()
        self.aéroports11.show() 

# main --------------------------------------------------
if __name__ == "__main__":
    print(' --- main --- ')
    # création d'une QApplication
    app = QApplication(sys.argv)

    # création d'un widget
    f = VueAnnuaire()
    
    # lancement de l'application
    sys.exit(app.exec())