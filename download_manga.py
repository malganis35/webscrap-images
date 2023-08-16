import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# URL de la page web à partir de laquelle vous souhaitez télécharger les images
url = "https://yourlieinaprilmanga.com/manga/your-lie-in-april-chapter-1/"  # Remplacez par l'URL de votre choix

# Dossier de destination pour enregistrer les images
destination_folder = "images"
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Obtenir le contenu HTML de la page
response = requests.get(url)
html_content = response.text

# Créer un objet BeautifulSoup pour analyser le HTML
soup = BeautifulSoup(html_content, "html.parser")

# Trouver toutes les balises <img> qui ont un attribut src se terminant par .jpg
image_tags = soup.find_all("img", src=lambda src: src and src.endswith(".jpg"))

# Télécharger et enregistrer les images
for img_tag in image_tags:
    img_url = img_tag["src"]
    img_url = urljoin(url, img_url)  # Gérer les URLs relatives
    img_name = os.path.basename(img_url)
    img_path = os.path.join(destination_folder, img_name)

    # Télécharger l'image
    img_response = requests.get(img_url)
    if img_response.status_code == 200:
        with open(img_path, "wb") as img_file:
            img_file.write(img_response.content)
        print(f"Image {img_name} téléchargée avec succès.")
    else:
        print(f"Impossible de télécharger l'image {img_name}.")

print("Téléchargement des images terminé.")