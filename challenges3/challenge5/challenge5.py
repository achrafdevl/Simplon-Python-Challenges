

def ecrire_fichier(chemin_fichier, lignes):
    with open(chemin_fichier, 'w') as f:
        for ligne in lignes:
            f.write(ligne + "\n")


chemin_fichier = 'challenges3/challenge5/fichier/fichier.txt'
lignes = ['Achraf have DAKA ', 'Hello Simplon teams', 'good neight']
ecrire_fichier(chemin_fichier, lignes)
