#! /bin/python

from pathlib import Path
import json

# Ce script va ajouter les informations des utilisateurs 
# dans le dictionnaire et les organiser avec des ID des positions
json_file = Path.home() / "Documents/projects/script/user_by_id.json"
json_file.touch(exist_ok=True)
# 1 - Définition du dictionnaire
dico = {0:{}}
# 1 - 1 Définition de la condition d'exécution de la boucle
nb_user = int(input("Combien d'utilisateur souhaiter vous enregistrer : "))

# 1 - 2 Ouverture du fichier
with open(json_file,"w") as file:
    # 2 - Boucle 
    for item in range(nb_user):
        dico[item] = {}
        dico[item]["nom"]=str(input("Entrer votre nom : "))
        dico[item]["age"]=int(input("Entrer votre âge : "))
        dico[item]["métier"]=str(input("Votre métier/occupation actuelle : "))
        json.dump(dico,file,indent=3)
print(dico)
