from random import*

# liste des produits 
liste_produits = ["La flûte" ,"baguette traditionelle","baguette paysane","pain rond","pain sportif","La baguette moulée","La baguette en épi",
           "jambon","beurre","crème fraîche","lardon","yaourt","fromage","lait","Tofu","oeufs","pizza","frites","Mini cheeseBurgers",
           "Pastis","Cognac","triple-sec","Vin","vin blanc","Whisky","Rhum","Muguets","Rose","marguerite","tulipe","hibiscus","Rockstar","RedBull","Coca",
           "Eau","Fanta","Orangina","café","Ice Tea","chips","bretzel","pistaches","Vetements","bricolage","jouets","Carglass","peluche",
           "nourriture animal","clavier","caméra","Produit_anti-insectes","lessive","dentifrice","maquillage","Couche","Démaquillant","papier-toilette",
           "brosse_a_dent","rouge à lèvre","croissant","pain au chocolat","brioche","chausson aux pommes","donuts","beignets","Saucisson", "Coppa", "Rosette", "Salami", "chorizo",
           "Jägermeister","Pinard","Mezcal","Brandy","Tequilla","Banane","Poire","pomme","ananas","orange","tomate","brocoli","choux-fleur",
           "carotte","petit pois","Pomme_bio","Steack_Végetal""Armagnac","avocat","LeParisien","VoixDuNord","France-Presse","Nord_Litoral","Carte pokémon",
           "PS5","blanc de calmar","cuisse de grenouille","tapas","escargots"]

#Référencement de tout les produits pour les courses
course= { 'Pain' : { "La flûte" : (0,8) ,"baguette traditionelle" : (0,9) , "baguette paysane" : (0,9) , "pain rond" : (0,10) , "pain sportif" : (0,10) ,"La baguette moulée" : (0,11) , "La baguette en épi" :(0,11)} , 
        'Frais' : {"jambon" :(10,0) , "beurre" :(0,1) , "crème fraîche" :(0,2), "lardon" :(9,0) ,"yaourt" :(0,3) , "fromage" :(8,0),"lait" :(0,4),"Tofu" :(7,0),"œufs" :(0,5)},
        'Alcool' : {"Pastis" :(4,8) , "Cognac":(4,8), "triple-sec" :(4,9),"Vin" :(4,7),"vin blanc":(4,7),"Whisky" :(4,10),"Rhum" :(4,10)},
        'Surgelés' : {"pizza" :(12,1), "frites":(10,4), "Mini cheeseBurgers" :(12,2)},
        'Fleurs' : {"Muguets" :(2,5),"Rose" :(2,5) , "marguerite" :(2,5) ,"tulipe" :(2,5),"hibiscus" :(2,5)},
        'Boissons' :  {"Rockstar" :(12,7), "RedBull": (12,7) , "Coca":(12,8),"Eau" :(12,9) ,"Fanta" :(12,8) , "Orangina":(12,8) , "café" :(12,10),"Ice Tea" :(12,9)},
        'Salé' : {"chips" :(2,7) ,"bretzel" :(2,7),"pistaches" :(2,7)},
        'Non_alimentaire' :  {"Vetements" :(6,2) ,"peluche" :(6,3),"jouets":(6,3),"bricolage" :(6,4),"Carglass":(6,5) ,"clavier" :(8,2), "caméra" :(8,3),"Produit_anti-insectes" :(8,4),"nourriture animal" :(8,5)},
        'DPH': {"lessive": (8,7), "dentifrice": (8,10) , "maquillage": (8,9) , "Couche": (8,8) , "Démaquillant": (8,9) , "papier-toilette" : (8,7) , "brosse_a_dent": (8,10) , "rouge à lèvre":(8,9)},
        'Viennoiserie' : {"croissant": (6,7 ), "pain au chocolat": (6,7), "brioche": (6,8), "chausson aux pommes": (6,8), "donuts": (6,9), "beignets": (6,9) },
        'SEC' : {"Saucisson": (10,7), "Coppa": (10,7), "Rosette": (10,8), "Salami": (10,9), "chorizo": (10,9)},
        'Spiritueux' : {"Jägermeister": (12,12),"Pinard": (12,12),"Mezcal": (12,12),"Brandy": (12,12),"Tequilla": (12,12)},
        'Fruit_Légume' : {"Banane": (2,9),"Poire": (2,9),"pomme": (2,9),"ananas": (2,9),"orange": (2,9),"tomate": (2,10),"brocoli": (2,10),"choux-fleur": (2,10),"carotte": (2,10),"petit pois": (2,10)},
        'Bio' : {"Pomme_bio" :(0,6) , "Steack_Végetal":(0,6)},
        'Promos' : {"Armagnac":(2,12),"avocat":(2,12)},
        'WP' : {"LeParisien":(2,3),"LaVoixDuNord":(2,3),"France-Presse":(2,2),"Nord_Litoral":(2,2)},
        'Spiritueux' : {"Jägermeister": (12,12),"Pinard": (12,12),"Mezcal": (12,12),"Brandy": (12,12),"Tequilla": (12,12)},
        'Fruit_Légume' : {"Banane": (2,9),"Poire": (2,9),"pomme": (2,9),"ananas": (2,9),"orange": (2,9),"tomate": (2,10),"brocoli": (2,10),"choux-fleur": (2,10),"carotte": (2,10),"petit pois": (2,10)},
        'Produit_temporaire' : {"Carte pokémon": (4,3),"PS5": (4,4)},
        'Frais_temporaire' : {"blanc de calmar": (2,0),"cuisse de grenouille": (2,0),"tapas": (3,0),"escargots": (4,0)}}

#fonction pour faire une liste de 20 produits aléatoires
def liste_aleatoire(): 
    liste_course_aleatoire =[]
    
    for i in range (0,3):
        aleatoire = choice(liste_produits)
        for k in course.keys():
            v = course[k]
            if aleatoire in v.keys():
                produit = (aleatoire , v[aleatoire])
                liste_course_aleatoire.append(produit)
        
    return liste_course_aleatoire
                            
print(liste_aleatoire())

