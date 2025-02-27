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

# Interface utilisateur pour sélectionner l'image d'origine
root = tk.Tk()
root.withdraw()  # Cacher la fenêtre principale de tkinter

print("Sélectionnez l'image d'origine :")
image_originale = charger_image()

if image_originale is not None:
    print("Sélectionnez l'image de gradient :")
    gradient = charger_image()

    if gradient is not None:
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
            print("Image traitée enregistrée sous le nom 'image_traitee.jpg'.")

        else:
            print("Les dimensions de l'image et du gradient ne correspondent pas.")
    else:
        print("Aucune image de gradient sélectionnée.")
else:
    print("Aucune image d'origine sélectionnée.")
