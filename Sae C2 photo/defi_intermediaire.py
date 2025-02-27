import cv2
import tkinter as tk
from tkinter import filedialog

# Fonction pour charger une image depuis un fichier
def charger_image():
    file_path = filedialog.askopenfilename(title="Sélectionnez une image", filetypes=[("Fichiers image", "*.jpg *.png *.bmp *.jpeg")])
    if file_path:
        image = cv2.imread(file_path)
        return image
    else:
        return None

# Fonction pour détecter le gradient dans une image
def detecter_gradient(image):
    # Convertir l'image en niveaux de gris
    image_gris = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Appliquer l'opérateur de Sobel pour détecter le gradient
    gradient_x = cv2.Sobel(image_gris, cv2.CV_64F, 1, 0, ksize=3)
    gradient_y = cv2.Sobel(image_gris, cv2.CV_64F, 0, 1, ksize=3)
    
    # Calculer la magnitude du gradient
    gradient_magnitude = cv2.magnitude(gradient_x, gradient_y)
    
    return gradient_magnitude

# Interface utilisateur pour sélectionner l'image d'origine
root = tk.Tk()
root.withdraw()  # Cacher la fenêtre principale de tkinter

image_originale = charger_image()

if image_originale is not None:
    # Interface utilisateur pour sélectionner l'image du gradient
    gradient = charger_image()

    if gradient is not None:
        # Vérifier que les dimensions de l'image et du gradient correspondent
        if image_originale.shape == gradient.shape:
             # Soustraire le gradient de l'image
            image_traitee = cv2.subtract(image_originale, gradient)

            # Afficher l'image d'origine
            cv2.imshow("Image d'Origine", image_originale)
            cv2.waitKey(0)

            # Afficher l'image traitée
            cv2.imshow("Image Traitee", image_traitee)
            cv2.waitKey(0)
            
            # Enregistrer l'image traitée
            cv2.imwrite("image_traitee.jpg", image_traitee)

            # Détecter le gradient dans l'image d'origine
            gradient_magnitude = detecter_gradient(image_originale)
            cv2.imshow("Gradient dans l'Image d'Origine", gradient_magnitude)
            cv2.waitKey(0)

        else:
            print("Les dimensions de l'image et du gradient ne correspondent pas.")
    else:
        print("Aucune image de gradient sélectionnée.")
else:
    print("Aucune image d'origine sélectionnée.")
