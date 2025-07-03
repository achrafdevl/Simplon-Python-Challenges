import os

def verifier_fichier_config(repertoire):
    chemin_fichier = os.path.join(repertoire, 'config.yaml')
    if os.path.exists(chemin_fichier):
        with open(chemin_fichier, 'r') as f:
            contenu = f.read()
            print(contenu)
    else:
        print("Le fichier config.yaml n'existe pas.")

repertoire = 'challenges3/challenge2/fichier'
verifier_fichier_config(repertoire)
